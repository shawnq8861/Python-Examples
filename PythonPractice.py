"""
Practice from Chapter 12, 13

"""

if 1:
    print('hello')
    
x = 'spam'
while x:
    print x,
    x = x[:-1]

print '\n'
    
a = 0
b = 10
while a < b:
    print a,
    a += 1
    
def funct1():
    pass

print '\n'

x = 10
while x:
    x -= 1
    if x % 2 != 0: continue
    print x,

print '\n'

x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print x,
        
x = 0
while x < 100:
    print x
    x +=5
    if x == 30:
        break
    
y = 0
for x in [1, 2, 3, 4]:
    y += x
print 'sum = ' + str(y)
 
for x in ['first', 'second', 'third']:
    for y in [1, 2, 3, 4, 5]:
        print x, '   ', y
        
for i in range(5):
    print 'i = ', i
    
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
print L

def AddNum(x = 1, y = 2):
    return x + y

print '2 + 7 = ', AddNum(2, 7)

OtherName = AddNum

print 'calling by new name...'
print '5 + 11 = ', OtherName(5, 11)

print AddNum( 'char ', str(4))

def times(x, y):
    return x * y

print '3 * 5 = ', times(3, 5)
print '\'a\' * 4 = ', times('a', 4)

def intersect(seq1, seq2):
    res = []                # Start empty
    for x in seq1:          # Scan seq1
        if x in seq2:       # Common item?
            res.append(x)   # Add to end
    return res

print intersect([1, 2, 3, 4], [2, 3, 5, 6, 7])

st1 = 'shawn'
st2 = 'spam'
print 'intersection of ', st1, ' and ', st2, ' is ', intersect(st1, st2)
