l = []
while True:
    try:
        e = input()
        l.append(e)
    except EOFError:
        break
print(l)