num_list = input().split('-')
print(sum(map(int, num_list[0].split('+'))) + sum(-(sum(map(int, num_list[i].split('+')))) for i in range(1, len(num_list))))