N, need = map(int,input().split(" "))
trees = list(map(int,input().split(" ")))
start, end = 1, max(trees)
while start <= end:
    wood = 0
    height = (start + end) // 2
    for tree in trees:
        wood += (tree - height) * (tree > height)
        
    if wood < need:
        end = height - 1
    else:
        start = height + 1
    
print(end)