import socket


def scan():
    host = input("HOST--->")
    if not host:
        print("Error: must be input")
        raise SystemExit

    try:
        ports = list(map(int, input("PORTS--->").split()))
    except ValueError:
        print("Error: must be integer")
        raise SystemExit

    if not ports:
        print("Error: must be input")
        raise SystemExit

    for some in ports:
        if int(some) > 65535:
            print("Error: port must be 0-65535")
            raise SystemExit

    print("\n")
    print("~" * 50)

    for port in ports:
        try:
            scan = socket.socket()
            scan.settimeout(1)
            scan.connect((host, port))
        except socket.error:
            print("PORT--->", port, "[CLOSED]")
        else:
            print("PORT--->", port, "[OPEN]")
    print("~" * 50)


scan()

#Use it :3
