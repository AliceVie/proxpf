# proxpf
A script for forwarding ports in an iptables firewall, designed for use with my single-ip ProxMox setup.

A common issue with running a server with a single public IP address is that virtual machines inside of the host are unable to receive or send traffic. Alongside masquerading and IP forwarding for outbound traffic, inbound traffic needs to be NATed using iptables. This script automates the process of creating these NAT rules. It's very short and sweet, but allows for forwarding traffic based on source ip, as well as protocol ('tcp', 'udp', or 'both')
