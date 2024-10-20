#string : it is the sequence of character which is typically enclosed with the inverted commas either single or double

str = 'sumit'       #single line string simultaneously it is single quoted string
str2 = "gangster"   #double quoted string
str3 = ''' sumit 
           bhai jann
           ganga'''  #multi line string simultaneously it is triple quoted string

print(str,str2,str3)

# string slicing : Slicing in Python is a technique used to extract specific portions or subsequences from data structures like strings, lists, or tuples. It allows you to access a range of elements by specifying a start index, an end index, and an optional step size.

str = "Sumit"
str_slice = str[0:4]   #0 is started index it is counted and 4 is end index it is not counted
char = str[1]  # print value on index 1 in str
str1_Slice = str[1:] #print all the character from index 1 to atlast in str 
print(str_slice,char,str1_Slice)

#negative slicing : negative slicing in python is a technique used to extract specific portion from data strctures like string , list or tuple using negative index . it allow you to access a range of element by specifying a start negative index and end negative index.

str = "Sumit"
str_slice = str[-4:-1]   #-4 is started index it is counted and -1 is end index it is not counted
char = str[-1]  # print value on index -1 in str
str1_Slice = str[-5:] #print all the character from index -5 to atlast in str 
str4 = str[ :-1 ]
print(str_slice,char,str1_Slice,str4)

#slicing with steps :  Slicing with steps in Python allows you to extract elements from a sequence (like a string, list, or tuple) by specifying an interval, or "step," between the elements you want to include in the result. This is done using the slicing syntax:

str = "12345678910"
str_slice = str[0:10:2]
print(str_slice)
