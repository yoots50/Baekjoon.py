from time import gmtime, time
t = gmtime(time())
print(f"{t.tm_year}-{t.tm_mon}-{t.tm_mday}")