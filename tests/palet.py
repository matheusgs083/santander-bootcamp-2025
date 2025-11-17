def boxs_per_palet(capacity,boxs):
    return round(boxs/capacity)

box = int(input())
capacity = int(input())

boxs_per_palet = boxs_per_palet(capacity,box)

print(f"{boxs_per_palet:.0f}")
