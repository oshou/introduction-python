print("'...'.splitlines()", """\
Alice
Bob
Carol""".splitlines())

print("'abcd'.replace('bc','-'):", 'abcd'.replace('bc', '-'))
print("'1 2 3'.split():", '1 2 3'.split())
print("'1<>2<><><3'.split('<>'):", '1<>2<><><3'.split('<>'))
print("'--abc--'.strip():", '--abc--'.strip('-'))
print("'--abc--'.rstrip():", '--abc--'.rstrip('-'))
print("'--abc--'.lstrip():", '--abc--'.lstrip('-'))
print("'-'.join('1 2 3'.split()):", '-'.join('1 2 3'.split()))
