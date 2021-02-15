name = "John"
age = 23
if name == "John" and age == 23:
	print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
	print("Your name is either John or Rick.")


if name in ["John", "Rick"]:
	print("your name is either John and Rick")

#........

statement = False
another_statement = True
if statement is True:
	# do something
	pass
elif another_statement is True: #else if
	#do something else
	pass
else:
	#do another thing
	pass

#........

x = 2
if x == 2:
	print("x equals two!")
else:
	print("x does not equal to two.")

#........

r = [1,2,3]
w = [1,2,3]
print(r == w) #print true
print(r is w) #print false

#........

print(not False)
print((not False) == (False))