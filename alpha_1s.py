def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


def battery_info(parameters):
    return {'voltage': int.from_bytes(parameters[0:2], byteorder='big'),
            'charge': {0: 'no',
                       1: 'yes',
                       2: 'no battery'}.get(parameters[2]),
            'capacity': parameters[3]}


class Command:
    def __init__(self):
        self.commands = {}
        self.add_command(b'\x18', battery_info)

    def add_command(self, key, function):
        self.commands[int.from_bytes(key, byteorder='big')] = function

    def get(self, data):
        command, parameters = self.alpha_parser(data)
        return self.commands.get(command, lambda x: None)(parameters)

    @staticmethod
    def alpha_parser(message):
        if len(message) < 8:
            return None, None
        print(message)
        header = message[0:2]
        length = message[2]
        command = message[3]
        parameters = message[4:-2]
        check = message[-2]
        end = message[-1]
        checks = all([
             header == b'\xfb\xbf',
             end == 237,
             length == (5 + len(message[4:-2])),
             check == check,  # FIXME check == sum(message[2:-2])
            ])
        if not checks:
            return None, None
        return command, parameters
