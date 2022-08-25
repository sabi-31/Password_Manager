from pm_file_op import *
from pm_login import *
from pm_generator import *
from pm_encryption_handler import *
recursion_flag = True


def main():
    choice = input("1.Login to exisitng user\n2.Create new user\n*.Quit\n:")
        
    if choice == '1':
        print("User Login Portal\n=================")
        existing_name = input("Enter Name: ")
        master_password = input("Enter Master Password: ")
        login_credentials = unlock_user(existing_name, master_password)
        
        if login_credentials:
            try:
                while True:
                    user_choice = input("Choose an Option:\n1. View Saved Logins\n2. Add a new Login\n*. Logout\n:")
                    
                    if user_choice == '1':
                        print_vault(existing_name)   
                    elif user_choice == '2':
                        print("--------------------")
                        title = input("Choose a suitable Title: ")
                        print("--------------------")
                        user_name = input("Enter Username: ")
                        print("--------------------")
                        user_choice = input("Do you want to:\n1.Enter the password yourself  2.Generate a random Password \n:")
                        
                        if user_choice == '1':
                            password = input("Enter Password: ")
                            save_to_file(existing_name, master_password, title, user_name, password)
                            print("Login for ", title, " saved succesfully")    
                        else:
                            config = input("\nDefault generated password length is 8 and contains 2 uppercase letters, 2 lowercase letters, 2 numbers and 2 symbols.\nContinue with this configuration? (Y/n)")
                            
                            if config == 'n':
                                print("\nDefine custom configuration\n---------------------------")
                                character_type_default_occurence[lower] = int(input("How many lowercase letters do you want? "))
                                character_type_default_occurence[upper] = int(input("How many uppercase letters do you want? "))
                                character_type_default_occurence[numbers] = int(input("How many numbers do you want? "))
                                character_type_default_occurence[symbols] = int(input("How many symbols do you want? "))
                            password = rand_password()
                            print("Your randomly generated password is:", password)
                            print("Login for", title, "saved succesfully")
                            save_to_file(existing_name, master_password, title, user_name, password)
                    else:
                        print("Logged out and locked ", existing_name,"'s Vault", sep ='')
                        encrypt_vault(existing_name, master_password)
                        break
            except:
                print("An Error Occured")
            finally:
                encrypt_vault(existing_name, master_password)
    elif choice == '2':
        print("User Creation Portal\n====================")
        new_name = input("Select a Username: ")
        new_password = input("Select a strong Password: ")
        make_user(new_name,new_password)
    else:
        print("Program is Exited Succesfully")
        global recursion_flag 
        recursion_flag = False


if __name__ == "__main__" :
    while recursion_flag:
        main()
