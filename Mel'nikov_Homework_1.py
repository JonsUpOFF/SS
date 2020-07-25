for i in range(1, 101):
    fizz = ""
    buzz = ""
    if i % 3 == 0:
        fizz = "Fizz"
    if i % 5 == 0:
        buzz = "Buzz"
    if fizz != "Fizz" and buzz != "Buzz":
        print(i)
    else:
        print(fizz + buzz)