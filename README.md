# DIY Static Site Generator

A DIY approach to static site generation, using Pandoc.

![Screenshot of a this README, without the screenshot, rendered using this blog.](/images/screenshot.png)

## How to use

1. Put your Markdown posts in `posts/`,
2. run `./build.sh`,
3. and point your HTTP server to `site/`!

### Filestructure

 * `build.sh` -- (Old). Renders files in `source/` and puts them in `site/`!
 * `build.py` -- (WIP). Renders files in `source/` and puts them in `site/`!
 * `source/themes/minimalist.css` -- A simple theme for the blog.
 * `source/themes/template.html` -- Pandoc HTML template.
 * `source/` -- Edit these files!
    * `header.md` -- Appended to the top of every page
    * `footer.md` -- Appended to the bottom of every page
    * `bodybar.md` -- Placed just before the body of each page
    * `about.md` -- Custom "about" page.
    * `posts/`-- Markdown posts go here!
 * `site/` -- Site is hosted here. (Point your HTTP server hre!)

## Things this could still use

### Improve `build.py`:

I want to replace `build.sh` entirely with a Python script.

* Finish it-- it must run without errors!
* Make all paths, etc. as parameters. (`source`, `site`, etc.)
* Should raise descriptive errors.
* Plus an extra "verbosity" command.
* Use OS-agnostic path handling. 
* Avoid using subprocess.call for
* Fix linter and lint.

### Improve `index.html`

* Parse dates (stored as actual dates, not strings)
* Parse dates and titles without `lxml`; draw from Markdown instead.
* Index page should organize by category and then by date.
* Build a by-category page.
 * "Featured" blogposts

### Other

 * Make this pretty for "public release".
 copying; fix!
 * RSS feed generator
 * Make optional "table of contents" jump in posts.
 * More themes!
    * Make CSS + Pandoc-template packs
 * Code boxes in CSS should scroll when overwidth.
 * Make a "sanity check" test 

## Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.
 * This code makes assumptions that you're on a Unix-like system-- paths and whatnot probably won't work with Windows!

