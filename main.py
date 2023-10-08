with open('advent3.txt', 'r') as file:
	rucksack = file.read().split()

def element_priority(letter):
	if letter.islower():
		return ord(letter) - ord('a') + 1
	else:
		return ord(letter) - ord('A') + 27

def find_common_items(rucksack):
	common_item_types = []
	for item in rucksack:
		a_1, a_2 = item[:len(item)//2], item[len(item)//2:]
		unique = []
		for k in sorted(a_1):
			if k not in unique:
				unique.append(k)
		for x in unique:
			if x in sorted(a_2):
				common_item_types.append(x)
	return common_item_types

def badges(rucksack):
	badge_list = []
	for i in range(0, len(rucksack), 3):
		sack_1, sack_2, sack_3 = rucksack[i:i+3]
		badge = set(sack_1) & set(sack_2) & set(sack_3)
		badge_list.append(badge.pop())
	return badge_list

common_item_priorities = [element_priority(i) for i in find_common_items(rucksack)]
badge_priorities = [element_priority(i) for i in badges(rucksack)]

print(sum(common_item_priorities), sum(badge_priorities))