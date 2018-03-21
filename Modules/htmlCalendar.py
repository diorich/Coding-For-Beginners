import calendar

cal=open("cal.html","w")
c=calendar.HTMLCalendar(calendar.MONDAY)
cal.write(c.formatmonth(2018,1))
cal.close()

