import time
print(time.asctime())
import datetime
print(time.asctime(time.localtime(time.time())))
datetime_object = datetime.datetime.now()
print(datetime_object)
print("year:", datetime_object.year)
print("month:", datetime_object.month)
print("date:", datetime_object.date)
print("hour:", datetime_object.hour)
print("minute:", datetime_object.minute)
import calendar
s = calendar.prcal(2022)
print(s)
count=5
def some():
    global count
    count=count+1
    local=10
    print(count)
    print(local)
some()