# The Unix epoch is also known as Unix time or POSIX time or Unix timestamp.
# It is the number of seconds that have elapsed since January 1, 1970, at UTC.
#Code - 
###Today timestamp

import datetime
print(int(datetime.datetime.now().timestamp()))

#### oldtimestamp

from datetime import timezone
dt = datetime(2015, 10, 19)
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print(timestamp)