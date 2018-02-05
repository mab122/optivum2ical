optivum2ical
========

**optivum2ical** scrapes a timetable from website generated with [optivum vulcan](//www.vulcan.edu.pl/dla_szkol/optivum/plan_lekcji/Strony/wstep.aspx) and exports it to [iCal format](https://tools.ietf.org/html/rfc5545) for easy use everywhere.

Installation
------------

Install optivum2ical by running:

	git clone git@github.com:mab122/optivum2ical.git	# clone git repo
	cd optivum2ical/
	pip install -r requirements.txt	# install python deps

And run it like this
--------------------

	[mab122@macchiato optivum2ical]$ ./convert.py
	Enter URL with auth info (ex: http://user:password@website.com/path_to/schedule.html):
	http://mab122:secretpassword@myschool.edu/timetables/group01.html

	[mab122@macchiato optivum2ical]$ head schedule.ical
	BEGIN:VCALENDAR
	BEGIN:VEVENT
	SUMMARY:Random lecture Group 01 room 91
	DTSTART;VALUE=DATE-TIME:20180205T085000
	DTEND;VALUE=DATE-TIME:20180205T093500
	RRULE:FREQ=DAILY;INTERVAL=7
	END:VEVENT



What still needs to be done
---------------------------

- Definitely implementing argument parser
- Option to choose recurrence end date
- Also to choose starting date (and default to nearest or last monday relative to now)


Contribute
----------

- Issue Tracker: github.com/optivum2ical/optivum2ical/issues
- Source Code: github.com/optivum2ical/optivum2ical

Support
-------

There is no support. If you are having *issues*, please *issue* a *issue* on github *issue* tracker or [let me know](mailto:me@1CEC0FFEE.black), but I don't promise anything.
