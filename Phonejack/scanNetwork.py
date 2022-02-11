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
