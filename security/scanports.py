import socket

import colorama
from colorama import Fore

colorama.init()

def scan():
	host = input("HOST--->")
	if not host:
		print(Fore.RED, "Error: must be input")
		raise SystemExit

	try:
		ports = list(map(int, input("PORTS--->").split()))
	except ValueError:
		print(Fore.RED, "Error: must be integer")
		raise SystemExit

	if not ports:
		print(Fore.RED, "Error: must be input")
		raise SystemExit

	for some in ports:
		if int(some) > 65535:
			print(Fore.RED, "Error: port must be 0-65535")
			raise SystemExit

	print("\n")
	print("~"*50)

	for port in ports:
		try:
			scan = socket.socket()
			scan.settimeout(1)
			scan.connect((host, port))
		except socket.error:
			print(Fore.RED, "PORT--->", port, "[CLOSED]" + Fore.RESET)
		else:
			print(Fore.GREEN, "PORT--->", port, "[OPEN]" + Fore.RESET)
	print("~"*50)

	scan.close()

scan()
