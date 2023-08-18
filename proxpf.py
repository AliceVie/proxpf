#!/root/proxpf/bin/python

import yaml
import os

def flush_iptables():
    os.system('iptables -t nat -F PREROUTING')

def apply_rules(rules):
    for rule in rules:
        source_ip = rule['source'].split(':')[0]
        source_port = rule['source'].split(':')[1]
        dest_ip = rule['dest'].split(':')[0]
        dest_port = rule['dest'].split(':')[1]
        protocol = rule['type']

        if (protocol == 'tcp' or protocol == 'both'):
            if (source_ip == '0.0.0.0'):
                os.system('iptables -t nat -A PREROUTING -p tcp --dport ' + source_port + ' -j DNAT --to ' + dest_ip + ':' + dest_port)
            else:
                os.system('iptables -t nat -A PREROUTING -p tcp -s ' + source_ip + ' --dport ' + source_port + ' -j DNAT --to ' + dest_ip + ':' + dest_port)
        if (protocol == 'udp' or protocol == 'both'):
            if (source_ip == '0.0.0.0'):
                os.system('iptables -t nat -A PREROUTING -p udp --dport ' + source_port + ' -j DNAT --to ' + dest_ip + ':' + dest_port)
            else:
                os.system('iptables -t nat -A PREROUTING -p udp -s ' + source_ip + ' --dport ' + source_port + ' -j DNAT --to ' + dest_ip + ':' + dest_port)

def main():
    rules = []

    with open('./portdef.yml', 'r') as f:
        rules = yaml.safe_load(f)['rules']

    flush_iptables()
    apply_rules(rules)

if __name__ == "__main__":
    main()
