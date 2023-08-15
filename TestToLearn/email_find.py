'''
def email_func(data):
    find_value = []
    for string in data.split(' '):
        if string.find('@') > 0:
            find_value.append(string)
    if len(find_value) > 0:
        return find_value[0]
    else :
        return False
'''

def email_func(data):
    find_value = [string for string in data.split(' ') if string.find('@') > 0]
    return find_value[0] if len(find_value) > 0 else False

#print(email_func("Crazy Frog"))

#print(email_func("this is first abhinav@cloudxlab.com and this is second sandeep@cloudxlab.com"))

print(email_func("a a@"))