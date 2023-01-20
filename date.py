import time
# Jan 1 1970 12:00 AM
tm = time.time()
local = time.localtime(tm)

tm2 = time.asctime(local)

print(tm2)
