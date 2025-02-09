n=int(input ())
h=int(input())
MPVW=0
for i in range (n):
    a=int(input())
    if a>2*h:
        print ("Invalid Input")
    elif 5<a<=2*h:
        MPVW+=2
    else:
        MPVW+=1
print(MPVW)   
