letter = ''' dear <|name|>,
             You are selected !!!
             on <|Date|> '''
name = input("Enter Your Name : ")
date = input("Enter Date : ")

print(letter.replace("<|name|>",name).replace("<|Date|>",date))

#str.replace("old str","new str") = its used to replace the old str to new str.