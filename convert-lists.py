
# lambda functions
mysum = lambda x, y: (x + y)
convert = lambda l: (l*2.54)
multiply = lambda x: (x*2.5, x*3.5)
cube = lambda b ,c: (b**3, c**3)
cubethree = lambda d, e, f: (d**3, e**3, f**3)
# various more things
thousand = range(1,1000)
someodds = [1, 3, 5, 7, 9, 11, 13, 15, 17]
someevens = [2, 4, 6, 8, 10, 12, 14, 16, 18]
inchlist = [20, 13, 1.0]
cm = [convert(x) for x in inchlist]
numbers = zip (someodds, someevens)


# In to Cm converter
print('inches: ' + str(inchlist[:]))
print('centimeters: ' + str(cm[:]))
# adding lambda
print ('sum of two numbers: ' + str(mysum(12.2, 13.8)))
# multiple outputs?
print ('multiplication: ' + str(multiply(3)))
print ('cube of two numbers: ' + str(cube(3, 4)))
print ('cube of three numbers: ' + str(cubethree(4, 5.8, 3.3)))
# i have to range 0,1001 to get 500500 as an answer
print (sum(thousand[0:]))
# odds and evens
print (list(zip([1, 2, 3], [3, 2, 1])))

