"""
weight converter
what it needs: input (both value and unit), and convert
"""

def main():
    x=float(input("enter the weight:"))
    y=str(input("kgs(K) or lbs(L):")).upper()
    if y=="K":
        print("your weight in lbs:",round(x/2.20462,2),"lbs")
    elif y=="L":
        print("your weight in kgs:",round(x*2.20462,2),"kgs")
    else:
        print( "there is an error, check your inputs")

main()