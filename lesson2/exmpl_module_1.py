from collections import Counter

phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8', 'iPhone Xs', 'Xiaomi Mi8']
count = Counter(phones)

print(count)
print(count['iPhone Xs'])