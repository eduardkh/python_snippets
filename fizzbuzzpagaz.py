def fizzbuzzpagaz(max):
    for i in range(1, max+1):
        # print(f" > i is: {i}")  # for debug
        output = ""
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            output = i
        if i % 7 == 0:
            output = f"pagaz{output}"
        if i % 5 == 0:
            output = f"buzz{output}"
        if i % 3 == 0:
            output = f"fizz{output}"
        print(output)


fizzbuzzpagaz(100)
