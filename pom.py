#!/usr/bin/env python

"""
2016.01.30  John Dey
 pom.py Phase of Moon
    Compute for whole calander year
    Phase of Moon
    Sunrise SunSet
    Equinox, Soltice 
"""

import ephem
import datetime


days_year = 365    # number of days in a year 365 normal 366 leap
dayArc = 360.0 / float(days_year)
epoc = ephem.Date("2019/01/01")   # Beginning of year
year = '2019'

def sun_rise_set(year):
    '''
    Calculate sun rise and set for whole year
    '''
    sea = ephem.city('Seattle')
    sea.date = ephem.Date("2017/01/01 12:00:00")
    sun = ephem.Sun()
    for day in range(1, days_year + 1 ):
       sunrise = sea.next_rising(sun)
       sunset  = sea.next_setting(sun)
       sol = ephem.localtime(sunrise)
       set = ephem.localtime(sunset)
       rise_dec =  float(sol.hour) + (float(sol.minute)/60.0) + (float(sol.second)/60.0 / 60.0)
       set_dec  =  float(set.hour) + (float(set.minute)/60.0) + (float(set.second)/60.0 / 60.0)
       print "%d %6.4f %7.4f Sol %%%% Sun Rise/Set: %s %s PST" % (day,
		       rise_dec, set_dec, sol.strftime("%b-%d %H:%M:%S"), set.strftime("%H:%M:%S") )
       sea.date += 1

def get_angle(date):
   round  = ephem.Date( ephem.second * 30 + date)
   angle = (round - epoc )/days_year * 360.0
   parts = round.tuple()
   time_str = "%02d:%02d" % (parts[3], parts[4])
   return (angle, time_str)
   
def sol_print(name, date):
    (angle, time_str) = get_angle(date)
    print "%6.2f (%s %s) event %%%% %sZ" % ( angle, name, time_str, date )

def sol(year):
   '''Soltice and Equinox data
 
      Output format
       77.89 (Spring Equinox 04:30) event %% 2016/3/20 04:30:03Z
   '''
   springEqn = ephem.next_equinox(year)
   summerSol = ephem.next_solstice(year)
   fallEqn = ephem.next_equinox(year + '/6/1')
   winterSol = ephem.next_solstice(year + '/9/1')

   sol_print ("Spring Equinox", springEqn)
   sol_print ("Summer Soltice", summerSol)
   sol_print ("Fall Equinox", fallEqn)
   sol_print ("Winter Soltice", winterSol)

def pom_format(name, date):
    '''
    PostScript Format: 4.11 (Full Moon 04:53) (Full) pom
    PostScript commands:  Full New First Last
    '''
    (angle, time_str) = get_angle(date)
    (cmd, des) = name.split()
    pom_str = "%6.2f (%s %s) (%s) pom %%%% %sZ" % ( angle, name, time_str, cmd, date )
    return pom_str
  
def get_moons_in_year(year, quarter=False):
  '''
  Returns a list of the full and new moons in a year. The list contains tuples
  of either the form (DATE,'full') or the form (DATE,'new')
  Data is truncated at hours and minutes; round to nearest Minute by 
  adding 30 seconds to date
  '''
  moons=[]

  date=ephem.Date(datetime.date(year, 01,01))
  while date.datetime().year==year:
    date=ephem.next_full_moon(date)
    moons.append( pom_format('Full Moon',date) )

  date=ephem.Date(datetime.date(year, 01,01))
  while date.datetime().year==year:
    date=ephem.next_new_moon(date)
    moons.append( pom_format('New Moon', date) )

  if quarter == True:
     date=ephem.Date(datetime.date(year, 01,01))
     while date.datetime().year == year:
       date=ephem.next_first_quarter_moon(date)
       moons.append( pom_format('First Quarter', date) )
   
     date=ephem.Date(datetime.date(year,01,01))
     while date.datetime().year==year:
       date=ephem.next_last_quarter_moon(date)
       moons.append( pom_format('Last Quarter', date) )
   
     moons.sort(key=lambda x: float(x.split()[0]))
  return moons 

sol(year)
pom = get_moons_in_year(int(year), quarter=True)
for phase in pom:
   print phase
sun_rise_set(int(year))
print "showpage\n\n%%%%EOF\n"
