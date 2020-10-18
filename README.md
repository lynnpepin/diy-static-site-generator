# DIY Static Site Generator

A DIY approach to static site generation, using Pandoc.

![Screenshot of a this README, without the screenshot, rendered using this blog.](/images/screenshot.png)

## How to use this

**Step 1: Don't use this.** I made this for my own education. It's unfinished and lacks features! I'm not a web developer!

Also, it's full of cludges! *This is not a good piece of software engineering!* Marvel at the lack of tests! See how it is not properly portable!

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

## Improvements and TODOs

### Things to style:
* `<aside>`
* `<abbr>`
* `<cite>`
* `<del>`
* `<ins>`
* `<sub>`
* `<sup>`
* `<var>`
* `<mark>`
* `<kbd>`

### Improve `build.py`:

I want to replace `build.sh` entirely with a Python script, `build.py`.

* Make all paths, etc. as parameters. (`source`, `site`, etc.)
* Should raise descriptive errors.
* Plus an extra "verbosity" command.
* Use OS-agnostic path handling.

### Improve `index.html`

* Parse dates and titles without `lxml`; draw from Markdown instead!
   * Would require refactoring the workflow...
* Index page should organize by category too...
* And then list the top 10 posts.
* Build a by-category page.
   * "Featured" blogposts

### Other

 * Make this pretty for "public release".
 * RSS feed generator
 * Make optional "table of contents" jump in posts.
 * More themes!
    * Make CSS + Pandoc-template packs
 * Less fragile theming?
 * Code boxes in CSS should scroll when overwidth.
 * Make a "sanity check" test 
 * This codebase is about 300 lines long. Might consider rewriting it from a TDD approach!

