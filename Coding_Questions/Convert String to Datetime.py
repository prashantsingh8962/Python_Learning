Example 1: Using datetime module
from datetime import datetime

my_date_string = "Mar 11 2011 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)

==>Output:
<class 'datetime.datetime'>
2011-03-11 11:31:00


Example 2: Using dateutil module
from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))

==>Output:
2011-03-11 11:31:00
<class 'datetime.datetime'>
