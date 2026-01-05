# Release Notes

### 2026 Jan Dark Mode

Version 2.1.0
  - fix spelling of Release.md
  - Add versioin to PomCal `/version`
  - Add Dark Mode, carving the elements from black makes everything smaller. Increase
    size of almost everything.
  - Draw Black square over the whole paper first, then carve out with white.
  - Increase size of, Year, Desgined by, Moon Phases, Radian Lines.
  - Increase size of Seattle from 94 too 135  (43.5 % bigger) 
  - Create White band for Day of Week, and Day of Month. Black text for Day of Week is the 
    same for Normal and Dark mode. Keep black/white for Day of Week.
  - Remove `leftedge` it should have been rightedge, The rightedge is really `paperWidth`
  - ToDo - the tick mark for the POM intrudes into the outer band by about a half point

### 2022 Dec 21 Redesign

Added new function call to pom.py `SolEqn`.  **SolEqn** is identical to Sol, for drawing
the Sun Rise/Sun Set lines. But is rendered as a full Pt in thickness to mark the Soltice and
Equinox. Remove all astro events as they appeared as lines inside the Calander.


Move Moon's to outside and more than double the size of each Moon. Add small tick mark to 
indicate POM, but with no data. First time all times are local to Seattle.

BigCal will break with **SolEqn** data.  2022.data was used to generate BigCal before
data type was introduced.

New postscript file PomCal.ps for 2022 redesign does not support Lunar. Add Lunar to outside?
Redefined how radian lines, rad1,2,3 are used.  How to add Lunar?
Should fix line thickness between days. clean up line thickness errors. Are all white
lines thick?

Fix white line between Saturday and Sunday when happens between last day of year and
first day of year.  13th Month added to monthlen to allow checking the very last day
of the  year.

TODO add cresent shape to POM. 

Smaller POM created for testing on letter size paper.
