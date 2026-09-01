k='aabbccddeff'
# ans={}
# for i in k:
#     ans[i]+=1
# for key,values in ans.items():
#     if values==1:
#         print(ans[key])
# count={}
# for i in k:
#     count[i]=count.get(i,0)+1
# for j in k:
#     if count[j]==1:
#         print(j)
#         break

count={}
for i in k:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for key,values in count.items():
    if values==1:
        print(key)


