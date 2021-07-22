from shutil import copyfile
import ntpath, time, os
from datetime import datetime
from datetime import timedelta
import glob

class Monkey(object):
    def __init__(this, path, backup, num_max):
        this._cached_stamp = 0
        this.filename = path
        this.backup = backup
        this.name = ntpath.basename(this.filename)
        this.max = num_max 

    def ook(this):
        stamp = os.stat(this.filename).st_mtime
        if stamp != this._cached_stamp:
            this._cached_stamp = stamp 
            this.copy()
            this.remove_old()

    def copy(this):
        dateTimeObj = datetime.now()
        start = time.time()
        src = this.filename 
        dst = this.backup + dateTimeObj.strftime("%d-%m_%H.%M.%S") + this.name
        copyfile(src, dst) 
        end = time.time()
        elapsed = end-start
        print(str(timedelta(seconds=elapsed)))

    def remove_old(this):
        files = glob.glob(this.backup + "*"+this.name)
        files.sort(key=os.path.getmtime)
        print(files)
        if (len(files) > this.max):
            for i in range (0,len(files)-this.max):
                print(files[i])
                os.remove(files[i])
            

path = 'C:/Users/ragus/Desktop/test.txt'
backup = 'C:/Users/ragus/Desktop/test/'
max = 5
object = Monkey(path, backup, max)

while(True):
    object.ook()
    
