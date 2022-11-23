""" build.py -- This builds the static site! 
"""

import os
import subprocess
import shutil
from pathlib import Path
import argparse
import lxml.html

_vprint = print

def _copytree_and_overwrite(src, dst):
    '''Removes `dst`, then copies the entirety of src to dst'''
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def makedirs_if_not_exist(path):
    """
    Wraps os.makedirs to prevent errors when path does not exist.

    :param path: Path of folders to make
    """
    if not os.path.exists(path):
        os.makedirs(path)


def remove_if_exists(path):
    """
    Removes a file or directory if it exists at the path.

    :param path: Path to remove
    """
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)


def get_title(filename, default="Untitled post"):
    """
    Read an HTML file, returning the <title>, or `default` if not found.

    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param default: String. Return this if no attribute is found.
    :returns: String. Title of post.
    """
    post_text = lxml.html.parse(str(filename)).find(f".//title")

    if post_text is not None:
        return post_text.text
    else:
        return default


def get_date(filename, default="    -  -  "):
    """
    Read an HTML file for the date, returning 'default' if it doesn't work.

    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param default: String. Return this if no attribute is found.
    :returns: String representing date of post.
    """
    try:
        return lxml.html.parse(str(filename)).find(f".//time").values()[0]
    except:
        return default


def _get_and_sort_posts(target_folder = "./site/posts/", newest_first=True):
    """
    Find all the HTML files in  target_folder, sorted by the time metadata.
    # html_posts: list of posix_path
    
    returns a list of tuple of string (date), PosixPath

    e.g. 

    >>> build._get_and_sort_posts()
    [('2022-5-22', PosixPath('site/posts/python_mobile.html')),
     ('2022-1-7', PosixPath('site/posts/linear_sorting.html')),
     ('2021-5-15', PosixPath('site/posts/reso_intro.html')),
     ('2021-04-30', PosixPath('site/posts/seo_dating_spam.html')),
     ('2020-12-31', PosixPath('site/posts/gimp_and_python.html'))
    ]
    """
    # get List of Posix Path
    html_posts = list(reversed(list(Path(target_folder).iterdir())))
    # get matching list of dates (strings)
    dates = [get_date(post) for post in html_posts]
    dates_and_posts = list(zip(dates, html_posts))
    dates_and_posts.sort(key = lambda pair: pair[0])
    if newest_first:
        dates_and_posts.reverse()

    return dates_and_posts
    
   
def generate_index(out_file = "source/index.md", target_folder = "./site/posts/"):
    """
    Generates an index Markdown file at `out_file`, to later be compiled by pandoc.
    
    Combs through all the posts in `target_folder`, to be placed in the index.
    
    :param out_file: String; path to place the index markdown in.
    :param target_folder: String; folder to look for posts in.
    """
    # TODO
    out_path = Path(out_file)
    # create / blank index.md if it does not exist
    
    # build index.md by line
    #TODO: Sort by date?
    with open(out_file, "w") as f:
        # todo: automate date; there are better ways to do this in Python
        f.write("---\n")
        f.write("title: \"Blog index\"\n")
        f.write("lang:  en-US\n")
        f.write("---\n")
        
        for date, post in _get_and_sort_posts(target_folder=target_folder):
            link_to_post = "./" + "/".join(post.parts[1:])
            year, month, _ = date.split('-')
            month_str = ['','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'][int(month)]
            link_to_post = "./" + "/".join(post.parts[1:])
            #get post title
            post_title = get_title(post)
            f.write(f"`{year} {month_str}`\t::\t[{post_title}]({link_to_post})\n\n")


def _generate_rss():
    # TODO
    '''Read from 
    From list of dict 'entries', generate RSS

    Each entry has keys 'title', 'link', 'updated'.
    '''
    pass
    
    rss_out = (
        "<feed xmlns=\"http://www.w3.org/2005/Atom\" xml:lang=\"en\">\n"
        "  <title>lynndotpy cyberadobe weblog</title>\n"
        "  <id>https://lynndotpy.xyz</id>\n"
        "  <updated>TODO</updated>\n"
    )
    for entry in entries:
        rss_out += (
            f"  <entry>\n"
            f"    <title>{1}</title>\n"
            f"    <link href=\"{1}\" rel=\"alternate\"/>\n"
            f"    <updated>{1}</updated>\n"
            f"    <id>{1}</id>\n"
            f"  </entry>\n"
        )
    
    return rss_out


