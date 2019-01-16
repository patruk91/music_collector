import os


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
    albums_indices = [index for index, album_name in enumerate(
        albums_by_name) if album_name == entered_album_name.lower()]
    for index in albums_indices:
        albums_result.append(list_of_albums[index])

    return albums_result


def find_suggestions_by_album_name():
    album_name = view_albums_by_name()
    list_of_albums = read_data_from_file()
    genre_list = album_name[0][3]
    accurate_suggestion = []
    less_suggestion = []

    for album in list_of_albums:
        if album_name[0] == album:
            accurate_suggestion = accurate_suggestion
        elif genre_list == album[3]:
            accurate_suggestion.append(album)
        else:
            if set(genre_list.split()) & set(list(album[3].split())):
                less_suggestion.append(album)
    return accurate_suggestion, less_suggestion


def find_albums_by_artist_name():
    list_of_albums = read_data_from_file()
    artist_names = []
    albums_by_artist_name = []

    for artist in list_of_albums:
        artist_names.append(artist[0])
    entered_name = input("Please enter the artist's name to find: ").lower()
    artist_indices = [index for index, name in enumerate(
        artist_names) if name == entered_name.lower()]

    for index in artist_indices:
        albums_by_artist_name.append(list_of_albums[index])

    return albums_by_artist_name


def find_albums_by_genre():
    list_of_albums = read_data_from_file()
    albums_by_genre = []
    albums_result = []

    for genre in list_of_albums:
        albums_by_genre.append(genre[3])

    entered_music_genre = input("Please enter music genre to find: ").lower()
    genre_indices = [index for index, album_name in enumerate(
        albums_by_genre) if album_name == entered_music_genre.lower()]

    for index in genre_indices:
        albums_result.append(list_of_albums[index])

    return albums_result


def find_shortest_or_longest_album():
    list_of_albums = read_data_from_file()
    albums_by_time = []
    albums_in_seconds = []
    albums_result = []

    for time in list_of_albums:
        albums_by_time.append(time[4])
    for time in albums_by_time:
        m, s = time.split(":")
        albums_in_seconds.append((int(m) * 60 + int(s)))
    time_indices = albums_in_seconds.index(
        min(albums_in_seconds)), albums_in_seconds.index(
        max(albums_in_seconds))

    for index in time_indices:
        albums_result.append(list_of_albums[index])

    return albums_result


'''
def time_from_to():
    from_time = input("Give time from wich I'll search(format 'MM:SS'): ").split(":")
    to_time = input("Give time to wich I'll search(format 'MM:SS'): ").split(":")
    if from_time[0] is None:
        from_time[0] = 0
    if to_time is None:
        to_time = 0
    time_list = from_time + to_time
    time_list = [int(i) for i in time_list]
    print(time_list)
    begin_time_in_sec = time_list[0] * 60 + time_list[1]
    end_time_in_sec = time_list[2] * 60 + time_list[3]
    if begin_time_in_sec > end_time_in_sec:
'''


def save_to_external_file():
    new_file_name = input("Enter desired file name: ")
    with open("text_albums_data.txt", "r") as file_object:
        with open(new_file_name, "w") as new_file_object:
            new_file_object.writelines(file_object)


def add_new_album():
    artist_name = input("Enter artist name: ")
    album_name = input("Enter album name: ")
    release_year = input("Enter release date: ")
    genre_name = input("Enter genre name: ")
    duration = input("Enter duration of album (MM:SS): ")

    with open("text_albums_data.txt", "a") as file_object:
        file_object.write("{},{},{},{},{}\n" .format(
            artist_name, album_name, release_year, genre_name, duration))


def find_between_dates():
    list_of_albums = read_data_from_file()
    release_dates = []
    albums_by_release_date = []

    for date in list_of_albums:
        release_dates.append(date[2])
    release_dates = [int(date) for date in release_dates]
    entered_begin_year = int(input("Please enter date from which to search: "))
    entered_end_year = int(input("Please enter date to which to search: "))

    for year_range in range(entered_begin_year, entered_end_year + 1):
        if year_range in release_dates:
            year_indices = [index for index, year in enumerate(
                release_dates) if year == year_range]

            for index in year_indices:
                albums_by_release_date.append(list_of_albums[index])

    return albums_by_release_date


def find_oldest_or_youngest_album():
    list_of_albums = read_data_from_file()
    albums_by_date = []
    albums_result = []

    for date in list_of_albums:
        albums_by_date.append(date[2])
    albums_by_date = [int(date) for date in albums_by_date]
    date_indices = albums_by_date.index(
        min(albums_by_date)), albums_by_date.index(
        max(albums_by_date))

    for index in date_indices:
        albums_result.append(list_of_albums[index])

    return albums_result


def display_results(list_of_albums, list_of_longest_strings):
    len_of_vertical_lines = 6
    extra_len = 4
    for album in list_of_albums:
        print(
            "-" * sum(list_of_longest_strings)
            + "-" * len_of_vertical_lines
            + "-" * (extra_len * 5))

        print(
            "|{:^{l_n}}|{:^{l_a}}|{:^{l_y}}|{:^{l_g}}|{:^{l_t}}|".format(
                album[0].title(),  # fix with *args?
                album[1].title(),
                album[2].title(),
                album[3].title(),
                album[4].title(),
                l_n=list_of_longest_strings[0] + extra_len,
                l_a=list_of_longest_strings[1] + extra_len,
                l_y=list_of_longest_strings[2] + extra_len,
                l_g=list_of_longest_strings[3] + extra_len,
                l_t=list_of_longest_strings[4] + extra_len, ))
    print("-" * sum(list_of_longest_strings) + "-" *
          len_of_vertical_lines + "-" * (extra_len * 5))


