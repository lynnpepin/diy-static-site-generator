# Static Site Generator in 10 Minutes

A do-it-yourself approach to static site generation, using Pandoc.

Write posts in markdown in `./source/posts/` and run the build script.

## Goals

 * Generate an "index.html" page automatically
    * Index page should organize by category and then by date
    * List most recent 10 posts
 * Clean up CSS style
 * Render Math in a pretty manner
 * Make a new Pandoc template
 * Make a small assortment of Pandoc templates and CSS themes.

## Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.

## Questions

### It's not DIY if you use Pandoc!

True! In fact, this would take much more than 10 Minutes if we didn't use Pandoc. This is many layers of abstraction lower than using something like Jekyll or Hugo though.

### Why do you use Python and not Bash or Perl or my favorite scripting language?

Because I like Python! It's easier for me to extend Python!
