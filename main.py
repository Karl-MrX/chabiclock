import time
import datetime
from datetime import datetime
now = datetime.now()

seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
seconds_since_midnight = seconds_since_midnight+3600

chabitime=seconds_since_midnight/8640
chabitime=int(chabitime*10000)
chabitime=chabitime/10000
print("chabis", chabitime)
while True:
  time.sleep(0.864)
  
  
  chabitime=round(chabitime, 4)
  chabitime=chabitime+0.0001
  chabitime=round(chabitime, 4)
  print("chabis", chabitime)
