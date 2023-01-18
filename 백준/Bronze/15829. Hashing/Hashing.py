hashcode, answer = " abcdefghijklmnopqrstuvwxyz", 0
N = int(input())
string = " ".join(list(input()))
for i in range(1,27):
    string = string.replace(hashcode[i],str(i))
string = string.split(" ")
for i,s in enumerate(string):
    answer += int(s)*(31**i)
answer %= 1234567891
print(answer)