my_string = 'масло сир макарони'

# new list
purchase_list = my_string.split()
something2_new_list = my_string.split(' сир ')

new_list = ['broccoli', 'bread']
new_list_2 = list()


for word in purchase_list:
    print(word, end=' ** ')

# get elements
string_slice = my_string[-1]
list_slice = purchase_list[-1]
# list_slice_ = something_new_list[5]

string_slice2 = my_string[1:4]
list_slice2 = purchase_list[1:5]

# add elements
purchase_list.append(5)
purchase_list.append('ball')
purchase_list.extend(new_list)

purchase_list.insert(0, 'beer')



# delete data
purchase_list.pop(0)  # 0- index
purchase_list.pop()  # last elem

purchase_list.remove(5)  # defined (first) element