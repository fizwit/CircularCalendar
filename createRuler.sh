#!/bin/bash


gs -o Ruler.pdf \
 -sDEVICE=pdfwrite \
 -sFONTPATH=/Library/Fonts -dEmbedAllFonts=true \
 -sDEFAULTPAPERSIZE=letter \
-c "[/Author (John Dey)
     /Subject (Solar Lunar Circular Calendar)
     /Keywords (Phase of Moon Sunrise Equonox Calendar)
     /DOCINFO pdfmark" \
 -f Ruler.ps 
