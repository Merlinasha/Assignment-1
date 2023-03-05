#Fibonacci series between 0 to 50

num1 = 1
num2 = 1
print("Fibonacci series between 0 to 50:")

for i in range (1,10):
    print(num1)

    next_num = num2 + num1
    num1 = num2
    num2 = next_num


    
#The mirror dimension of the given word

word = "welcome"
print("The original dimension of the word:")
print(word)
print("The mirror dimension of the word:")
print(word[:: -1])



#Don't go outside in odd day

numbers = (11,12,13,14,15,16,17,18,19,20,21)
even_num = 0
odd_num = 0

for x in numbers:
    if not x % 2:
        even_num += 1
    else:
        odd_num += 1
print("number of even numbers:",even_num)        
print("number of odd numbers:",odd_num) 

