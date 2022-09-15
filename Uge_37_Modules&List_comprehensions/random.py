from re import L
import string

alphabet_string = string.ascii_uppercase

list =[i for i in alphabet_string if i not in [chr(70), chr(75), chr(80), chr(85)]]

print((list))

list =[v for i,v in enumerate(alphabet_string) if v > 'F' and v <'O' and i % 2]
list =[v for v in alphabet_string if v > 'F' and v <'O' and ord(v) % 2]
print(list)

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

lists = [(v,n) for v in colors  for n in sizes]
print(lists)
soled_out = [('Black', 'm'), ('White', 's')]
list = [v for v in ((v,n) for v in colors  for n in sizes) if v not in soled_out]
print(list)
