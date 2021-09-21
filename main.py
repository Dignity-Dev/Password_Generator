from random import *
mixcharacter = "abcdefghijklmnpqrstyvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}][;/><.,\|:"
randomcheck = "".join(choice(mixcharacter) for x in range(randint(8, 20)))
print("yor password is: ", randomcheck)