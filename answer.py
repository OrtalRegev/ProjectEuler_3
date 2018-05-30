num = 600851475143
biggest = 0
i = 2
while num != 1:
    if num % i == 0:
        biggest = i
        num /= i
        continue
    else:
        if i == 2:
            i += 1
        else:
            i += 2
print(biggest)
