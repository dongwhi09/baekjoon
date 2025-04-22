while True:
    sentence = input()
    if sentence == "#":
        break
    x = 0
    x += sentence.count("A")
    x += sentence.count("a")
    x += sentence.count("E")
    x += sentence.count("e")
    x += sentence.count("I")
    x += sentence.count("i")
    x += sentence.count("O")
    x += sentence.count("o")
    x += sentence.count("U")
    x += sentence.count("u")
    print(x)