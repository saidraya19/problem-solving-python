import requests
def reve(rev):
    rev = list(rev)
    i = 0
    j = len(rev) - 1
    while i < j:
        rev[i], rev[j] = rev[j], rev[i]
        i += 1
        j -= 1
    print("".join(rev))
reve("hello")
