

if __name__ == "__main__":

    l = []
    while True:
        try:
            e = input()
            l.append(e)
        except EOFError:
            break
    l = list(map(int, l))
    print(l)
