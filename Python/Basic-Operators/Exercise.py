#The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d object" % len(x_list))
print("x_list contains %d object" % len(y_list))
print("big_list contains %d object" % len(big_list))

#testin
if x_list.count(x) == 10 and y_list.count == 10:
	print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")