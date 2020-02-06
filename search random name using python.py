g = ['hello','jello','mereka','sohib','kari']
search_in = str(input('Please insert '))
find_in = list(filter(lambda x : search_in in x, g ))
print(find_in)
print(g)