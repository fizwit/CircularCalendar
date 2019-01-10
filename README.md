# Big Calendar

Big Calendar is an anual calander that prints  36 inche square. The
calendar is circular.  The new year starts at the 12 Noon position.
The months are aranged in a circle on the outside edge.

In the center of the calander radian lines indecate the length of each
day.  The Lines are drawn in half inch scale. Half Inch equals one hour.
The Sunrise and Sunset for each day can be read by placing the 
Zero of an Archetects ruler on the inner most circle. An 18" Architect 
scale is needed to read sunset times which are past 22:00 hours during 
the longest days of summer. Sunrise will apear where it should at around 
4" to 6" inches which can be directly converted to hours and minutes.

Full and new moon are displayed for the whole years. The Chinese version
was created because the months align with the Lunar cycle. New Moon times
are GST which is why they do not perfectly align with the Chinese calander.


### How to convert ps to pdf
To render from source Ghostscript is required.  Use ps2pdf command.
Ghostscript 9.05 is currently being used.

ps2pdf -dDEVICEWIDTHPOINTS=2592 -dDEVICEHEIGHTPOINTS=2592 Chinese-2019.ps output.pdf


### How to generate Solar and Luna Events
pom.py generates the phase of moon and solar sunrise sunset data.  The ouput
from pom.py is added to the bottom of the Postscript files.  The data is generated
for Seattle. To localize the calander the city information can be changed in
pom.py
