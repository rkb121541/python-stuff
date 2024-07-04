import os

def main():
    dict = {}
    read_file = open("./dictionary.txt", "r")
    list_of_lines = []
    for line in read_file:
        list_of_lines += [line]
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].rsplit('\n')[0]
        list_of_lines[i] = list_of_lines[i].lower()
    for word in list_of_lines:
        mid = {}
        for letter in word:
            if letter not in mid:
                mid[letter] = 1
            else:
                mid[letter] += 1
        dict[word] = mid
    
    user_input = input("Enter some letters: ")
    user_input = user_input.lower()
    user_dict = {}
    for letter in user_input:
        if letter not in user_dict:
            user_dict[letter] = 1
        else:
            user_dict[letter] += 1

    print("Here are a list of words that you can make with the letters you provided:")
    result_words = []
    for item in dict.items():
        if item[1] == user_dict:
            result_words += [item[0]]
    print(result_words)

if __name__ == "__main__":
    main()
