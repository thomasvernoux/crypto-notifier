

import subprocess
import ipaddress

def change_ip(interface, new_ip, netmask):
    try:
        # Validate the IP address and netmask
        ipaddress.IPv4Address(new_ip)
        ipaddress.IPv4Address(netmask)
    except ipaddress.AddressValueError:
        print("Invalid IP address or netmask.")
        return
    
    try:
        # Run the commands to change the IP address
        subprocess.run(['netsh', 'interface', 'ip', 'set', 'address', interface, 'static', new_ip, netmask])
        print(f"IP address of interface '{interface}' changed to '{new_ip}'")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
interface = 'Wi-Fi'  # Change to your Wi-Fi interface name
new_ip = '192.168.1.100'  # Change to your desired IP address
netmask = '255.255.255.0'  # Change to your netmask
change_ip(interface, new_ip, netmask)
