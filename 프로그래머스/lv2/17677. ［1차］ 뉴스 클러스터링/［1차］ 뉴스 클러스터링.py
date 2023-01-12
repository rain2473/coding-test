def solution(str1, str2):
    str1, str2, a, b = list(str1.lower()), list(str2.lower()), [], []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(max(len(str1),len(str2))):
        try:
            if str1[i] in alphabet and str1[i+1] in alphabet:
                a.append(str1[i]+str1[i+1])
        except:
            pass
        try:
            if str2[i] in alphabet and str2[i+1] in alphabet:
                b.append(str2[i]+str2[i+1])
        except:
            pass
    inter = []
    for i in sorted(a):
        if i in b:
            inter.append(i)
            a.remove(i)
            b.remove(i)
    union = inter + a + b
    try:
        return int(65536*len(inter)/len(union))
    except:
        return 65536