import sys 
import socket 

ip_to_scan = input(' IP or domain name to scan: ')
if ip_to_scan == '':
    print(' Didn\'t received target IP or domain name. Using default one: scanme.nmap.org')
    ip_to_scan = 'scanme.nmap.org'

try: 
    port_range = input('\n Port range to scan (1-65535): ')
    if port_range == '':
        print(' Didn\'t received port range. Using default one: 1-100')
        first_port, last_port = 1, 100
    else:
        first_port, last_port = int(port_range.split('-')[0]), int(port_range.split('-')[1])

    if first_port > last_port:
        print(' Beginning port is greater than last port. Range is being inverted, to successfully make a scan.\n')
        first_port, last_port = last_port, first_port
    elif first_port == last_port:
        input(' Provided range has 0 ports. Shutting down...\n')
        sys.exit(0)
    else:
        print('')
    for port in range(first_port, last_port):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        if sck.connect_ex((ip_to_scan, port)) == 0:
            print(' >', port, 'is opened', ' '*20)
        print(' Scanning', str(port) + '/' + str(last_port), end='\r')
        sck.close()
except: 
    input(' Error occurred. Probably you provided wrong IP or domain name.') 
    sys.exit(0)

print(' '*30)
input(' Press ENTER to shutdown...')

