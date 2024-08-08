Example 1: Using os module
import os.path, time

file = pathlib.Path('abc.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))

==>Output: 
Last modification time: Mon Apr 12 10:43:24 2020
Last metadata change time or path creation time: Mon Apr 12 10:43:24 2020



Example 2: Using stat() method
import datetime
import pathlib

fname = pathlib.Path('abc.py')
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))

==>Output: 
Last modification time: 2021-04-12 10:43:24.234189
Last metadata change time or path creation time: 2021-04-12 10:43:24.234189
