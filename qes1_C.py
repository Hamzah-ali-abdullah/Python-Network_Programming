L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

filtered_list = filter(lambda x: x.startswith('B'), L)

for i in filtered_list:
    print(i)
