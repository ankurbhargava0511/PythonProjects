try:
    file=  open("test.txt") #FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
    a_dict={"key":"value"}
    print(a_dict["abcd"]) #keyError 'abcd'

except FileNotFoundError:
    file = open("test.txt","w")
    file.write("something")
except KeyError as error_message:
    print (f"The key {error_message} does not exist.")

else :
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")





try:
    fruit_list= ["Apple", "Banana","Pear"]
    fruit=fruit_list[5]
except IndexError as ind:
    print(ind)

try :
    text ="abc"
    print(text + 5)
except TypeError as message:
    print (message)
    raise ValueError("my message")
