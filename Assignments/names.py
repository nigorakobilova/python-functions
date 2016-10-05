# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# def names(arr, title):
#     print title
#     for x in range(0, len(arr)):
#         fullname = arr[x]['first_name'] + ' ' + arr[x]['last_name']
#         print fullname
#
# names(students, 'Students')


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
    count=0
    storage=0
    print key
    for val in data:
        fullname = val['first_name']+' '+ val['last_name']
        count += 1
        storage = len(fullname)-1
        print count, '-', fullname.upper(), '-', storage
