import pdb
print "program started"
def fun():
	print "hello world"
	a=10
	b=20
	c=a+b
	return c
a1=100
b1=200
c1=a1+b1
pdb.set_trace()
fun()
for i in [100,200,300]:
	print i
print "program ended"