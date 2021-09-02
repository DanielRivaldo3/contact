
import contact_function

#This program is about contact just like on smart phone but not with GUI
#you can see this program version with GUI on another repository on @DanielRivaldo3

#All data use here aren't real data
contact_fill =[]

contact_fill.append({"name" : "Daniel", 
"mail" : "danielrivaldo@yahoo.com",
"phonenumber":  2345 })
contact_fill.append({"name" : "Rivaldo", 
"mail" : "rivaldodaniel@yahoo.com",
"phonenumber": 5262 })

while True:
    print(20*"=")
    print("Contact Menu :")
    print("1. Contacts ")
    print("2. Create Contact ")
    print("3. Delete Contact")
    print("4. Search")
    print("0. Exit")

    menu = input("Select Contact Menu : ")
    if menu == "0":
        break
    elif menu == "1":
        contact_function.contacts(contact_fill)
    elif menu == "2":
        new_contact = contact_function.create_contact()
        contact_fill.append(new_contact)
    elif menu == "3":
        contact_function.delete_contact(contact_fill)
    elif menu == "4":
        contact_function.search(contact_fill)
    else:
        print("error")
        break
print("Program Finish")
