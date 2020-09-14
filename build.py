#!/bin/sh
import os
import subprocess
import shutil
from pathlib import Path
import argparse
import lxml.html

## TODOS:
# 1. Make OS agnostic
# 2. Avoid subprocess.call(); prefer os/system/shutil copy functions.

def makedirs_if_not_exist(path):
    """
    Wraps os.makedirs to prevent errors
    
    :param path: Path of folders to make
    """
    if not os.path.exists(path):
        os.makedirs(path)


def get_attribute_from_html(filename, attribute="title", default="Untitled post"):
    """
    Read an HTML file for an attribute, returning 'default' if it doesn't work.
    
    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param attribute: String, the attribute that is to be found.
    :param default: String. Return this if no attribute is found.
    :returns: String. Title of post.
    """
    
    post_text = lxml.html.parse(str(filename)).find(f".//{attribute}")
    
    if post_text is not None:
        return post_text.text
    else:
        return default


def generate_index(out_file = "source/index.md",
                   target_folder = "./site/posts/"):
    """
    :param out_file: String; path to place the index markdown in.
    :param target_folder: String; folder to look for posts in.
    """
    html_posts = sorted(Path(target_folder).iterdir(), key=os.path.getmtime)
    # https://stackoverflow.com/questions/168409/
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
            #post_title = parse_markdown_for_html(html_post) -- doesn't work!
            post_title = get_attribute_from_html(html_post, "title", "Untitled post")
            post_date = get_attribute_from_html(html_post, "date", "-")
            f.write(f"{post_date}: [{post_title}]({link_to_post})\n\n")


def _vprint(verbose=True, x=""):
    if verbose:
        print(x)


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

    if copy_readme:
        # copy readme file over as a post
        _vprint(verbose, "Copying README to build as post.")
        shutil.copy("README.md", "./source/posts/README.md")

    # initialize directories
    _vprint(verbose, "Initializing directories.")
    makedirs_if_not_exist("site")
    makedirs_if_not_exist("site/posts")
    makedirs_if_not_exist("site/images")
    makedirs_if_not_exist("site/fonts")
    
    # copy over files
    _vprint(verbose, "Copying over style and fonts!")
    shutil.copy(style, "site/style.css")
    # TODO: Make this OS agnostic
    #os.system("cp fonts/ site/fonts")
    subprocess.call(["cp", "-r", "fonts/", "site/fonts"])
    if copy_readme:
        shutil.copy("images/screenshot.png", "site/images/screenshot.png")
    
    
    # Build header, footer, body preamble, to be put in each document
    # header is the top of the document
    _vprint(verbose, "Building extra files.")
    # bodybar, footer, header
    subprocess.call(["pandoc", "-c", "style.css", "./source/header.md", "-o", "./site/header.html"])
    subprocess.call(["pandoc", "-c", "style.css", "./source/bodybar.md", "-o", "./site/bodybar.html"])
    subprocess.call(["pandoc", "-c", "style.css", "./source/footer.md", "-o", "./site/footer.html"])

    # Build any post ending in .md
    # TODO: FROM HERE
    _vprint(verbose, "Building posts!")
    for filename in os.listdir("source/posts/"):
        _vprint(verbose, f"... Building {filename}")
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
        _vprint(verbose, "Building index...")
        generate_index()
        
        # build index.html
        subprocess.call(["pandoc", "-s", "-c", "style.css",
                         "-H", "site/header.html",
                         "-B", "site/bodybar.html",
                         "-A", "site/footer.html",
                         "./source/index.md",
                         "--template", f"{template}",
                         "-o", "site/index.html"])
        #os.system(f"pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/index.md --template {template} -o site/index.html")

    # Build about page
    _vprint(verbose, "Building about...")
    subprocess.call(["pandoc", "-s", "-c", "style.css",
                     "-H", "site/header.html",
                     "-B", "site/bodybar.html",
                     "-A", "site/footer.html",
                     "./source/about.md",
                     "--template", f"{template}",
                     "-o", "site/about.html"])
    #os.system(f"pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/about.md --template {template} -o site/about.html")

    # 6. Cleanup: Remove header.html, bodybar.html, footer.html
    if cleanup:
        _vprint(verbose, "Cleaning up!")
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
                        
    args = parser.parse_args()
    
    main(style=args.style[0],
         template=args.template[0],
         build_index=not args.ignore_index,
         cleanup=not args.no_cleanup,
         copy_readme=args.copy_readme)
