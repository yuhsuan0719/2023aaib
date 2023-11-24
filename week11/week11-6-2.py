a = list(map(int, input().split() ))

#a[0] a[i] ... a[9]
ans = 0
for b in a:
	if b%3==0: ans+=1
	
	
print(ans)