import sys, struct
import xmlrpc.client


def little_endian_to_big_endian(i):
    return struct.pack('>' + 'B' * len(i), *i)


def big_endian_to_little_endian(i):
    for e in i:
        int.as_integer_ratio(e)
        print(type(e), e)
        el = e.to_bytes(4, byteorder='little')
        print(type(el))
        eb = e.to_bytes(4, byteorder='big')
        print("little", el, "big", eb)
        ebl = int.from_bytes(eb, 'big')
        print("be->le", ebl)


if __name__ == '__main__':
    # print(sys.byteorder)
    a = [1, 7, 15, 23, 31]
    # a_len = len(a)
    # s = 'B' * a_len
    # s1 = '>' + s
    # print(a_len)
    # print(s)
    # print(s1)
    print(little_endian_to_big_endian(a))
    print(big_endian_to_little_endian(a))
