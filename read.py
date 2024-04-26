data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0: # %求餘數
			print(len(data))

print(len(data)) # 看資料數
print('-'*30)
print(data[0]) # 印出第一筆
print('-'*30)
print(data[1])