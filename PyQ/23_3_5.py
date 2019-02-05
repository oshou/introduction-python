lst = ['A', 'B', 'C', 'D', 'E']
print(lst[0])
print(lst[-1])
print(lst[1:3])
print(lst[::2])
print(lst[::-1])
print(lst+['F', 'G'])
lst.append('F')
print(lst)
lst[1:4] = 'C'
print(lst)
