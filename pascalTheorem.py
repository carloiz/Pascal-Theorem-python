def pascal(h, d, c, delop, list, list2):
    if c >= 3:
        list = []
    list.append(1)
    if c >= 3:
        x = 0
        for x in range(d):
            b = 0
            b = list2[x] + list2[x + 1]
            x = x + 1
            list.append(b)
        list.append(1)
        d = d + 1
      
    list2 = list
    
    g = ""
    for i in range(h):
        g = g + "  "
    
    i = ""
    for v in list:
        if len(str(v)) == 1:
            i = str(i) + "   " + str(v) 
        elif len(str(v)) == 2:
            i = str(i) + "  " + str(v)
        elif len(str(v)) == 3:
            i = str(i) + " " + str(v)
        else:
            i = str(i) + str(v)
        
    print(g, i)
    
    h = h - 1
    c = c + 1
   
    if c >= delop:
        return
    pascal(h, d, c, delop, list, list2)

while True:
    delop = int(input("Enter How Many: "))
    pascal(delop - 2, 1, 1, delop, list=[], list2=[])
    print()
       
        
   
        
        
        


# print(a)
#    a = a + a
#    c = c + c
#    print(a)
#    a = str(b) + str(c) + str(b)
  #  print(a)
#    break