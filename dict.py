data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取完了,共有', len(data), '筆資料')
		
wc = {}
for d in data:
	words = d.split() #括弧裡不打字則預設為空白鍵,這種寫法比(' ')這樣寫是避免多個空白連在一起時,被依每個空白鍵切成很多段
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100:
		print(word,wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼字?')
	if word =='q':
		break
	if word in wc:
		print(word,'出現的次數為: ',wc[word])
	else:
		print('這個字沒有在裡面')
print('感謝使用')


