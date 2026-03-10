def merge_the_tools(string, k):

    for i in range(0, len(string), k):
        part = string[i:i+k]

        seen = set()
        result = ""

        for ch in part:
            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)


if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s, k)