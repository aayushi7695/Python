import math
import sys
import datetime

print('Twinkle, twinkle, litle star,\n \t How I wonder what you are! \n\t\tUp above the world so high, \n \t \tLike a '
      'diamond in the sky.\n Twinkle, twinkle, little star,\n \t How I wonder what you are')

x = float(input('Enter Radius'))
area = math.pi * x * x
print(area)

print('Version=', sys.version)
print('Version info=', sys.version_info)

print(datetime.datetime.now())
