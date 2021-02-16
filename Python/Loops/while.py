#prints out 0,1,2,3,4

count = 0
while count < 5:
	print(count)
	count += 1 

count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break

#print out online odd numbers - 1,3,5,7,9
for x in range(10):
	#check if x is even
	if x % 2 == 0:
		continue
	print(x)

count=0
while(count<5):
	print(count)
	count += 1
else:
	print("Count value reached %d" %(count))

for i in range(1, 10):
	if(i%5==0):
		break
	print(i)
else:
	print("this is not printed because for loop is terminated because of break but not due to fail in condition")