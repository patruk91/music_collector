def read_data_from_file():
    list_of_albums = []
    with open("text_albums_data.txt") as file_object:
        for line in file_object:
            list_of_albums.append(line.lower().rstrip().split(","))
    return list_of_albums


def find_albums_by_name():
    list_of_albums = read_data_from_file()
    albums_by_name = []
    albums_result = []

    for album in list_of_albums:
        albums_by_name.append(album[1])

    entered_album_name = input("Please enter the album name to find: ").lower()
    albums_indices = [index for index, album_name in enumerate(albums_by_name) if album_name == entered_album_name.lower()]
    for index in albums_indices:
        albums_result.append(list_of_albums[index])

    if entered_album_name in albums_by_name:
        return albums_result
    else:
        print("\nNo such album name in database!")


def find_albums_by_artist_name():
    list_of_albums = read_data_from_file()
    artist_names = []
    albums_by_artist_name = []

    for artist in list_of_albums:
        artist_names.append(artist[0])
    entered_name = input("Please enter the artist's name to find: ").lower()
    artist_indices = [index for index, name in enumerate(artist_names) if name == entered_name.lower()]

    for index in artist_indices:
        albums_by_artist_name.append(list_of_albums[index])

    if len(albums_by_artist_name) == 0:
        print("\nNo such artist in database!")
    else:
        return albums_by_artist_name


def view_all_albums():
    list_of_albums = read_data_from_file()
    list_of_longest_strings = longest_strings_in_albums()
    len_of_vertical_lines = 6
    extra_len = 4

    for album in list_of_albums:
        print("-" * sum(list_of_longest_strings) + "-" * len_of_vertical_lines + "-" * (extra_len * 5))
        print(
            "|{:^{l_n}}|{:^{l_a}}|{:^{l_y}}|{:^{l_g}}|{:^{l_t}}|" .format(
                album[0].title(),
                album[1].title(),
                album[2].title(),
                album[3].title(),
                album[4].title(),
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
    return list_of_longest_strings


def choose_main_option():
    print("1) View all albums")
    print("2) Find...")
    print("3) All info...")
    option = input("Please enter your choice: ")
    return option


def choose_find_option():
    print("1) by artist name")
    print("2) by album name")
    find_option = input("Please enter your choice: ")
    return find_option


def main():
    main_option = choose_main_option()
    if main_option == "1":
        view_all_albums()
    elif main_option == "2":
        find_option = choose_find_option()
        if find_option == "1":
            find_albums_by_artist_name()
    elif main_option == "3":
        find_albums_by_name()


if __name__ == "__main__":
    main()
