from scapy.all import *
from netfilterqueue import NetfilterQueue
from cryptography.fernet import Fernet
import socket


def encrypt(packet):
 cipher_suite = Fernet(key)
 enc_vc=cipher_suite.encrypt(packet.get_payload())
 pkt = IP(packet.get_payload())
 MESSAGE = enc_vc
 sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 sk.sendto(MESSAGE, (pkt[IP].dst, pkt[UDP].dport))
 packet.drop()
 
nfqueueenc = NetfilterQueue()
nfqueueenc.bind(2, encrypt)


def decrypt(packet):
 cipher_suite = Fernet(key)
 dec_vc=cipher_suite.decrypt(packet.get_payload())
 pkt = IP(packet.get_payload())
 MESSAGE = dec_vc
 sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
 sk.sendto(MESSAGE,(pkt[IP].dst, pkt[UDP].dport))
 packet.drop()
 
nfqueuedec = NetfilterQueue()
nfqueuedec.bind(3, decrypt)
