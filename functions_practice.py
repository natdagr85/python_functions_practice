def  hello():
    print('Hello world')

def pack(x,y,z):
    my_list= [x,y,z]
    return my_list

def eat_lunch(ex_list):
  if len(ex_list) == 0:
    print("no food in lunch box :(")
  else:
    for i in range(len(ex_list)):
      if i == 0:
        print(f"First I eat {ex_list[0]}")
      else:
        print(f"Next I eat {ex_list[i]}")

hello()
print(pack('test1', 'test2','test3'))
eat_lunch([])
eat_lunch(["chicken"])
eat_lunch(['chicken', 'pizza', 'sandwich'])