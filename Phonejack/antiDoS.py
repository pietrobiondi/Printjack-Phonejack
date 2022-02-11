from scapy.all import *
from netfilterqueue import NetfilterQueue
import socket

def antiDos(packet):
  pkt = IP(packet.get_payload())
  Flag=0
 with open('blacklist.txt') as f:
  if str(packet.get_payload()) in f.read():
  Flag=1
  if Flag == 1:
   packet.drop()
  else:
   packet.accept()
   f= open("blacklist.txt","a+")
   f.write(str(packet.get_payload()))
   f.close()
   Flag=0
nfqueue = NetfilterQueue()
nfqueue.bind(1, antiDos)
