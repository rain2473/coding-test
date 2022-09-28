pw = list(map(int,input()))
len_pw = len(pw)
tmp =[0 for i in range(len_pw+1)]

if pw[0] ==0:
    print(0)
    
else:
    tmp[0] =tmp[1]=1
    pw = [0] + pw
    for i in range(2,len_pw+1):
        if pw[i]>0:
            tmp[i] += tmp[i-1]
        temp = pw[i-1]*10 +pw[i]
        if temp >= 10 and temp <= 26:
            tmp[i] += tmp[i-2]
    print(tmp[len_pw]% 1000000)