def view_all_albums():
    albums = read_data_from_file()
    longest_strings = longest_strings_in_albums(albums)
    display_results(albums, longest_strings)


def view_albums_by_artist_name():
    artist_name = find_albums_by_artist_name()
    if len(artist_name) == 0:
        print("\nNo such artist in database!")
    else:
        longest_strings = longest_strings_in_albums(artist_name)
        display_results(artist_name, longest_strings)


def view_albums_by_name():
    albums_name = find_albums_by_name()
    CONST = 26
    # CONST due to free spaces, vertical lines, see display function

    if len(albums_name) == 0:
        print("\nNo such artist in database!")
    else:
        longest_strings = longest_strings_in_albums(albums_name)
        print(
            "\n{:^{l_s}}". format(
                "SEARCHED ALBUM",
                l_s=sum(longest_strings) + CONST))
        display_results(albums_name, longest_strings)
    return albums_name


def view_suggestions_by_album_name():
    albums_name = find_suggestions_by_album_name()
    accurate_suggestions = albums_name[0]
    less_suggestions = albums_name[1]
    CONST = 26
    # CONST due to free spaces, vertical lines, see display function

    longest_strings_accurate = longest_strings_in_albums(accurate_suggestions)
    print(
        "\n{:^{l_s}}".format(
            "SIMILAR MUSIC",
            l_s=sum(longest_strings_accurate) + CONST))
    display_results(accurate_suggestions, longest_strings_accurate)

    longest_strings_less = longest_strings_in_albums(less_suggestions)
    print(
        "\n{:^{l_s}}".format(
            "RELATIVELY SIMILAR MUSIC",
            l_s=sum(longest_strings_less) + CONST))
    display_results(less_suggestions, longest_strings_less)


def view_albums_by_genre():
    genre = find_albums_by_genre()
    if len(genre) == 0:
        print("\nNo such music genre in database!")
    else:
        longest_strings = longest_strings_in_albums(genre)
        display_results(genre, longest_strings)


def view_shortest_and_longest_album():
    albums_sl = find_shortest_or_longest_album()
    longest_strings = longest_strings_in_albums(albums_sl)
    display_results(albums_sl, longest_strings)


def view_between_dates():
    albums_by_release = find_between_dates()
    longest_strings = longest_strings_in_albums(albums_by_release)
    display_results(albums_by_release, longest_strings)


def display_statistics_about_albums():
    longest_shortest_album = find_shortest_or_longest_album()
    oldest_youngest_album = find_oldest_or_youngest_album()
    list_of_albums = read_data_from_file()
    genre_stat = genre_statistics()

    print("The shortest album is: {}. Time duration: {}".format(
        longest_shortest_album[0][1].title(), longest_shortest_album[0][4]))
    print("The longest album is: {}. Time duration: {}".format(
        longest_shortest_album[1][1].title(), longest_shortest_album[1][4]))

    print("\nThe oldest album is: {}. Release date: {}".format(
        oldest_youngest_album[0][1].title(), oldest_youngest_album[0][2]))
    print("The youngest album is: {}. Release date: {}".format(
        oldest_youngest_album[1][1].title(), oldest_youngest_album[1][2]))

    print("\nTotal album quantity: {}" .format(len(list_of_albums)))

    print("\nIndividual genres in albums:")
    for genre, quantity in genre_stat.items():
        print("{}: {}" .format(genre.title(), quantity))


def genre_statistics():
    list_of_albums = read_data_from_file()
    genre_list = []
    genre_stat = dict()
    for genre in list_of_albums:
        genre_list.append(genre[3])

    for i in genre_list:
        genre_stat[i] = genre_stat.get(i, 0) + 1

    return genre_stat


def longest_strings_in_albums(list_of_albums):
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
    print("3) Overall statistics")
    print("4) Add new album")
    print("5) Save albums to external file")
    print("9) Exit")

    option = input("Please enter your choice: ")
    return option


def choose_find_option():
    print("1) album by artist name")
    print("2) album by album name")
    print("3) album by genre")
    print("4) shortest and longest album")
    print("5) between dates")
    print("9) Back to previous menu")
    find_option = input("Please enter your choice: ")
    return find_option


def main():
    condition = True
    while condition:
        while True:
            os.system('clear')
            main_option = choose_main_option()
            os.system('clear')

            if main_option == "1":
                view_all_albums()
            elif main_option == "2":
                find_option = choose_find_option()
                os.system('clear')
                if find_option == "1":
                    view_albums_by_artist_name()
                elif find_option == "2":
                    view_suggestions_by_album_name()
                elif find_option == "3":
                    view_albums_by_genre()
                elif find_option == "4":
                    view_shortest_and_longest_album()
                elif find_option == "5":
                    view_between_dates()
                elif find_option == "9":
                    break
                if find_option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print("Error occurred!")
            elif main_option == "3":
                display_statistics_about_albums()
            elif main_option == "4":
                add_new_album()
            elif main_option == "5":
                save_to_external_file()
            elif main_option == "9":
                condition = False
                return condition

            input("\nPress Enter to main menu...\n")

        if condition and find_option != "9":
            break


if __name__ == "__main__":
    main()
