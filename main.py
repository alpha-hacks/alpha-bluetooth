import bluetooth
from alpha_1s import Command


def main():
    msg = message(b'\x18', [b'\x00'])
    print(msg)
    bd_addr = discover()

    if bd_addr:
        port = 6
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((bd_addr, port))
        print('Connected')
        sock.settimeout(60.0)
        sock.send(msg)
        print('Sent data')
        response = sock.recv(1024)
        print(Command().get(response))
        sock.close()


def message(command, parameters):
    header = b'\xFB\xBF'
    end = b'\xED'
    parameter = b''.join(parameters)
    # len(header + length + command +parameters + check)
    length = bytes([len(parameters) + 5])
    data = [command, length]
    data.extend(parameters)
    check = bytes([sum(ord(x) for x in data)])
    return header+length+command+parameter+check+end


def discover():
    print("searching ...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        if name == "ALPHA 1S":
            return addr


if __name__ == '__main__':
    main()
