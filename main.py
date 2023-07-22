# var1 = 'value'
# print(var1[0])
# print(var1[1:])
# print(len(var1))

# num1 = 1
# print(num1)
# print(type(num1))

# comp = complex(4 + 6j)
# print(comp)

# str1='hello'
# str2= str1[0:2]+'mm'+str1[4:]
# print(str2)



#  create calculater app

# we will learn about how to deal with if else condition in python and how to take input from user

# what is if else condition


# if else condition is used to check the condition and based on the condition we can perform some action

# if >>> true >> perform some action
# else >>> false >> perform some action


# if else condition syntax
# import numbers


# choose1= input('enter your choice: ')
# #  convert string to int

# if choose1.isdigit():
#     print(choose1)
# else:
#     print('please enter number only')




# for loop in python

# for loop is used to iterate over a sequence
# i = 0
# for i in range(2,10):
#     if i % 2 == 0:
#         print(i)
#     else:
#         print('odd')
# home work for you

# create a program which will take input from user and check if the number is even or odd

# evenOrOdd = int(input('enter your number: '))
# if evenOrOdd == 0:
#     evenOrOdd = int(input('enter your number: '))
# else:
#     if evenOrOdd % 2 == 0:
#         print('even')
#     else:
#         print('odd')


# 2 create a program which will take input from user and check if the number is prime or not

# primeOrNot = int(input('enter your number: '))
# # primeOrNot = primeOrNot + 1
# if primeOrNot > 1:
#     for i in range(2, primeOrNot):
#         if primeOrNot % i == 0:
#             print('not prime')
#             break
#     else:
#             print('prime')

#  3 . take input from user as string and check if the string have l or u in it and replase it with *
# and aleart the user that
# the word have the u and  l and print the index for these lutters
# counter = 0
# while counter < 5:
#     print('_'*50)
#     userInput = input('enter your string: ')

#     for i in range(len(userInput)):
#         if userInput[i] == 'l' or userInput[i] == 'u':
#             print('the word have the u and  l and print the index for these lutters')
#             print(i)
#             userInput = userInput.replace(userInput[i], '*')
#             print(userInput)
#     counter = counter + 1



# elif  condition syntax
# what is elif condition in python
# elif is used to check multiple condition

# if 1 == 2:
#     print('1')
# elif 1 == 3:
#     print('2')
# else:
#     print('unknown')



# switch case in python
# what is switch case in python and how to use it

# switch case is used to check multiple condition

# switch case syntax

# switch:
#     case 1:
#        print('1')

#    case 2:
#       print('2')

#   default:
#      print('unknown')






# while loop in python

# while loop is used to iterate over a block of code as long as the condition is true

# while loop syntax
#  check an input from the user and if the word is == the value that allready stored in the variable
#  print correct in while loop
#  else print wrong and ask the user to enter the word again

# secretWord = 'python'
# # userInput = input('enter your word: ')
# c = 0
# check = True
# while check:
#     userInput = input('enter your word: ')
#     c = c + 1
#     if userInput == secretWord:
#         print('correct')
#         break
#     else:
#         print('wrong')
#         if c == 2:
#             check = False
#             print('you have reached the limit')
#             break

# home work for you

# all the last previous home works will be added in 1 while loop
# the first is to check if the number is even or odd 3 times
# the second is to check if the number is prime or not 3 times
# the third is to check if the string have l or u in it and replase it with * 3 times

# functions in python

# what is function in python and how to use it

# function is a block of code which only runs when it is called

# function syntax
# 1- function without parameters
# def myFunction():
#     print('hello world')
#     // code here

# myFunction()

# def myFunction():
#     print('hello world')

# myFunction()

# 2 - function with parameters

# def myFunction(partmenter, partmenter2):
#    print(partmenter)
#    print(partmenter2)

# myFunction('hi', 'hello')

# 3 - function with return

# def myFunction1():

#    return 'hello world'


# print(myFunction1())


# live example about function in python
# create a function which will take 2 parameters and return the sum of these 2 parameters

# num1 = int(input('enter your first number: '))
# num2 = int(input('enter your second number: '))

# def sum(num1, num2):
#     return num1 + num2

# print(sum(num1, num2))

# home work for you

# convert the last home work to function (prime number, even or odd, string with l or u)

