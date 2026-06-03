n=7

x=int(input("Enter your number:"))

def main(prediction):
    
    if prediction==n:
        print("congo, its correct")

    elif prediction>n:
        print("too high")
    else:

        print("too low")

while x!=n:
    main(x)
    x=int(input("Enter your number:"))

main(x)