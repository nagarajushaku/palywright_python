# program  to read contents of a file 
f= open('/Users/naguraj/Documents/python/sample.txt', 'r') #  here first  value returns the file name and next arg is return the access mode 
a =f.readline() #read the enitre line 
f.close()
print(a)
# a return the hi we 