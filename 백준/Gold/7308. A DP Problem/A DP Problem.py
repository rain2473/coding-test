T = int(input())
for t in range(T):
    a,b = input().split("=")
    a = a.split('-')
    new_a = a[0].split('+')
    if len(a)>1:
        for i in range(1,len(a)):
            a[i]='-'+a[i]
            new_a=new_a+(a[i].split('+'))
    a=[]
    a_int=[]
    for num in new_a:
        if 'x' in num:
            if num == '-x':
                a.append(-1)
            elif num == 'x':
                a.append(1)
            else:
                a.append(int(num.replace('x','')))
        elif num !='':
            a_int.append(int(num))
            
    b = b.split('-')
    new_b = b[0].split('+')
    if len(b)>1:
        for i in range(1,len(b)):
            b[i]='-'+b[i]
            new_b=new_b+(b[i].split('+'))       
    b=[]
    b_int=[]
    for num in new_b:
        if 'x' in num:
            if num == '-x':
                b.append(-1)
            elif num == 'x':
                b.append(1)
            else:
                b.append(int(num.replace('x','')))
        elif num !='':
            b_int.append(int(num))
    x = sum(a)-sum(b)
    k = sum(b_int)-sum(a_int)
    
    if x == 0:
        if k==0:
            print('IDENTITY')
        else:
            print('IMPOSSIBLE')
    else:
        ans=abs(k)//abs(x)
        if x*k>=0:
            print(ans)
        else:
            print(-1*(ans+1))