# Static Site Generator in 10 Minutes

A DIY approach to static site generation, using Pandoc.

Write posts in markdown in `./source/posts/` and run the build script.

## TODOs

 * Make proper 'absolute' URL linkage
 * Proper metadata on every page, including index, about, etc.
 * Rename project -- maybe '1000 minutes'? :)
 * Style 'About', etc. in CSS (not inline source.)
 * Style title properly, not as id `lynns-cool-blog`.
 * Parse args in bash (e.g. 'delete helper html files', etc.)

### Longer-term goals

 * Move entire build either to Python or to Bash.
 * Introduce RSS feed generator
 * Themes, combining CSS and Pandoc templates.
   * Considering [Google Fonts](https://fonts.google.com/attribution) -- add script to download and self-host?
 * Make use of Pandoc's "filters" feature.
 * Improve `index.html`
   * Index page should organize by category and then by date
   * List most recent 10 posts
 * Make a "version 1.0" release :)
 * Make appropriate "defaults" for release (and not just as my personal blog!)

## Requirements

 * **Pandoc** is used to convert markdown files to HTML.
 * **Python 3.6** or greater is used. (f-strings were introduced in 3.6.)
 * Python package **lxml** is used to read titles when generating index.html.

## Questions

### It's not DIY if you use Pandoc!

True! Pandoc is most of the work! This is many layers of abstraction lower than using something like Jekyll or Hugo though.

### Why do you use Python? Why not entirely Bash?

Because I like Python! It's easier for me to extend Python because I already know it.
