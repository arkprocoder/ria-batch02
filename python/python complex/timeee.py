import time,datetime
print(time.time())
print(time.asctime())
# time.sleep(5)
print("i am python")
x = datetime.datetime.now()
print(x)
print(x.date())
print(x.time())
print(x.second)
print(x.year)
print(x.month)
print(x.microsecond)
print(x.minute)
print(x.day)
print(x.strftime("%B"))
print(x.strftime("%A"))

y = datetime.datetime(2020, 5, 17)
print(y)

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
print(x.strftime("%A"))


# seconds passed since epoch
seconds = time.time()

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)
result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_minutes:", result.tm_min)




named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)