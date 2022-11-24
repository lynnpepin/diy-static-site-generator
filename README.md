# lynndotpy.xyz static site generator

In 2020 I made a static site generator for a personal blog. Three big components:

 - an UGLY ad-hoc python script `build.py`.

 - pandoc for markdown-> html + custom template

 - hand rolled CSS.

![Screenshot of a this README, without the screenshot, rendered using this blog.](/images/screenshot.png)

## How to use this

**Step 1: Don't use this.** I made this for my own education. It's isn't good! It's not supposed to be and isn't going to be! It's full of ugly cludges that I could but won't fix. 

### But seriously, how can I use this?

1. Put your Markdown posts in `posts/`,
2. run `python build.py`,
3. and point your HTTP server at `site/`!


### Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.
 * This code makes assumptions that you're on a Unix-like system-- paths and whatnot probably won't work with Windows!


### Filestructure

 * `build.py` -- Renders files in `source/` and puts them in `site/`!
 * `source/themes/minimalist.css` -- A simple theme for the blog.
 * `source/themes/template.html` -- Pandoc HTML template.
 * `source/` -- Edit these files!
    * `header.md` -- Appended to the top of every page
    * `footer.md` -- Appended to the bottom of every page
    * `bodybar.md` -- Placed just before the body of each page
    * `about.md` -- Custom "about" page.
    * `posts/`-- Markdown posts go here! (Most important directory.)
 * `site/` -- The site files are placed here. (Point your HTTP server here!)

