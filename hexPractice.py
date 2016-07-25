num = 48
print num
hexNum = hex(num)
print hexNum
num += 11
print num
hexNum = hex(num)
print hexNum
dec = int(hexNum, 16)
print dec
hexNum = 0x0C
print hexNum
print "example calculation:"
a = 48
b = 12
print "a = "
print a
print "b = "
print b
c = a - b
print "c = "
print c
print "hex equivalent of a = "
print hex(a)
print "hex equivalent of b = "
print hex(b)
print "hex equivalent of a - b = "
d = hex(c)
print d
prefix, value = d.split('x')
print prefix
print value
e = int(value)
print e
f = 13
print e + f
