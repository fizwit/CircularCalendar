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

### Lunar Version
An extra ring for Day of Month is added for the Chinese calender. IE, Feb 17, is Chinese New
Year in 2026. Set isLunar to true, and adjust days of month in `LunarMonthlen`.

### Dark Mode
Create the calender with Black background.  Set `ifDark` to `true`.

### Fonts
Helvitica is used for the Year and for the names of Months. Day of month is set with BabelSans.

### Release Nodes

 - 2.1.0 Jan 2026 Add Dark mode. For Dark mode radian lines are much thicker. Increate size of moon 20%
   increate Size of Year in center. Increase font size for `Designed by John Dey`
 - Add gray/white alternating months to Lunar calendar.

### Reference

US Naval Observtory Data
[Navy](https://aa.usno.navy.mil/data/RS_OneYear)

This is good site which had UTC and Los Angles in the same table.

```
https://www.calendar-12.com/moon_phases/2025#google_vignette
https://www.timeanddate.com/moon/phases/?year=2024
```

### PostScript References
[PS Gide](http://materials.ucsd.edu/doc/ps_guide.pdf)
