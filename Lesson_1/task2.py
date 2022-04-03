from ipaddress import ip_address, ip_network
from pprint import pprint

from task1 import host_ping


def host_range_ping(startip, rangeip):

    ipv4 = ip_address(startip)
    SUBNET = ip_network(ipv4)
    list_ipv4 = [ipv4 + x for x in range(rangeip) if SUBNET]
    return host_ping(list_ipv4)


if __name__ == '__main__':
    result = host_range_ping('192.168.1.1', 5)
    pprint(result)