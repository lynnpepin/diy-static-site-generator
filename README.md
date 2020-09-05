# Static Site Generator in 10 Minutes

A do-it-yourself approach to static site generation, using Pandoc.

Write posts in markdown in `./source/posts/` and run the build script.

## Goals

 * Add footer, header, and `<aside>` sidebar
 * Cheat and do that with PHP instead!
 * Generate an "index.html" page automatically
    * Index page should organize by category and then by date
    * List most recent 10 posts
 * Render Math in a pretty manner
 * ToC to link to headers; add hoverover to said links.

## Questions

### It's not DIY if you use Pandoc!

True! In fact, this would take much more than 10 Minutes if we didn't use Pandoc. This is many layers of abstraction lower than using something like Jekyll or Hugo though.

### Why do you use Python and not Bash?

Because I like Python! It's easier for me to extend Python!

That said, I actually haven't used Python here yet, sooo.... ;)

### But you call Pandoc from Python!

Yeah! It's easier that way!

### Gross!

Sorry (but not really.)
