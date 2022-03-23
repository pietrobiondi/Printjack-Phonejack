import subprocess
import random
import time
import threading
from multiprocessing import Pool
import nmap 
import sys
import os


 	

if __name__ == "__main__":
	 	subprocess.Popen(['tcpreplay', '--intf1=enp0s3','--loop=50000','list/newSipInvite'+str(2)+'_'+str(2)+'.pcap'])
	 	subprocess.Popen(['tcpreplay', '--intf1=enp0s3','--loop=50000','list/newSipInvite'+str(3)+'_'+str(1)+'.pcap'])
	 		


