import sys
from src.resolver import Resolver

help = """

Usage:

python main.py [host] [wordlist]

"""

host = sys.argv[1]
wordlist = sys.argv[2]

if host == "" or wordlist == "":
    print(help)
    exit(1)

with open(wordlist) as w:
    for dom in w.readlines():
        dom = f"{dom.strip()}.{host}"
        Resolver.ipv4(dom)
        Resolver.ipv6(dom)
