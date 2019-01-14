def read_data_from_file():
    list_of_albums = []
    with open("text_albums_data.txt") as file_object:
        for line in file_object:
            list_of_albums.append(line.rstrip().split(","))
    return list_of_albums


def view_all_albums():
    list_of_albums = read_data_from_file()
    list_of_longest_strings = longest_strings_in_albums()
    len_of_vertical_lines = 6
    extra_len = 4
    for album in list_of_albums:
        print("-" * sum(list_of_longest_strings) + "-" * len_of_vertical_lines + "-" * (extra_len * 5))
        print(
            "|{:^{l_n}}|{:^{l_a}}|{:^{l_y}}|{:^{l_g}}|{:^{l_t}}|" .format(
                album[0],
                album[1],
                album[2],
                album[3],
                album[4],
                l_n=list_of_longest_strings[0] + extra_len,
                l_a=list_of_longest_strings[1] + extra_len,
                l_y=list_of_longest_strings[2] + extra_len,
                l_g=list_of_longest_strings[3] + extra_len,
                l_t=list_of_longest_strings[4] + extra_len,))
    print("-"*sum(list_of_longest_strings) + "-" * len_of_vertical_lines + "-" * (extra_len * 5))

def longest_strings_in_albums():
    list_of_albums = read_data_from_file()
    list_of_longest_strings = []
    for i in range(5):
        longest_string = 0
        for album in list_of_albums:
            if longest_string < len(album[i]):
                longest_string = len(album[i])
        list_of_longest_strings.append(longest_string)
    print(list_of_longest_strings)
    return list_of_longest_strings


def main():
    read_data_from_file()
    view_all_albums()
    longest_strings_in_albums()

if __name__ == "__main__":
    main()
