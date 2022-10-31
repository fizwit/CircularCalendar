#!/usr/bin/env python3

""" pom.py Phase of Moon

    Compute for the whole calander year
     - Phase of Moon
     - Sunrise SunSet
     - Equinox, Soltice
    This data is designed to be used by BigCal Postscript Program

Copyright 2016-2023  John Dey

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
__copyright__ = "Copyright 2015-2023"
__license__ = "GPLv3"
__date__ = "2021/08/26"
__version__ = "1.0.1"

import ephem
import datetime
import sys

year = '2023'
if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
    days_year = 366  # is a leap year
else:
    days_year = 365
dayArc = 360.0 / float(days_year)
epoc = ephem.Date("{}/01/01".format(year))  # Beginning of year
local_zone = ('America/Los_Angeles')
city = 'Seattle'
# city = 'Los Angeles'
"""  US timezone names
Eastern  = USTimeZone(-5, "Eastern",  "EST", "EDT")
Central  = USTimeZone(-6, "Central",  "CST", "CDT")
Mountain = USTimeZone(-7, "Mountain", "MST", "MDT")
Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")
"""
SolEqn = []

def sun_rise_set(city, year):
    '''
    Calculate sun rise and set for whole year
    '''
    sea = ephem.city(city)
    sea.date = ephem.Date("{}/01/01 12:00:00".format(year))
    sun = ephem.Sun()
    earlest_dec = 12.0
    latest_dec = 12.0
    longest_len = 8.0
    for day in range(1, days_year + 1):
        sunrise = sea.next_rising(sun)
        sunset = sea.next_setting(sun)
        sol = ephem.localtime(sunrise)
        set = ephem.localtime(sunset)
        rise_dec = float(sol.hour) + (float(sol.minute)/60.0) + (float(sol.second)/60.0 / 60.0)
        set_dec = float(set.hour) + (float(set.minute)/60.0) + (float(set.second)/60.0 / 60.0)
        if rise_dec < earlest_dec:
            earlest_dec = rise_dec
            earlest_sol = sol
        if set_dec > latest_dec:
            latest_dec = set_dec
            latest_sunset = set
        day_length = set_dec - rise_dec
        if day_length > longest_len:
            longest_len = day_length
            longest_day = sol
            longest_set = set
        if day in SolEqn:
            label = 'SolEqn'  # This day is an Soltice or Equinox
        else:
            label = 'Sol'
        print("{:d} {:6.4f} {:7.4f} {} %% Sun Rise/Set: {} {} PST".format(
              day, rise_dec, set_dec, label, sol.strftime("%b-%d %H:%M:%S"), set.strftime("%H:%M:%S")))
        sea.date += 1
    sys.stderr.write("Ealest Sun Rise: {}\n".format(earlest_sol.strftime("%b-%d %H:%M:%S")))
    sys.stderr.write("Longest Day      {} {}\n".format(longest_day.strftime("%b-%d %H:%M:%S"),
                     longest_set.strftime(" %H:%M:%S")))
    sys.stderr.write("Latest Sun Set : {}\n".format(latest_sunset.strftime("%b-%d %H:%M:%S")))


def get_angle_localtime(ephem_date):
    """convert UTD ephem date to local time
    convert date to angle
    """
    local = ephem.localtime(ephem_date)
    dayofyear = local.timetuple()[7]
    time_str = "{:02d}:{:02d}".format(local.hour, local.minute)
    angle = float(local.timetuple().tm_yday - 1) / float(days_year) * 360.0
    angle += float(local.hour * 60 + local.minute) / 1440.0
    return (angle, time_str, local.ctime(), dayofyear)


def sol(year):
    """Soltice and Equinox data
       Output format
       77.89 (Spring Equinox 04:30) event %% 2016/3/20 04:30:03Z
    """
    events = [('Spring Equinox', ephem.next_equinox(year)),
              ('Summer Soltice', ephem.next_solstice(year)),
              ('Fall Equinox', ephem.next_equinox(year + '/6/1')),
              ('Winter Soltice', ephem.next_solstice(year + '/9/1')),
    ]

    for day in events:
        (angle, time_str, local, dayofyear) = get_angle_localtime(day[1])
        print("{:6.2f} ({} {}) event %% {} ".format(angle, day[0], time_str, local))
        SolEqn.append(dayofyear)


def pom_format(name, date):
    """
    PostScript Format: 4.11 (Full Moon 04:53) (Full) pom
    PostScript commands:  Full New First Last
    """
    (angle, time_str, local, dayofyear) = get_angle_localtime(date)
    (cmd, des) = name.split()
    pom_str = "{:6.2f} ({} {}) ({}) pom %% {}Z".format(angle, name, time_str, cmd, local)
    return pom_str

def interpolate_cresent_moon(moons):
    """ ephem only reports 4 phases of the moon, I want eight 
    Add Cresent and Gibbos moons between quarters based on angle
    """
    newMoons = []
    phases = ['New', 'First', 'Full', 'Last']
    newPhases = ['WaxingCrescent', 'WaxingGibbous', 'WaningGibbous', 'WaningCrescent']

    last = False 
    for phase in moons:
        fields = phase[1].split()
        angle = float(fields[0])
        if last:
            diff = angle - lastAngle
            if diff < 0:
                diff = 360 + diff
            newAngle = lastAngle + (diff / 2.0)
            if newAngle > 360.0:
                newAngle = newAngle - 360.0
            pom_str = "{:6.2f} ({}) ({}) pom %% ".format(newAngle, newPhases[newP], newPhases[newP])
            newMoons.append(lastr)
            newMoons.append(pom_str)
        else:
            last = True
        lastr = phase[1]
        lastAngle = angle 
        if fields[1].strip('(') in phases:
            newP = phases.index(fields[1].strip('('))
        else:
            print('Error what phase of the moon is this: {}'.format(fields[1]))
            sys.exit()
    newMoons.append(phase[1])
    return newMoons

def get_moons_in_year(year):
    """
    Returns a list of the full and new moons in a year. The list contains tuples
    of either the form (DATE,'full') or the form (DATE,'new')
    Data is truncated at hours and minutes; round to nearest Minute by
    adding 30 seconds to date
    """
    moons = []

    start = ephem.Date(datetime.date(year-1, 12, 12))
    end = ephem.Date(datetime.datetime(year+1, 1, 12))
    date = start
    while date < end: 
        date = ephem.next_full_moon(date)
        if date < end:
            moons.append([date, pom_format('Full Moon', date)]) # list of tuple

    date = start
    while date < end: 
        date = ephem.next_new_moon(date)
        if date < end:
            moons.append([date, pom_format('New Moon', date)])

    date = start
    while date < end:
        date = ephem.next_first_quarter_moon(date)
        if date < end:
            moons.append([date, pom_format('First Quarter', date)])

    date = start 
    while date < end:
        date = ephem.next_last_quarter_moon(date)
        if date < end:
            moons.append([date, pom_format('Last Quarter', date)])

    moons.sort(key=lambda x: x[0])
    return moons


sol(year)
pom = get_moons_in_year(int(year))
MoonPhases = interpolate_cresent_moon(pom)
for phase in MoonPhases:
    print(phase)
sun_rise_set(city, int(year))
print("showpage\n\n%%EOF\n")
