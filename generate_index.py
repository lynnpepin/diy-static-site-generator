"""generate_index.py

A simple script that should loop over all the HTML files and generate a simple
index.md of them all.

Goal is to organize most recent 10 posts, and then list all posts by category.
"""

import os
from pathlib import Path
import lxml.html

def parse_markdown_for_html(filename, default="Untitled post"):
    """
    Loads a Markdown file, and looks for a line of the form `Title:`.
    This function doesn't actually work yet!
    Yeah I'm pushing code that won't work to master, what's wrong?
    
    :param filename: String or Path, pointing to a Markdown file to be parsed.
    :param default: String. Return this if no filename is found.
    :returns: String. Title of post.
    """
    with open(filename, "r") as f:
        line = f.readline()
        while line is not '':
            if "title:" in line:
                # cheap way to process the 'title:' out of a line.
                return line.split("title:")[-1].strip()
            
            line = f.readline()
     
    return default


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


def main(out_file = "source/index.md", target_folder = "./site/posts/"):
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
        f.write("""
---
title: "Blog index"
author:
 - Lynn
abstract: Site homepage
date: 2020 Sept 4
lang: en-US
---

""")
        #f.write("# All posts, by date.\n\n")
        for html_post in html_posts:
            # e.g. link_to_post = ./posts/my_cool_post.html
            link_to_post = "./" + "/".join(html_post.parts[1:])
            #get post title:
            #post_title = parse_markdown_for_html(html_post) -- doesn't work!
            post_title = get_attribute_from_html(html_post, "title", "Untitled post")
            post_date = get_attribute_from_html(html_post, "date", "-")
            f.write(f"{post_date}: [{post_title}]({link_to_post})\n\n")


if __name__ == '__main__':
    main()
