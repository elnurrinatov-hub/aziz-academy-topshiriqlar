s = 6 
c = 0 
while c < 3:
        g = int(input())
        
        if g < 1 or g > 10:
            print("Invalid")
            continue
            
        c += 1 
        
        if g == s:
            print("Correct")
            
