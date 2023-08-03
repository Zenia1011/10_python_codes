#code to check if the number is palindrome or not
x = int(input("Enter a number: "))

temp = x
reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if x == reverse:
  print('The number IS a Palindrome number')
  
else:
  print("The number IS NOT a palindrome number")

  

  
  