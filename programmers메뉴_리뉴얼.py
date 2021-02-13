def solution(orders, course):
    DIC = dict()
    for order in orders:
        dic = dict()
        dic.update({"":1})
        for i in range(len(order)):
            ch = order[i]
            stack = []
            for key in dic.keys():
                temp = list(key+ch)
                temp.sort()
                stack.append(''.join(temp))
            for j in range(len(stack)):
                if not dic.__contains__(stack[j]):
                    dic.update({stack[j]:1}) 
                else:
                    dic[stack[j]] += 1
        for key in dic.keys():
            if not DIC.__contains__(key):
                DIC.update({key:1})
            else:
                DIC[key] += 1
    
    S = [[] for i in range(11)]
    for key in DIC.keys():
        l = len(key)
        S[l].append((DIC[key], key))

    answer = []
    for i in course:
        if len(S[i]) == 0:
            continue
        S[i].sort(key=lambda x:-x[0])
        MAX = S[i][0][0]
        if MAX == 1:
            continue
        for j in range(len(S[i])):
            if S[i][j][0] == MAX:
                answer.append(S[i][j][1])
            else:
                break
    answer.sort()
    return answer
