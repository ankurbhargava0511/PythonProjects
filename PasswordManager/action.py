from Config import actions
from passwordgenertor import get_password
from filemanager import FileManger

m_file = FileManger()


def save_to_pm(web: str, user: str, pwd: str) -> None:
    is_save: str = input("Press Y to Save the details.").upper()
    if is_save == "Y":
        m_file.savedata(web, user, pwd)


def action_selector():
    for action in actions:
        print(action)
    user_action = input("Please select your action from above list\n")

    if user_action == "Add":
        webpage = input("Please Provide WebPage address\n")
        user_name = input("Please Provide UserName\n")
        user_password = get_password()
        save_to_pm(webpage, user_name, user_password)
    elif user_action == "Update":
        webpage = input("Please Provide WebPage address\n")
        details = m_file.getdata(webpage)
        new_password = get_password()
        save_to_pm(webpage,details,new_password )
    elif user_action == "Retrieve":
        webpage = input("Please Provide WebPage address\n")
        details = m_file.getdata(webpage)
        print(details)
    elif user_action == "Upload":
        file_type = input("Please provide File Type. CSV, XML , JSON\n")
        file_name = input("Please full file name\n")
        m_file.upload_data(file_type,file_name)
    elif user_action == "Download":
        file_type = input("Please provide File Type. CSV, XML , JSON\n")
        file_name = input("Please full file name\n")
        m_file.download_data(file_type, file_name)
    else:
        print("sorry. Wrong Selection")
