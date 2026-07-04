import socket


class Resolver:
    @staticmethod
    def ipv6(dom: str):
        try:
            res = socket.getaddrinfo(dom, None, socket.AF_INET6)
            print(f"{dom}\t\tIPV6 - {res[2][4][0]}")
        except socket.gaierror:
            None

    @staticmethod
    def ipv4(dom: str):
        try:
            res = socket.getaddrinfo(dom, None, socket.AF_INET)
            print(f"{dom}\t\tIPV4 - {res[2][4][0]}")
        except socket.gaierror:
            None
