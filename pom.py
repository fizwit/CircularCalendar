#!/usr/bin/env python

""" pom.py Phase of Moon

    Compute for the whole calander year
     - Phase of Moon
     - Sunrise SunSet
     - Equinox, Soltice 
    This data is designed to be used by BigCal Postscript Program

Copyright 2016-2021  John Dey

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

"""

__author__ = "John Dey"
__contact__ = "fizwit@gmail.com"
__copyright__ = "Copyright 2015-2021"
__license__ = "GPLv3"
__date__ = "2021/08/26"
__version__ = "1.0.1"

import ephem
import datetime
import sys


days_year = 365    # number of days in a year 365 normal 366 leap
dayArc = 360.0 / float(days_year)
epoc = ephem.Date("2021/01/01")   # Beginning of year
year = '2021'
city = 'Seattle'
#city = 'Los Angeles'

def sun_rise_set(city, year):
    '''
    Calculate sun rise and set for whole year
    '''
    sea = ephem.city(city)
    sea.date = ephem.Date("2020/01/01 12:00:00")
    sun = ephem.Sun()
    earlest_dec = 12.0 
    latest_dec = 12.0 
    longest_len = 8.0
    for day in range(1, days_year + 1 ):
       sunrise = sea.next_rising(sun)
       sunset  = sea.next_setting(sun)
       sol = ephem.localtime(sunrise)
       set = ephem.localtime(sunset)
       rise_dec =  float(sol.hour) + (float(sol.minute)/60.0) + (float(sol.second)/60.0 / 60.0)
       set_dec  =  float(set.hour) + (float(set.minute)/60.0) + (float(set.second)/60.0 / 60.0)
       print("rise_dec: {} set_dec: {}".format(type(rise_dec), type(set_dec)))
       if rise_dec < earlest_dec: 
           earlest_dec = rise_dec
           earlest_sol = sol
           early_day = day
       if set_dec > latest_dec:
           latest_dec = set_dec
           latest_sunset = set
           latest_day = day
       day_length = set_dec - rise_dec
       if day_length > longest_len:
           longest_len = day_length 
           longest_day = sol
           longest_set = set
       print "%d %6.4f %7.4f Sol %%%% Sun Rise/Set: %s %s PST" % (day,
		       rise_dec, set_dec, sol.strftime("%b-%d %H:%M:%S"), set.strftime("%H:%M:%S") )
       sea.date += 1
    sys.stderr.write("Ealest Sun Rise: {}\n".format(earlest_sol.strftime("%b-%d %H:%M:%S") ))
    sys.stderr.write("Longest Day      {} {}\n".format(longest_day.strftime("%b-%d %H:%M:%S"),longest_set.strftime(" %H:%M:%S")))
    sys.stderr.write("Latest Sun Set : {}\n".format(latest_sunset.strftime("%b-%d %H:%M:%S")))

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
sun_rise_set(city, int(year))
print "showpage\n\n%%%%EOF\n"
