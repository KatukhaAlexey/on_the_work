def backward_string_by_word(text: str) -> str:
    list_of_text = text.split(' ')
    new_text = ''
    len_of_list = len(list_of_text)
    if list_of_text[0] != '':
        new_text = f' {str(reversed(list_of_text[0]))}'
    else:
        for i in list_of_text[1:len_of_list - 1]:
            if i != '':
                new_text = f' {str(reversed(i))}'
            else:
                new_text = f' {i}'
    return str(new_text)

print(backward_string_by_word(""))
print(backward_string_by_word("world"))
print(backward_string_by_word("hello world"))
print(backward_string_by_word("hello   world"))
print(backward_string_by_word("welcome to a game"))
