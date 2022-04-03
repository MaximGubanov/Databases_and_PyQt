from tabulate import tabulate
from task2 import host_range_ping


def tabulated_list_ip():
    host_list = host_range_ping('87.250.250.230', 10)
    return tabulate(host_list, headers='keys', tablefmt='pipe', stralign='center')


if __name__ == '__main__':
    print('Pinging of range...')
    table = tabulated_list_ip()
    print(table)