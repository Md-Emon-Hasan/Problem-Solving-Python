def solve(s):

    words = s.split(" ")
    result = []

    for w in words:
        if w:
            result.append(w[0].upper() + w[1:])
        else:
            result.append(w)

    return " ".join(result)


if __name__ == '__main__':
    s = input()
    print(solve(s))