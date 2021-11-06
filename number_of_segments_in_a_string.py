def countsegments(s):
    ans = s.split()
    return len(ans)


if __name__ == "__main__":
    print(countsegments("Hello, my name is John"))
    print(countsegments("Hello"))
    print(countsegments("love live! mu'sic forever"))
    print(countsegments(""))
