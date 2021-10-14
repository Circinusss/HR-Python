if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    mi = -999
    for i in a:
        if i>mi and i<m:
            mi = i
    print(mi)