# number1 = int(input('enter a number to check if it is prime or not:'))
# def ifprime(number1):
#     for i in range(2,number1):
#       if number1 % i == 0:
#         print ('the number is not prime')
#         break
#       else:
#         print('the number is not prime')
#   for i in range(2,number1):
#     if number1 % i == 0:
#       print ('the number is not prime')
#       break
#     else:
#       print('the number is not prime')

# def oddoreven(number2):
#     if number2 % 2 == 0:
#       print('even')
#     else:
#       print('odd')

# var1 = input('enter a string to check if it has l or u: ')
# def str1(var):
#     for i in range(0,len(var)):
#       if var[i]=='u' or var[i]=='l':
#             var=var.replace(var[i] , '*')
#     print(var)

# ifprime(number1)
# oddoreven(number1)
# str1(var1)



# #    Alice, that was a great trick!
# #    I can't wait to see your next trick, Alice.
# #    David, that was a great trick!
# #    I can't wait to see your next trick, David.
# #    Carolina, that was a great trick!
# #    I can't wait to see your next trick, Carolina.

# def magicTrick(names):
#     for i in names:
#         print(i + ', that was a great trick!')
#         print("I can't wait to see your next trick, " + i + '.\n')

# magicTrick(names)


# counter=0
# while counter<3:


#     word=input("enter a word to check")

#     if "i" in word and "u" in word:

#         print("the word have a both of letters")

#         replace_words=word.replace("i", "*").replace("u","*")

#         print("replace_words", replace_words)

#         i_indexing=[i for i in range(len(word)) if word [i]=="i"]


#         u_indexing=[i for i in range(len(word)) if word [i]=="u"]
#         print("the indexing of i : ",i_indexing)
#         print("the indexing of u : ",u_indexing)

#     elif "i" in word:

#        print("the word have i just")
#        replace_i=word.replace("i","**")
#     #    I_indexing=[i for i in range(len(word)) if word (i)=="i"]
#        print("the indexing of i : "+replace_i)
#     elif "u" in word:

#        print("the word have u just")
#        replace_u=word.replace("u","***")
#        U_indexing=[i for i in range (len(word)) if word [i]=="u"]
#        print("the indexing of u :", U_indexing)
#     else:
#      print("we dont have the letters ")
#     counter=counter+1
#     #task2


# numTest = int(input("enter a number to check if it is prime or not: "))
# for i in range(2, numTest):
#     if numTest % i == 0:
#         print("the number is not prime")
#         break
# else:
#         print("the number is prime")
# counter = 0
# names = ['Alice', 'David', 'Carolina']
# for i in names:
#     # print(counter)
#     # print(i)
#     if i == 'Alice':
#         names = names[0:counter] + names[counter + 1:]
#         print(names)
#     counter = counter + 1

# solve the index[0] problem  in the list to print all the names except the
# first one
# try to add new value to the list and print it using the user input

names = ['Alice', 'David', 'Carolina' ,9]
# test = ['test']
# names = names+ ['mohammed']
# print(names)

# methods for list in python

# append method : is used to add new value to the list at the end of the list
# names.append('mohammed')
# names = names[0:2] +[ 'value'] + names[2:]

# insert method : is used to add new value to the list at the index that you want
names.insert(1, 'mohammed')
# print(names)

list1 = [1, 2, 3, 4, 5,1 ,1,4]
list2 = [6, 7, 8, 9]
# extend method : is used to add new list to the list at the end of the list

# sumList= 0
# for i in list1:
#     sumList = sumList + i

# sum  : is used to get the sum of the list
# print(sum(list1))

# count : is used to get the count of the value in the list
# print(list1.count('1'))
# print(len(list1))   # len : is used to get the length of the list

# print the index of the value in the list

# counter = 0

# for i in list1:
#     if i == 4:
#         print(counter)

#     counter = counter + 1

# index : is used to get the index of the value in the list

# print(list1.index('1'))


maxValue = 0

minValue = 0

# print(max(list1))
# print(min(list1))

# pop : is used to remove the value from the list based on the index

print(list1.pop())  # remove the last value from the list
print(list1)

# remove : is used to remove the value from the list based on the value

print(list1.remove(2))
print(list1)

# reverse : is used to reverse the list
# sort : is used to sort the list
print(list1.reverse()) # reverse the list
print(list1)

list1.sort(reverse=True) # sort the list in descending order
print(list1)

# home work for you



