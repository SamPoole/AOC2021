from utils import read_file

input_string = read_file(16)[0]


def decode_hexadecimal(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    if len(binary_string) < 4 * len(hex_string):
        binary_string = '0' * (4 * len(hex_string) - len(binary_string)) + binary_string
    return binary_string


def parse_binary(binary_string):
    packet_version = int(binary_string[:3], 2)
    packet_type = int(binary_string[3:6], 2)
    number_of_sub_bits = int(((len(binary_string) - 6) - (len(binary_string) - 6) % 5) / 5)
    sub_bits = [binary_string[7 + 5 * i:11 + 5 * i] for i in range(number_of_sub_bits)]
    # extra_end = binary_string[-((len(binary_string) - 6) % 5):]

    return packet_version, packet_type, sub_bits


class Packet:
    def __init__(self, binary_string):
        self.packet_version = int(binary_string[:3], 2)
        self.packet_type = int(binary_string[3:6], 2)
        self.length_type_id = None
        self.sub_packet_string = None
        self.sub_packets = []
        self.parse_message(self.packet_type, binary_string[6:])

    def debug(self):
        return self.packet_version, self.packet_type, self.length_type_id, self.sub_packets

    def parse_message(self, packet_type, message_string):
        if packet_type == 4:
            sub_packet_count = int((len(message_string) - len(message_string) % 5) / 5)
            self.sub_packets = [message_string[1 + 5 * i:5 + 5 * i] for i in range(sub_packet_count)]
        else:
            self.length_type_id = int(message_string[0])
            if self.length_type_id == 0:
                total_length_of_bits = int(message_string[1:16], 2)
                self.sub_packet_string = message_string[16:16+total_length_of_bits]
            else:
                total_number_of_bits = int(message_string[1:12], 2)
                self.sub_packet_string
            # self.sub_packets = [message_string[13 + 5 * i:5 + 5 * i] for i in range(self.sub_packet_count)]

        print(self.debug())


a = Packet(decode_hexadecimal('D2FE28'))
b = Packet(decode_hexadecimal('38006F45291200'))
c = Packet(decode_hexadecimal('EE00D40C823060'))
d = Packet(decode_hexadecimal('8A004A801A8002F478'))
e = Packet(decode_hexadecimal('620080001611562C8802118E34'))
f = Packet(decode_hexadecimal('C0015000016115A2E0802F182340'))
g = Packet(decode_hexadecimal('A0016C880162017C3686B18A3D4780'))
