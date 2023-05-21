def permute (string, posket=""):
    if len(string) == 0:
        print(posket)

    else:
        for i in range(len(string)):
            letter = string[i]
            front_l = string[0:i]
            back_l = string[i+1:]
            together = front_l + back_l
            permute(together, letter + posket)

print(permute("AGC", ""))

