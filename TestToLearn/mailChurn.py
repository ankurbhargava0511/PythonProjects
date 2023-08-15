def read_line():
    with open("mbox-short.txt", "r") as file:
        data = file.read()
        print(data)

def number_of_lines():
    with open("./mbox-short.txt", "r") as file:
        data= file.read()
    lines= data.split("\n")
    return len(lines)-1

def count_number_of_lines():
    with open("/mbox-short.txt", "r") as file:
        count=0
        for line in file:
            line= line.rstrip()
            if line.startswith('Subject:'):
                count +=1
    return count

def average_spam_confidence():
    with open("/mbox-short.txt", "r") as file:
        sum_=0
        count=0
        for line in file:
            line= line.rstrip()
            if line.startswith('X-DSPAM-Confidence:'):
                span_confidence= line.split(':')[1]
                sum_ += float(span_confidence)
                count +=1
        average= sum_ /count
        return average


def find_email_sent_days():
    with open("/mbox-short.txt", "r") as file:
        mail_week_day_dict={}
        for line in file:
            line= line.rstrip()
            if line.startswith('From'):
                split_from= line.split(' ')
                try:
                    mail_week_day=split_from[2]
                    if mail_week_day in mail_week_day_dict:
                        mail_week_day_dict[mail_week_day] +=1
                    else:
                        mail_week_day_dict[mail_week_day] =1
                except:
                    pass
        return  mail_week_day_dict

def count_message_from_email():
    with open("/mbox-short.txt", "r") as file:
        mail_week_day_dict={}
        for line in file:
            line= line.rstrip()
            if line.startswith('From'):
                split_from= line.split(' ')
                try:
                    has_day=split_from[2]
                    email=split_from[1]
                    if email in mail_week_day_dict:
                        mail_week_day_dict[email] +=1
                    else:
                        mail_week_day_dict[email] =1
                except:
                    pass
        return  mail_week_day_dict

def count_message_from_domain():
    with open("/mbox-short.txt", "r") as file:
        mail_week_day_dict={}
        for line in file:
            line= line.rstrip()
            if line.startswith('From'):
                split_from= line.split(' ')
                try:
                    has_day=split_from[2]
                    email=split_from[1]
                    domain= email.split('@')
                    print(domain[1])
                    if email in mail_week_day_dict:
                        mail_week_day_dict[email] +=1
                    else:
                        mail_week_day_dict[email] =1
                except:
                    pass
        return  mail_week_day_dict