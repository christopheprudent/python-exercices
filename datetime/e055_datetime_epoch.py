# web solution
import time
print("Epoch")
print(time.gmtime(0))

print("Temps (%d secondes) depuis epoch" % 36000)
print(time.gmtime(36000))

# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=10, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# 
#     Janvier 1970      
# di lu ma me je ve sa  
#              1  2  3  
#  4  5  6  7  8  9 10  
# 11 12 13 14 15 16 17  
# 18 19 20 21 22 23 24  
# 25 26 27 28 29 30 31 
#
# 1/1/1970 wday=3 (jeudi)
