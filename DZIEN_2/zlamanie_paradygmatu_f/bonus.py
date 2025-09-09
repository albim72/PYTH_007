#bonus
nums = [1, 2, 3, 4]
itr  = map(lambda x: x * 2, nums)   # iterator, nie lista!

s = sum(itr)                        # pierwszy przebieg ZUŻYWA iterator
print("suma:", s)                   # 20

print(list(itr))                    # []  ← drugi przebieg nic nie widzi (pustka)

#naprawa
itr  = list(map(lambda x: x * 2, nums))
s = sum(itr)                        # pierwszy przebieg ZUŻYWA iterator
print("suma:", s)                   # 20

print(list(itr)) 
