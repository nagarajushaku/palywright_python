# program  to read contents of a file 
f= open('/Users/naguraj/Documents/python/sample.txt', 'r') #  here first  value returns the file name and next arg is return the access mode 
a =f.readlines() #this method returns the all file lines 
f.close()
for e in a :
    print(e)

# a return the hi we 