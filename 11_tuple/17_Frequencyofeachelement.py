'''
🐍 Challenge 9 — Frequency of each element
Let's increase the difficulty again, ra! This time, we want to know how many times each product ID appears.

product_ids = (101, 205, 101, 310, 205, 101, 420, 310)

Expected result:

101: 3
205: 2
310: 2
420: 1

'''
product_ids = (101, 205, 101, 310, 205, 101, 420, 310)

processed_ids = ()
freq = ()

for id in product_ids:
    if id not in processed_ids:
        count = 0

        for ids in product_ids:
            if id == ids:
                count += 1

        processed_ids += (id,)
        freq += ((id, count),)

for item in freq:
    print(f"{item[0]}: {item[1]}")

