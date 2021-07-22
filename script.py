from shutil import copyfile
import ntpath, time, os
from datetime import datetime
from datetime import timedelta

class Monkey(object):
    def __init__(this, path):
        this._cached_stamp = 0
        this.filename = path

    def ook(this):
        stamp = os.stat(this.filename).st_mtime
        if stamp != this._cached_stamp:
            this._cached_stamp = stamp 
            this.copy()

    def copy(this):
        dateTimeObj = datetime.now()
        start = time.time()
        src = this.filename 
        dst = 'C:/Users/ragus/Desktop/test/' + dateTimeObj.strftime("%d-%m_%H.%M.%S") + ntpath.basename(this.filename) 
        copyfile(src, dst) 
        end = time.time()
        elapsed = end-start
        print(str(timedelta(seconds=elapsed)))



path = 'C:/Users/ragus/Desktop/x64c.rpf'
object = Monkey(path)

while(True):
    object.ook()

