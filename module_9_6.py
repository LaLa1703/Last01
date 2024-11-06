def all_variants(text):
    for t1 in range(1, len(text) + 1):
        for t2 in range(len(text) - t1 + 1):
            yield text[t2:t2 + t1]

a = all_variants("abc")
for i in a:
    print(i)
