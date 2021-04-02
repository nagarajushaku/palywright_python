# write irregular file in open method it is create automatically file
f= open("sample1.txt",'w')
l =["hai" "","" "welocme ","python ","files"] # list can be written the file,
f.writelines(l)
f.close()