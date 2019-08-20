# =================================to remove duplicate from a string and return sorted one ===================
def test123(var1):
    b = set(var1)
    return ''.join(b)


if __name__ == "__main__":
    a = 'sankalppp'
    print(test123(a))
    print(set(a))
