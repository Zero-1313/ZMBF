import sys, os
os.system('git pull')

M = ('\x1b[1;91m')
O = ('\x1b[1;96m')

try:os.system('mkdir OK') 
except:pass 
try:os.system('mkdir CP')
except:pass

if sys.version_info.major != 3:
  exit("\n%s!%s gunakan versi python3 "%(M,O))

if __name__=='__main__':
    try:
        os.system('zero.cpython-310.pyc')
    except Exception as e:
        exit(str(e))
