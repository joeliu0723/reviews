data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		
#算每筆留言的平均長度
sum_len = 0 #總長
for i in data:
	sum_len = sum_len +len(i)#i是data裡的每筆留言(str)
print('留言的平均長度 ='sum_len/len(data))
	 