''''
import re

ini_string=input('Ebter a String:')
res1=" ".join(re.split("[^a-zA-Z]*", ini_string))
res2=" ".join(re.split("[^0-9]*", ini_string))
print("Second string result: ", str(res2))
print("First string result: ", str(res1))
'''
total_list=input("Enter a string of numbers and words seperated by spaces:\n").split() #asks the user to Enter a string of numbers and words seperated by spaces, then saves it in the variable total_list
num_list = [] # creates an empty list called num_list
def find_numbers(n):  #defines a function where it takes a list and splits it into a list of numbers and a list of words 
  word_list = [] # creates an empty list called word_list
  global num_list
  for i in n: # loops through all the objects