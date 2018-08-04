
def fizz_buzz(num):
	# if the number is div by  both 3 & 5
	if(num%3 ==0 and num%5==0):
		return "FizzBuzz"
	elif(num%3 == 0):
		# if number is divisible by 3 only
			return "Fizz"	
		#if num is divisble by 5 only
	elif(num%5 == 0):
			return "Buzz"	
		#number not divisible by neither 3 nor 5
	else:
			return num
# Call the function
for i in range(1, 100):
    print(fizz_buzz(i))