#!/usr/bin/python3

from ipaddress import ip_address
import nmap

scanner = nmap.PortScanner();

print("Welcome, this is a simple nmap scanner automation tool")
print("<----------------------------------------------------->")

ip_address = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_address)
type(ip_address)
