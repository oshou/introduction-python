s1 = '1234-567 89-00'
s2 = """\
1234
567
89"""
items = ['12', '345', '6789']

print(s1.replace('-', ''))
print(s1.split('-'))
print(s2.splitlines())
print(''.join(items))
