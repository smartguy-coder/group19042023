import re

text = 'Isgfsgfsfgyg9 glove9 I love055999 Love8 lovef l8ve1 lgve1 123python'
text2 = 'I'



# start_index = text.find('love')
# print(start_index)

match = re.findall(r'\blove', text)
match = re.findall(r'\bl.ve.', text)
match = re.findall(r'\blove\d', text)
match = re.findall(r'\blove\D', text)
match = re.findall(r'\b[lL]ove\d', text)
match = re.findall(r'\b[lL]ove\d{1,3}', text)
match = re.findall(r'\b[lL][\w\d]ve\d{1,3}', text)

match = re.findall(r'^I\w*', text)
match = re.findall(r'\w*\s\w*on$', text)
print(match)



mail = 'gjhdsgf d@gmail.com її@gmail.com'

res = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', mail)
print(res)