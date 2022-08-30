word="KAI"
result=[]
for i in range(len(word)):
    for j in range(len(word)):
        for k in range(len(word)):
            if i==j or j==k or i==k:
                continue
            result.append(word[i]+word[j]+word[k])
print(result)