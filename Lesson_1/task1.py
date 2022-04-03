from ipaddress import ip_address
from subprocess import PIPE, call
from pprint import pprint


def host_ping(hosts):
    ips = {'узел доступен': [], 'узел недоступен': []}
    for host in hosts:
        command = f'ping {ip_address(host)} -c 1'
        return_code = call(command, shell=True, stdout=PIPE)
        ips['узел доступен'].append(host) if return_code == 0 else ips['узел недоступен'].append(host)
    return ips


if __name__ == '__main__':
    hosts = ['127.0.0.1', '192.168.1.100', '8.8.8.8', '213.177.97.1', '213.177.97.201', '98.97.98.97']
    r = host_ping(hosts)
    pprint(r)