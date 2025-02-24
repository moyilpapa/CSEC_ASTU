h = map(int, input().split())
 
if not (1 <= n <= 1000 and 1 <= h <= 1000):
    print("invalid input")
    exit()
 
a = list(map(int, input().split()))
 
if len(a) != n:
    print("invalid input")
    exit()
 
mpvw = 0
 
for i in a:
    if not (1 <= i <= 2 * h):
        print("invalid input")
        exit()
    
    if i <= h:
        mpvw += 1
    else:
        mpvw += 2