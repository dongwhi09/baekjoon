while True:
    sentence = input()
    if sentence == "EOI":
        break
    print("Found" if "nemo" in sentence.lower() else "Missing")