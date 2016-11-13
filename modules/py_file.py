'''
import f1
print f1.fun1()
'''''
'''
import f2
print f2.fun2()
def fun3():
	c=f2.a
'''
'''
import f4
print f4.fun2()
print f4.main()
'''
'''
import mod1
print mod1.file1.fun2()
print mod1.file2.fun2()
'''
'''
import sqlite3
print sqlite3.__file__
import mod1
print mod1.__file__
con = sqlite3.connect("db1.db")
'''
import f1
import os
print f1.fun1()
print __file__
print os.getcwd()
print os.path.join(os.getcwd(),__file__)
path = os.path.join(os.getcwd(),"f1.txt")
f=open(path,'w')
f.close()