#!/bin/sh

# how to loop over files:
# https://stackoverflow.com/questions/20796200/

# 1. Create directories and copy over style
mkdir site
mkdir site/posts
cp  style.css site/style.css

# 2. Build header, footer, body preamble, to be put in each document
# header is the top of the document
pandoc -c style.css ./source/header.md   -o ./site/header.html
# bodybar comes right before the body
pandoc -c style.css ./source/bodybar.md  -o ./site/bodybar.html
# footer comes right after the body
pandoc -c style.css ./source/footer.md   -o ./site/footer.html

# 3. Build each post!
# build all the source files
for filename in ./source/posts/*.md; do
    pandoc -c ../style.css -H site/header.html -B site/bodybar.html -A site/footer.html --mathjax $filename -o site/posts/$(basename $filename md)html
done

# 4. Create the index.html file
# generate index.md
python generate_index.py
# build index.html
pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/index.md -o site/index.html

# 5. Build other pages here
# build about, contact, etc.
pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/about.md -o site/about.html

# 6. Cleanup: Remove header.html, bodybar.html, footer.html
rm ./site/header.html
rm ./site/bodybar.html
rm ./site/footer.html
