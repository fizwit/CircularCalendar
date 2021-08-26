# Circular Calendar 

Circular Calendar is an annual calendar that prints at a size of 36 inches square. The calendar is circular with the months arranged on the outside edge with the New Year at the Noon position. The radian lines in the center of the calendar indicate sunrise and sunset for each day. The sunrise sunset times are drawn at half scale and can be read with architect scale. Half inch equals one hour. To read Sunrise time, place the zero of an Architects scale on the innermost circle. Sunrise is the outer edge of the radian, and sunset is the end of the radian line. The sunset sunrise times are to read from the half-scale rule.  Four and a half on the scale is equivalent to 4:30AM.

An 18" Architect scale is needed to read sunset times for the longest days, which are past 22:00 hours during the days of summer. 
Full and new moon are displayed. The Chinese (Lunar) version aligns with the Lunar cycle of the new moon. New Moon times are GST which is why they do not perfectly align with the Lunar calendar.
The lunar feature is a single PS object.

### How to convert ps to pdf
To render from source Ghostscript is required.  Use ps2pdf command.
Ghostscript 9.05 is currently being used.

```
gs -sDEVICE=pdfwrite -sFONTPATH=/Library/Fonts -dEmbedAllFonts=true \
  -dDEVICEWIDTHPOINTS=2592 -dDEVICEHEIGHTPOINTS=2592 -o BigCal-2019.pdf  BigCal-2019.ps
```

### How to generate Solar and Luna Events
pom.py generates the phase of moon and solar sunrise sunset data.  The ouput
from pom.py is added to the bottom of the Postscript files.  The data is generated
for Seattle. To localize the calander the city information can be changed in
pom.py

### Fonts
Helvitica is used for the Year and for the names of Months. Day of month is set with BabelSans.
