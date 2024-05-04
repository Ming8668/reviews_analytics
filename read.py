data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 4000 ==0: # %求餘數
		# 	print(len(data))

print('檔案讀取完畢, 總共有', len(data), '筆資料')
print('-' * 40)


# 求每筆資料平均長度
sum_len = 0

for d in data:
	sum_len += len(d)
# print(sum_len)

average_len = sum_len / len(data)
print('每筆資料的平均長度為:', average_len)
print('-' * 40)


# 清單的篩選
new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料留言長度小於100')
print(new[0])
print('-' * 40)

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料留言含有good')
print(good[0])
print('-' * 40)


# list comprehension 清單快寫法

bad = [d for d in data if 'bad' in d]

print('一共有', len(bad), '筆資料留言含有bad')
print(good[0])
print('-' * 40)



# 文字的計數
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key進字典

# for word in wc:
# 	if wc[word] > 100:
# 		print(word, wc[word])
# print(len(wc))

while True:
	word = input('請問你想找什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word], '次')
	else:
		print('查無此字!!')

print('-' * 40)
print('感謝使用!!')


