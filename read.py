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


# 求每筆資料平均長度
sum_len = 0

for d in data:
	sum_len += len(d)
# print(sum_len)

average_len = sum_len / len(data)
print('每筆資料的平均長度為:', average_len)