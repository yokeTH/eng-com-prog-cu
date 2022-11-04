word = input()
message = input().split()
cnt = 0
# for i in message:
#     i = i.strip('"\'(),.')
#     n = len(word)
#     if len(i) < n:
#         n = len(i)
#     for j in range(n):
#         if not i[j] == word[j]:
#             break
#         else:
#             if j == n-1:
#                 cnt+=1

for i in message:
    i = i.strip('"\'(),.')
    if i == word:
        cnt+=1

print(cnt)