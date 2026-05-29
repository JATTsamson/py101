def main():
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

main()