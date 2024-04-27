data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 4000 ==0: # %求餘數
		# 	print(len(data))

# print(len(data)) # 看資料數
# print('-'*30)
# print(data[0]) # 印出第一筆
# print('-'*30)
# print(data[1])

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
print('一共有', len(good), '筆資料留言')
print(good[0])
