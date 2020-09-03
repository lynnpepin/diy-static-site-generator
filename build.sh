#!/bin/sh

# how to loop over files:
# https://stackoverflow.com/questions/20796200/

for filename in ./posts/*.md; do
    pandoc -s -c style.css $filename -o outputs/$(basename $filename md)html
done
