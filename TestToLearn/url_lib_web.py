from urllib import *
from urllib import request

fhand = request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand:
    print(line.strip())
