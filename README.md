# DIY Static Site Generator

A DIY approach to static site generation, using Pandoc.

![Screenshot of a this README, without the screenshot, rendered using this blog.](/images/screenshot.png)

## How to use

1. Put your Markdown posts in `posts/`,
2. run `./build.sh`,
3. and point your HTTP server to `site/`!

### Filestructure

 * `build.sh` -- Renders files in `source/` and puts them in `site/`!
 * `style.css` -- A simple theme for the blog.
 * `source/` -- Edit these files!
    * `header.md` -- Appended to the top of every page
    * `footer.md` -- Appended to the bottom of every page
    * `bodybar.md` -- Placed just before the body of each page
    * `about.md` -- Custom "about" page.
    * `posts/`-- Markdown posts go here!
 * `site/` -- Site is hosted here. (Point your 

## Things this could still use

 * Make this pretty for "public release".
 * Command-line arguments to build.sh (cleanup, style/layout).
 * RSS feed generator
 * Improve `index.html`
   * Parse date, title without `lxml`.
   * Parse date.
   * Index page should organize by category and then by date.
   * Build a by-category page..
 * More themes
   * Make CSS + Pandoc-template packs

## Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.

