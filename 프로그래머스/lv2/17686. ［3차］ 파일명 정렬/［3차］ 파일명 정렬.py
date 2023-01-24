def spliter(file):
    idx = []
    for i,c in enumerate(file):
        try: 
            int(c)
            idx.append(i)
        except:
            if len(idx) != 0:
                break
            else:
                continue
    head = file[:idx[0]]
    number = file[idx[0]:idx[-1]+1]
    tail = file[idx[-1]+1:]
    return [head, number, tail]

def solution(files):
    print(spliter(files[0]))
    result = [spliter(file) for file in files]
    result.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(result) for result in result]
    return answer