import re

output = []
unduplicate = []

# --------------------------------------------------
#read potential-contacts.txt
def read_mails():
    with open('potential-contacts.txt','r') as mail:
        read = mail.read()
    return read
# --------------------------------------------------
def emails_pure():
    validation = r'([\w\.-]+)@([\w\.-]+)'
    reader = read_mails()

    get_all = re.findall(validation, reader)
    for i in range(len(get_all)):
        get_all[i] = '@'.join(get_all[i])    
    get_all.sort()    

    with open('emails.txt','w') as E:
        for i in get_all:
            if i not in unduplicate:
                E.write(str(i)+'\n')
            unduplicate.append(i)
# --------------------------------------------------
def get_phones():
    rendered_phone_num = r'([+]?[(]?[0-9]{1,4}[)]?)([-|.]?[0-9]{1,4})([-|.]?[0-9]{1,4})([-|.]?([0-9]{1,4})?)([x]?([0-9]{1,7})?)'
    reader = read_mails()
    valid_numbers = re.findall(rendered_phone_num,reader)
    
    for i in range(len(valid_numbers)):
        valid_numbers[i]= list(valid_numbers[i])
        print(i)
        valid_numbers[i][6]=''
        valid_numbers[i][4]=''
        valid_numbers[i]=''.join(valid_numbers[i])

    print(valid_numbers)
    valid_numbers.sort()
    
#---------------------------------------------------
    with open('phone_numbers.txt','w') as phone:
        remove_duplicate =[]
        for i in valid_numbers:
            if i not in remove_duplicate:
                if i[0]== '+' or i[0] == '(':
                    phone.write(str(i)+'\n')
                elif i[0]=='0' and i[1]=='0' and i[2]=='1':
                    phone.write(str(i)+'\n')
                else:
                    phone.write('206-'+str(i)+'\n')
            remove_duplicate.append(i)
# --------------------------------------------------
if __name__ == "__main__":
    emails_pure()
    get_phones()
    