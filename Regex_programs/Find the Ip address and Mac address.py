import re

txt = '''Ethernet 0 is up, line protocol is up
  Hardware is MCI Ethernet, address is 0000.0c00.750c (bia 0000.0c00.750c)
  Internet address is 131.108.28.8, subnet mask is 255.255.255.0
  MTU 1500 bytes, BW 10000 Kbit, DLY 100000 usec, rely 255/255, load 1/255
  Encapsulation ARPA, loopback not set, keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 4:00:00'''

pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
ip = pattern.findall(txt)
print("ip address", ip[0])

pattern = re.compile(r"[0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}[.][0-9A-Fa-f]{4}")
mac = pattern.findall(txt)
print("mac address", mac[0])