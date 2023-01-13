import random
import string

def generate_random_string(length):
    letters = string.ascii_letters.lower()
    return ''.join(random.choice(letters) for i in range(length))


def encoding(str):
    words = str.split(" ")
    coding = True
    new_str = []
    if (coding):
        for word in words:
            if (len(word) >= 3):
                r1 = generate_random_string(3)
                r2 = generate_random_string(3)
                str_new = r1 + word[1:] + word[0] + r2
                new_str.append(str_new)
            else:
                str_new = word[::-1]
                new_str.append(str_new)
        new_str = " ".join(new_str)
    return new_str


def decoding(str):
    words = str.split(" ")
    coding = True
    new_str = []
    if (coding):
        for word in words:
            if (len(word) >= 3):
                str_new = word[3:-3]
                str_new = str_new[-1] + str_new[:-1]
                new_str.append(str_new)
            else:
                str_new = word[::-1]
                new_str.append(str_new)
        new_str = " ".join(new_str)
    return new_str







if __name__ == "__main__":

    str1 = "Varaliya is Mohammed"
    a = encoding(str1)
    print(a)

    str2 = "dkxaraliyaVzcb si zkdohammedMgsv"
    b = decoding(str2)
    print(b)