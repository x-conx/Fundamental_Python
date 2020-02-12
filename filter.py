# employee = [
#     {"name": 'Steve',"gender": 'male',"hobbies":['Video games','Football']},
#     {"name": 'Liina',"gender": 'female',"hobbies":['Shopping','Cooking']},
#     {"name": 'Reynald',"gender": 'male',"hobbies":['Run','Jump','hide']},
# ]

# # print(f'Mr.Steve  has 2 hobbies, they are video games and football')
# # print(f'Mrs.Lina  has 2 hobbies, they are shopping and cooking')
# # print(f'Mr.Reynald  has 3 hobbies, they are run, jump, and hide')

# # for x in employee:
# #     print(x)
# #     for f in employee(x):
# #         print(y, ' : ',employee[x][y] )

# # print(employee[0])
# # print(employee[1])
# # print(employee[2])

# for i in employee:
#     #i is dictionary
#     if i["gender"] == 'male':
#         i["name"]= 'Mr. ' + i["name"]
#     else:
#         i["name"]= 'Mrs. ' + i["name"]
    
#     name = i["name"]
#     hobbies = " ,".join(i["hobbies"])
#     len_hobs = len(i["hobbies"])

#     print(
#         f'{name} has {len_hobs} hobbies, they are {hobbies}'
#     )

# for i in range (len(employee)):
#     print(employee[i])
#     i+=1len(i["hobbies"])



mylist = ['Mixed Case One', 'Mixed Case Two', 'Mixed Three']
mylist =  list(map(lambda x: x.lower(), mylist))
print(mylist)
