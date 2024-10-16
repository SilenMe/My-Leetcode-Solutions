#since there are only 3 elements, using heap is not but benificial so solving using brute force
#this code can be refactor with proper use of if-else


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        main=''
        while (a!=0 and b!=0) or (c!=0 and b!=0) or (a!=0 and c!=0):
            mx=max(a,b,c)
            if mx==a:
                st='a'
            elif mx==b:
                st = 'b'
            else:
                st = 'c'
            if len(main)<2:
                if st == 'a':
                    main += 'a'
                    a -= 1
                if st == 'b':
                    main += 'b'
                    b -= 1
                if st == 'c':
                    main += 'c'
                    c -= 1
                continue
            if main[-2:]==st+st:
                if st=='a':
                    sst=max(b,c)
                    if sst==b:
                        main+='b'
                        b-=1
                    else:
                        main+='c'
                        c-=1
                if st=='b':
                    sst=max(a,c)
                    if sst==a:
                        main+='a'
                        a-=1
                    else:
                        main+='c'
                        c-=1
                if st=='c':
                    sst=max(a,b)
                    if sst==a:
                        main+='a'
                        a-=1
                    else:
                        main+='b'
                        b-=1
            else:
                if st=='a':
                    main+='a'
                    a-=1
                if st=='b':
                    main+='b'
                    b-=1
                if st=='c':
                    main+='c'
                    c-=1
        mx=max(a,b,c)
        if mx==a:
            if mx==0:
                pass
            elif mx==1:
                main+='a'
            else:
                main+='aa'
        if mx==b:
            if mx==0:
                pass
            elif mx==1:
                main+='b'
            else:
                main+='bb'
        if mx==c:
            if mx==0:
                pass
            elif mx==1:
                main+='c'
            else:
                main+='cc'
        return main


