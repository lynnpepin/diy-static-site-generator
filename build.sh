#!/bin/sh

# how to loop over files:
# https://stackoverflow.com/questions/20796200/

mkdir site
mkdir site/posts
cp style.css site/style.css

# header is the top of the document
pandoc -c style.css ./source/header.md   -o ./site/header.html
# bodybar comes right before the body
pandoc -c style.css ./source/bodybar.md  -o ./site/bodybar.html
# footer comes right after the body
pandoc -c style.css ./source/footer.md   -o ./site/footer.html

# build all the source files
for filename in ./source/posts/*.md; do
    pandoc -c ../style.css -H site/header.html -B site/bodybar.html -A site/footer.html --mathjax $filename -o site/posts/$(basename $filename md)html
done

# build index.md
python generate_index.py

# build index.html
pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/index.md -o site/index.html

# build about, contact, etc.
pandoc -s -c style.css -H site/header.html -B site/bodybar.html -A site/footer.html ./source/about.md -o site/about.html
