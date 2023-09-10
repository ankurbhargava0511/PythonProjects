
with open ("E:\AWS\File1.txt", encoding="utf8") as file:
    with open("E:\AWS\File2.txt", "a", encoding="utf8") as file1:
        data= file.readlines()
        for line in data:
            if  line.startswith("© Stephane Maarek") :
                continue
            elif  line.startswith("NOT FOR DISTRIBUTION ") :
                continue
            elif  line =="":
                continue
            else:
                file1.write(line)
