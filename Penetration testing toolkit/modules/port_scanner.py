import socket


def scan_ports(target):

    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306]

    open_ports = []

    for port in ports:

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        except:
            pass

    return {
        'target': target,
        'open_ports': open_ports
    }