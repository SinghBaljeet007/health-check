import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free>20
	
if not check_disk_usage("/"):
    print("ERROR!")
else:
    print("Everything is OK!")