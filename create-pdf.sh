#!/bin/bash
#
# Create PDF from PS using GhostScript

if [[ $# -ne 1 ]]; then
        echo Useage: create-pdf inputFile
        exit 1
fi 

gs -sDEVICE=pdfwrite -sFONTPATH=/Library/Fonts -dEmbedAllFonts=true \
        -dDEVICEWIDTHPOINTS=2592 -dDEVICEHEIGHTPOINTS=2592 -o ${1}.pdf ${1}.ps
