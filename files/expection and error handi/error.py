x ={'first':'python','second':'node'}
y= [10,20,30]
try:
  print(x['firstt'])
  print(y[0])
except KeyError :
    print ('key does not exist')
except IndexError :
    print('Index does not exist')

print('hi')