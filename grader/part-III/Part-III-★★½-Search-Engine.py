docs = {}

for i in range(int(input())):
    name = input()
    docs[name] = input()

words = []
word = input()
while word != '-1':
    words.append(word)
    word = input()

scores = {}
for word in words:
    scores[word] = {}
    for k in docs:

        listWord = docs[k].split()
        scores[word][k] = (listWord.count(word) / len(listWord)) * (1/len(set(listWord)))

ans = []
for word in words:
    top = max(scores[word].values())
    count = 0
    result = ''
    for doc in scores[word]:
        if scores[word][doc] == 0:
            count += 1
        if scores[word][doc] == top:
            result = doc
    if count == len(scores[word].keys()):
        ans.append('NOT FOUND')
    else:
        ans.append(result)

print(*ans,sep='\n')