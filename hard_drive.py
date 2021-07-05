import shutil, time
from datetime import datetime

sleep_secs = 60 * 60 # 1 hour
while True:
  total, used, free = shutil.disk_usage("/")
  print(f"{str(datetime.utcnow()).split('.')[0]} | Used: {used // (2**30)} GiB" )
  time.sleep(sleep_secs)
