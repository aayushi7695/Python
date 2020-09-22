import calendar
import datetime

color_list = ['Red', 'Green', 'White', 'Black']
print(color_list[0] + ',' + color_list[3])

exam_st_date = (11, 12, 2014)
print("The examination will start from", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])

n = int(input("enter a value"))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print(n1 + n2 + n3)

y = int(input("Enter year"))
m = int(input("Enter month"))
print(calendar.month(y, m))

print(datetime.date.day)