
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key:{k}, value:{v}")
    return None

a = {"one": 1, "two": 2}
print(a)
# print_dict(a)
return_value = print_dict(a)
print(return_value)

def get_first_last_word(text):
    words = text.split()
    print(words)
    return words[0], words[-1]

text = "Hello, My name is Mike"
first, last = get_first_last_word(text)
print(f"first:{first}, last:{last}")