#!/usr/bin/python3


import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap scanner automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter type of scan you want to run
                 1)SYN ASK Scan
                 2)UDP Scan
                 3)Comprehensive Scan \n""")

print("You have selected the option: ", resp)

if resp == '1':
   print("Nmap Version: ", scanner.nmap_version())
   scanner.scan(ip_addr, '1-1024', '-v -sS')
   print(scanner.scaninfo())
   print("IP Status: ", scanner[ip_addr].state())
   print(scanner[ip_addr].all_protocols())
   print("Open ports: ", scanner[ip_addr]['tcp'].keys())
  

   
 
