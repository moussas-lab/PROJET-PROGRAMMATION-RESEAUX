import os
import sys
import time
import signal

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

time_exec = int(sys.argv[1])

my_dir = os.path.dirname(sys.argv[0])
os.system('%s %s' % (sys.executable, 
                        os.path.join(my_dir, f'Analyseur_Packet.py {time_exec} > log.txt')))
