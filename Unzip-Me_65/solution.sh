#!/bin/bash

while [ -n "$(ls *.zip)" ]; do
    files=*.zip
    for file in $files; do
        echo "Unzipping $file..."
        unzip -q "$file"
        rm "$file"
    done
done

# Literally just unzip all the files...
# https://www.usenix.org/system/files/conference/3gse14/3gse14-chung.pdf

# flag{efforts_you_have_wasted_young_one}
