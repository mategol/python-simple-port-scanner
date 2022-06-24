import sys 
import socket 

ip_to_scan = input(' IP or domain name to scan: ')     # Input target
if ip_to_scan == '':     # Check if user typed something
    print(' Didn\'t received target IP or domain name. Using default one: scanme.nmap.org')
    ip_to_scan = 'scanme.nmap.org'     # Default target

try: 
    port_range = input('\n Port range to scan (1-65535): ')     # Get the range of ports
    if port_range == '':     # Check if user typed something
        print(' Didn\'t received port range. Using default one: 1-100')
        first_port, last_port = 1, 100     # Default port range
    else:
        first_port, last_port = int(port_range.split('-')[0]), int(port_range.split('-')[1])     # Get usable data (integer port range) from user input

    if first_port > last_port:     # Check if first_port is greater than last_port
        print(' Beginning port is greater than last port. Range is being inverted, to successfully make a scan.\n')
        first_port, last_port = last_port, first_port     # Invert range
    elif first_port == last_port:     # Check if first_port and last_port are equal
        input(' Provided range has 0 ports. Shutting down...\n')
        sys.exit(0)     # Shutdown
    else:
        print('')
    for port in range(first_port, last_port):     # Scanning loop
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        if sck.connect_ex((ip_to_scan, port)) == 0:
            print(' >', port, 'is opened', ' '*20)     # If port is opened, it will be printed
        print(' Scanning', str(port) + '/' + str(last_port), end='\r')     # Progress information
        sck.close()     # Close connection
except: 
    input(' Error occurred. Probably you provided wrong IP or domain name.') 
    sys.exit(0)

print(' '*30)
input(' Press ENTER to shutdown...')

