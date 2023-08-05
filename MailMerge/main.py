
with open("..\MailMerge\Input\Letter\Mail.txt", "r") as letter:
    mail_content = letter.read()

    with open("Input/AllName/Name.txt", "r") as names:
        name_content= names.read()
        guest_names=name_content.split('\n')
        for guest_name in guest_names:
            new_letter= mail_content.replace('[user]',guest_name)
            with open(f"Output/ReadyToSend/{guest_name}.txt", "w") as file:
                file.write(new_letter)





