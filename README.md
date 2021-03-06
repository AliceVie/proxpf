# proxpf
A script for forwarding ports in an iptables firewall, designed for use with my single-ip ProxMox setup.

## Why?
I recently have transitioned from an in-home homelab with plentiful access to IP addresses from my router, to a single public-facing IP address on a bare metal hosted server. This change has required some networking changes, including using my Proxmox VE install as the router for my virtual machines. This script exists to read a simple yaml file that defines which ports to forward, and to where, and applies the rules to the PREROUTING chain in iptables.

## What does it do?
Using a yaml file to define source and destination attributes, this script will clear out the PREROUTING on your iptables nat table and apply DNAT rules using the data provided in the yaml file. This specifically is useful for something like the single-ip Proxmox VE setup mentioned above.