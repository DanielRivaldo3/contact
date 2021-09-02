

#show all contacts
def contacts(contact_fill):
    for all_contact in contact_fill:
        print(10*"=")
        print(f'name :  {all_contact["name"]}')
        print(f'mail :  {all_contact["mail"]}')
        print(f'phonenumber :  {all_contact["phonenumber"]}')

#create new contact
def create_contact():
    name = input('name : ')
    mail = input('mail : ')
    phonenumber = input('phonenumber : ')
    contacts = { "name" : name,
    "mail" : mail,
    "phonenumber" : phonenumber}
    return contacts
    
#delete contact
def delete_contact(contact_fill):
    delete = input("name contact :")
    index = -1
    for i in range(0,len(contact_fill)):
        contact = contact_fill[i]
        if delete == contact_fill["name"]:
            index = i
            break
    if index == -1 :
        print("data not found")
    else:
        del contact_fill[i]
        print("data success deleted ")

#seacrh contact
def search(contact_fill):
    search_contact = input("search : ")
    for contact in contact_fill:
        name = contact["name"]
        if name.lower().find(search_contact.lower()) != -1:
            print(10*"=")
            print(f'name :  {contact["name"]}')
            print(f'mail :  {contact["mail"]}')
            print(f'phonenumber :  {contact["phonenumber"]}')


