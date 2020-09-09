# Static Site Generator in 10 Minutes

A DIY approach to static site generation, using Pandoc.

Write posts in markdown in `./source/posts/` and run the build script.

## Goals

 * Generate an "index.html" page automatically
    * Index page should organize by category and then by date
    * List most recent 10 posts
 * Clean up CSS style
 * Proper metadata on every page, including index, about, etc.
 * Subpages -- contact, about, etc.
 * Rename project -- maybe '1000 minutes'? :)

### Longer-term goals

 * Move entire build either to Python or to Bash.
 * Introduce RSS feed generator
 * Themes, combining CSS and Pandoc templates.
 * Make use of Pandoc's "filters" feature.

## Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.

## Questions

### It's not DIY if you use Pandoc!

True! In fact, this would take much more than 10 Minutes if we didn't use Pandoc. This is many layers of abstraction lower than using something like Jekyll or Hugo though.

### Why do you use Python and not Bash or Perl or my favorite scripting language?

Because I like Python! It's easier for me to extend Python!
