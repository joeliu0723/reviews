data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取完了,共有', len(data), '筆資料')
		
#算每筆留言的平均長度
sum_len = 0 #總長
for i in data:
	sum_len = sum_len +len(i)#i是data裡的每筆留言(str)
print('留言的平均長度 =', sum_len/len(data))

#篩選字數小於100的留言
new = []
for d in data:
	if len(d)< 100:
		new.append(d)
print('共有',len(new),'筆資料留言小於100字')
	 