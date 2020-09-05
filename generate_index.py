"""generate_index.py

A simple script that should loop over all the HTML files and generate a simple
index.md of them all.

Goal is to organize most recent 10 posts, and then list all posts by category.
"""

import os
from pathlib import Path
import lxml.html

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
        f.write("# All posts, by date.\n\n")
        for html_post in html_posts:
            # e.g. link_to_post = ./posts/my_cool_post.html
            link_to_post = "./" + "/".join(html_post.parts[1:])
            post_title = lxml.html.parse(str(html_post)).find(".//title").text
            f.write(f"[{post_title}]({link_to_post})\n\n")

if __name__ == '__main__':
    main()
