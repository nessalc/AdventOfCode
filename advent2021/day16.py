# day16.py

from functools import reduce
import operator
from typing import TypeGuard


def decode_packet_hex(packet_value: str) -> list[dict]:
    bits = ''
    for c in packet_value:
        bits += f'{int(c,16):04b}'
    return decode_packet(bits)


def decode_packet(bits: str, packet_count: int | None = None) -> list[dict]:
    version: int = int(bits[:3], 2)
    type_id: int = int(bits[3:6], 2)
    packets: list[dict] = []
    offset: int = 0
    if type_id == 4:
        i = 6
        parsing = True
        val: str | int = ''
        while parsing:
            val += bits[i+1:i+5]
            if bits[i] == '0':
                parsing = False
            i += 5
        val = int(val, 2)
        length: int = i
        packets.append({'version': version,
                        'type_id': type_id,
                        'value': val,
                        'length': length})
    else:
        length_type_id: int = int(bits[6])
        if length_type_id == 0:
            length: int = int(bits[7:22], 2)
            subpackets: list[dict] = decode_packet(f'{bits[22:22+length]}')
            subpackets_count: int = len(subpackets)
            packets.append({'version': version,
                            'type_id': type_id,
                            'length_type_id': length_type_id,
                            'subpackets': subpackets_count,
                            'value': subpackets,
                            'length': length+22})
            offset = 22
        else:
            subpackets_count: int = int(bits[7:18], 2)
            subpackets: list[dict] = decode_packet(
                f'{bits[18:]}', subpackets_count)
            length: int = sum(map(lambda x: x['length'], subpackets))
            packets.append({'version': version,
                            'type_id': type_id,
                            'length_type_id': length_type_id,
                            'subpackets': subpackets_count,
                            'value': subpackets,
                            'length': length+18})
            offset = 18
    if (packet_count is not None):
        packet_count -= 1
    if length < len(bits) and '1' in bits[length+offset:] and (packet_count is None or packet_count > 0):
        packets += decode_packet(f'{bits[length+offset:]}', packet_count)
    return packets


def version_sum(packets: list[dict]) -> int:
    total = 0
    for packet in packets:
        total += packet['version']
        if isinstance(packet['value'], list):
            total += version_sum(packet['value'])
    return total


def apply_operations(packet):
    if isinstance(packet, list) and len(packet) == 1:
        return apply_operations(packet[0])
    elif isinstance(packet, dict):
        if 'subpackets' in packet.keys() and packet['subpackets'] != len(packet['value']):
            raise ValueError('Incorrect subpacket count')
        match packet['type_id']:
            case 0:  # sum packet
                return sum(map(apply_operations, packet['value']))
            case 1:  # product packet
                return reduce(operator.mul, map(apply_operations, packet['value']), 1)
            case 2:  # minimum packet
                return min(map(apply_operations, packet['value']))
            case 3:  # maximum packet
                return max(map(apply_operations, packet['value']))
            case 4:  # literal packet
                return packet['value']
            case 5:  # greater than packet
                if packet['subpackets'] != 2:
                    raise ValueError('Incorrect number of subpackets')
                if apply_operations(packet['value'][0]) > apply_operations(packet['value'][1]):
                    return 1
                return 0
            case 6:  # less than packet
                if packet['subpackets'] != 2:
                    raise ValueError('Incorrect number of subpackets')
                if apply_operations(packet['value'][0]) < apply_operations(packet['value'][1]):
                    return 1
                return 0
            case 7:  # equal to packet
                if packet['subpackets'] != 2:
                    raise ValueError('Incorrect number of subpackets')
                if apply_operations(packet['value'][0]) == apply_operations(packet['value'][1]):
                    return 1
                return 0
    elif isinstance(packet, list):
        return [apply_operations[packet] for p in packet]


with open('input16.txt') as fp:
    input_value: str = fp.readline().strip()
    packets: list = decode_packet_hex(input_value)
    print(version_sum(packets))
    print(apply_operations(packets))
