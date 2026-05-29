def main1():
    designation=input("designation:").lower()
    match designation:
        case "admin"|"super_user":
            print("Full read and write access granted")
        case "editor":
            print("Edit access granted. Cannot delete data")
        case "viewer"|"guest":
            print("Read-only access granted")
        case _:
            print("who?, ohh you are for internship? so cute")

main1()

"""
it was easy ngl, 
ig the idea is still the same, make the code easy to read over smaller,
cuz you dont know what is happening the machine

learned match/case, if elif else, and conditions today fr
"""

def main ():
    user_input=int(input("x:"))
    if height(user_input):
        print("positive")
    else:
        print("negetive")
#if true it is positive
#if false it is negetive


def height(value):
    return value>0 
#think it will always send true or false
main()