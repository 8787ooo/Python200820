d = {}
print('welcome')
while True:
    print('1.建立')
    print('2.顯示')
    print('3.e-c')
    print('4.c-e')
    print('5.test')
    print('6.bye')
    o = input('choose:')
    if o == '6':
        break
    elif o == '1':
        while True:
            v = input('voc(0:lift)')
            if v =='0':
                break
            if v not in d:
                vc=input('ch')
                d[v] = vc
            else:
                print('voc is have')
    elif o == '2':
        s = sorted(d)
        for i in s:
            print(i,':',d[i])
    elif o == '3':
        while True:
            voc = input('eng')
            if voc == '0':
                break
            if voc in d:
                print(voc,'的中文',d[voc])
            else:
                print('no')
    elif o == '4':
        while True:
            g = False
            ch = input('ch')
            if ch == '0':
                break
            for k,v in d.items():
                if ch == v:
                    print(ch,'英文',k)
                    g = True
            if g == False:
                print('no')
    elif o == '5':
        s = 0
        for k,v in d.items():
           print(v)
           ans = input(':')
           if ans == k:
               s+= 1
               print('yes')
           else:
               print('no')
        print('total',s)
        

    
    
    
    
            
            