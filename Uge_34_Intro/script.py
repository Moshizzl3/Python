
k = 'Detteord'


print(k[2:4:])

a = 'abcd'
b = 'xy'


def front_back(a, b):
    front = ""
    back = ""

    front += a[:int(len(a) / 2) + len(a) % 2]
    back += a[int(len(a) / 2) + len(a) % 2:]

    front += b[:int(len(b) / 2) + len(a) % 2]
    back += b[int(len(b) / 2) + len(a) % 2:]

    return front + back


front_back(a, b)
