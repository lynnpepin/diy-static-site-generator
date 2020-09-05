#!/bin/sh

# how to loop over files:
# https://stackoverflow.com/questions/20796200/

mkdir site
mkdir site/posts
cp style.css site/style.css

# build all the source files
for filename in ./source/posts/*.md; do
    pandoc -s -c ../style.css $filename -o site/posts/$(basename $filename md)html
done

# build index.md
python generate_index.py

# build index.html
pandoc -s -c style.css ./source/index.md -o site/index.html
