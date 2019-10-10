import stack
"""charenge1"""
s = stack.Stack()
reverse = ''
for i in 'yesterday':
    s.push(i)
while s.size():
    reverse += s.pop()
print(reverse)

"""charenge2"""
n_reverse = []
nambers = []
for i in range(1, 6):
    nambers.append(i)
for i in nambers:
    s.push(i)
while s.size():
    n_reverse.append(s.pop())
print(n_reverse, nambers)
