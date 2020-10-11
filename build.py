"""
build.py

The primary script used to build the static site.


"""
import os
import subprocess
import shutil
from pathlib import Path
import argparse
import lxml.html

# todo: use pandoc package instead of subprocess?
# todo: use just os, or just subprocess, or just shutil? seems messy
# todo: go OS-agnostic using pathlib


def _copytree_and_overwrite(src, dst):
    # helper function
    # copy the entire tree  from src,
    # overwriting the ENTIRE destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def makedirs_if_not_exist(path):
    """
    Wraps os.makedirs to prevent errors

    :param path: Path of folders to make
    """
    if not os.path.exists(path):
        os.makedirs(path)

def remove_if_exists(path):
    """
    Wraps os.remove to prevent rerrors.

    :param path: Path to remove
    """
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

def get_title(filename, default="Untitled post"):
    """
    Read an HTML file for the title, returning 'default' if it doesn't work.

    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param default: String. Return this if no attribute is found.
    :returns: String. Title of post.
    """

    post_text = lxml.html.parse(str(filename)).find(f".//title")

    if post_text is not None:
        return post_text.text
    else:
        return default

def get_date(filename, default="----/--/--"):
    """
    Read an HTML file for the date, returning 'default' if it doesn't work.

    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param default: String. Return this if no attribute is found.
    :returns: String representing date of post.
    """
    try:
        return lxml.html.parse(str(filename)).find(f".//time").values()[0]
    except:
        return "-"


def generate_index(out_file = "source/index.md",
                   target_folder = "./site/posts/"):
    """
    Generates an index Markdown file at `out_file`, to later be compiled by pandoc.
    
    Combs through all the posts in `target_folder`, to be placed in the index.
    
    :param out_file: String; path to place the index markdown in.
    :param target_folder: String; folder to look for posts in.
    """
    # TODO: Properly parse by time
    html_posts = reversed(sorted(Path(target_folder).iterdir(), key=os.path.getmtime))
    out_path = Path(out_file)
    # create / blank index.md if it does not exist
    with open(out_file, "w") as f:
        # todo: automate date
        # todo: there are better ways to do this in Python
        f.write("---\n")
        f.write("title: \"Blog index\"\n")
        f.write("lang: en-US\n")
        f.write("---\n")

        # todo- lang param?
        #f.write("# All posts, by date.\n\n")
        for html_post in html_posts:
            # e.g. link_to_post = ./posts/my_cool_post.html
            link_to_post = "./" + "/".join(html_post.parts[1:])
            #get post title:
            post_title = get_title(html_post, "Untitled post")
            # can't get post_date yet! todo
            post_date = get_date(html_post, "-")
            f.write(f"{post_date} : [{post_title}]({link_to_post})\n\n")



def main(style="source/themes/minimalist.css",
         template="source/themes/layout.html",
         build_index=True,
         cleanup=True,
         copy_readme=False,
         verbose=True):
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

    # initialize empty site/ directory
    _vprint("Initializing directories.")
    makedirs_if_not_exist("site")
    makedirs_if_not_exist("site/posts")
    makedirs_if_not_exist("site/images")
    makedirs_if_not_exist("site/fonts")

    # copy over theme files.
    _vprint("Copying over style and fonts!")
    _vprint(f"... Using {style}")
    shutil.copy(style, "site/style.css")
    _copytree_and_overwrite("fonts/", "site/fonts/")
    # cludge to get the screenshot used in README.md
    if copy_readme:
        shutil.copy("images/screenshot.png", "site/images/screenshot.png")

    # Build header, footer, body preamble, to be put in each document
    # header is the top of the document
    _vprint("Building extra files.")
    # bodybar, footer, header
    subprocess.call(["pandoc", "-c", "style.css",
                     "./source/header.md",
                     "-o", "./site/header.html"])
    subprocess.call(["pandoc", "-c", "style.css",
                     "./source/bodybar.md",
                     "-o", "./site/bodybar.html"])
    subprocess.call(["pandoc", "-c", "style.css",
                     "./source/footer.md",
                     "-o", "./site/footer.html"])

    # Build any post ending in .md
    # TODO: FROM HERE
    _vprint("Building posts!")
    for filename in os.listdir("source/posts/"):
        _vprint(f"... Building {filename}")
        if filename[-3:] == ".md":
            subprocess.call(["pandoc", "-c", "../style.css",
                             "-H", "site/header.html",
                             "-B", "site/bodybar.html",
                             "-A", "site/footer.html",
                             "--mathjax", f"./source/posts/{filename}",
                             "--template", f"{template}",
                             "-o", f"site/posts/{filename[:-3]}.html"])

    # Create the index.html file
    if build_index:
        _vprint("Building index...")
        generate_index()

        # build index.html
        subprocess.call(["pandoc", "-s", "-c", "style.css",
                         "-H", "site/header.html",
                         "-B", "site/bodybar.html",
                         "-A", "site/footer.html",
                         "./source/index.md",
                         "--template", f"{template}",
                         "-o", "site/index.html"])
    # Build about page
    _vprint("Building about...")
    subprocess.call(["pandoc", "-s", "-c", "style.css",
                     "-H", "site/header.html",
                     "-B", "site/bodybar.html",
                     "-A", "site/footer.html",
                     "./source/about.md",
                     "--template", f"{template}",
                     "-o", "site/about.html"])

    # 6. Cleanup: Remove header.html, bodybar.html, footer.html
    if cleanup:
        _vprint("Cleaning up!")
        os.remove("./site/header.html")
        os.remove("./site/bodybar.html")
        os.remove("./site/footer.html")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build your blog from what's in `source/`")

    # Add arguments
    parser.add_argument("--style", "-c", default=["source/themes/minimalist.css"],
                        help="Source for the CSS file to use for this site.",
                        type=str, nargs=1)
    parser.add_argument("--template", "-D", default=["source/themes/layout.html"],
                        help="Source for the Pandoc layout to use for this site.",
                        type=str, nargs=1)
    parser.add_argument("--ignore_index", default=False,
                        help="Do not build the index from source/index.md",
                        action="store_true")
    parser.add_argument("--no_cleanup", default=False,
                        help="Do not remove intermediary files (footer.md, etc.)",
                        action="store_true")
    parser.add_argument("--copy_readme", default=False,
                        help="Build `README.md` as a post; site/posts/README.html",
                        action="store_true")
    parser.add_argument("--verbose", "-v", default=False,
                        help="Print extra information.", action="store_true")
    
    args = parser.parse_args()

    _vprint = print if args.verbose else lambda *a, **k: None
    
    main(style=args.style[0],
         template=args.template[0],
         build_index=not args.ignore_index,
         cleanup=not args.no_cleanup,
         copy_readme=args.copy_readme)