# Main
def main(
    style="source/themes/colorful.css",
    template="source/themes/layout.html",
    build_index=True,
    cleanup=True,
    copy_readme=False,
    verbose=True
):
    """
    Build the entire site from `source`, into `site`

    :param style: String. Path to the desired .css file.
    :param template: String. Path to the desired Pandoc template file.
    :param build_index: Boolean. If True, will create site/index.html from
        source/index.md
    :param cleanup: Boolean. If True, will remove footer.html, header.html, and
        bodybar.html after creating them.
    :param copy_readme: Boolean. If True, will build README.md into as post
        as site/posts/README.html
    :param verbose: Boolean. Prints extra info if true.
    """
    # empty out "site/"
    remove_if_exists("site")

    # copy readme file over as a post
    if copy_readme:
        _vprint("Copying README to build as post.")
        shutil.copy("README.md", "./source/posts/README.md")
    else:
        remove_if_exists("./source/posts/README.md")

    # initialize empty site/ directory
    _vprint("Initializing directories.")
    makedirs_if_not_exist("site")
    makedirs_if_not_exist("site/posts")
    makedirs_if_not_exist("site/images")
    makedirs_if_not_exist("site/fonts")

    # copy over theme files.
    _vprint("Copying over style and fonts! Copying {style} to site/style.css")
    shutil.copy(style, "site/style.css")
    _copytree_and_overwrite("fonts/", "site/fonts/")
    # cludge to get the screenshot used in README.md
    if copy_readme:
        shutil.copy("images/screenshot.png", "site/images/screenshot.png")

    # copy image files
    # i should really decide if it's gonna be `source/images` or `images/`
    _vprint("Copying images!")
    for filename in os.listdir("source/images/"):
        _vprint(f"... Building {filename}")
        shutil.copy(f"source/images/{filename}", f"site/images/{filename}")

    # Build header, footer, body preamble, to be put in each document
    _vprint("Building extra files.")
    # bodybar, footer, header
    for element in ("header", "bodybar", "footer"):
        subprocess.call(
            [
                "pandoc",
                "-c", "style.css",
                f"./source/{element}.md",
                "-o", f"./site/{element}.html"
            ]
        )

    # Build any post ending in .md
    _vprint("Building posts!")
    for filename in os.listdir("source/posts/"):
        _vprint(f"... Building {filename}")
        if filename[-3:] == ".md":
            subprocess.call(
                [
                    "pandoc", "-c", "../style.css",
                    "-H", "site/header.html",
                    "-B", "site/bodybar.html",
                    "-A", "site/footer.html",
                    "--mathjax", f"./source/posts/{filename}",
                    "--template", f"{template}",
                    "-o", f"site/posts/{filename[:-3]}.html",
                ]
            )

    # Create the index.html file
    if build_index:
        _vprint("Building index...")
        generate_index()

        # build index.html
        subprocess.call(
            [
                "pandoc", "-s", "-c", "style.css",
                "-H", "site/header.html",
                "-B", "site/bodybar.html",
                "-A", "site/footer.html",
                "./source/index.md",
                "--template", f"{template}",
                "-o", "site/index.html"
            ]
        )
    
    # Build about page
    _vprint("Building about...")
    subprocess.call(
        [
            "pandoc", "-s", "-c", "style.css",
            "-H", "site/header.html",
            "-B", "site/bodybar.html",
            "-A", "site/footer.html",
            "./source/about.md",
            "--template", f"{template}",
            "-o", "site/about.html"
        ]
    )
                     
    # Build projects page
    _vprint("Building projects...")
    subprocess.call(
        [
            "pandoc", "-s", "-c", "style.css",
            "-H", "site/header.html",
            "-B", "site/bodybar.html",
            "-A", "site/footer.html",
            "./source/projects.md",
            "--template", f"{template}",
            "-o", "site/projects.html"
        ]
    )
    
    # Copy every 'favicon' item to 
    _vprint("Copying favicon...")
    makedirs_if_not_exist("site/favicon_package/")
    _copytree_and_overwrite("source/favicon_package/", "site/favicon_package/")
    shutil.copy("source/favicon_package/favicon.ico", "site/favicon.ico")


    # 6. Cleanup: Remove header.html, bodybar.html, footer.html
    if cleanup:
        _vprint("Cleaning up!")
        for element in ("header", "bodybar", "footer"):
            os.remove(f"./site/{element}.html")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build your blog from what's in `source/`")

    # Add arguments
    parser.add_argument(
        "--style", "-c",
        default=["source/themes/colorful.css"],
        help="Source for the CSS file to use for this site.",
        type=str, nargs=1
    )
    parser.add_argument(
        "--template", "-D",
        default=["source/themes/layout.html"],
        help="Source for the Pandoc layout to use for this site.",
        type=str, nargs=1
    )
    parser.add_argument(
        "--ignore_index",
        default=False,
        help="Do not build the index from source/index.md",
        action="store_true"
    )
    parser.add_argument(
        "--no_cleanup",
        default=False,
        help="Do not remove intermediary files (footer.md, etc.)",
        action="store_true"
    )
    parser.add_argument(
        "--copy_readme", "-r",
        default=False,
        help="Build `README.md` as a post; site/posts/README.html",
        action="store_true"
    )
    parser.add_argument(
        "--verbose", "-v",
        default=False,
        help="Print extra information.", action="store_true"
    )
    
    args = parser.parse_args()

    # Verbose print function redefined here. Horrible scope graph! Bad code here!
    _vprint = print if args.verbose else lambda *a, **k: None
    
    main(
        style=args.style[0],
        template=args.template[0],
        build_index=not args.ignore_index,
        cleanup=not args.no_cleanup,
        copy_readme=args.copy_readme
    )
