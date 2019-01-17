import work_with_file as file
import find_albums as find_a


def longest_strings_in_albums(list_of_albums):
    """
    Search for longest string for each column
    and returns length of it.
    :param list_of_albums: list of used albums
    :return: list of len(longest strings)
    """
    list_of_longest_strings = []

    for i in range(5):
        longest_string = 0
        for album in list_of_albums:
            if longest_string < len(album[i]):
                longest_string = len(album[i])
        list_of_longest_strings.append(longest_string)
    return list_of_longest_strings


def display_results(list_of_albums, list_of_longest_strings):
    """
    Print table with records from list of used albums.
    :param: list_of_albums: list of used albums
    :param: list_of_longest_strings: length of strings of each column
    """
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
    """
    Call display_resultss with them based on all albums records and
    their string lengths.
    """
    albums = file.read_data_from_file()
    longest_strings = longest_strings_in_albums(albums)
    display_results(albums, longest_strings)


def view_albums_by_artist_name():
    """
    Call display results based on artist name and
    their string lengths.
    """
    artist_name = find_a.find_albums_by_artist_name()
    if len(artist_name) == 0:
        print("\nNo such artist in database!")
    else:
        longest_strings = longest_strings_in_albums(artist_name)
        display_results(artist_name, longest_strings)


def view_albums_by_name():
    """
    Searches for album by name,
    prints this album in table with title and
    returns it/them.
    """
    albums_name = find_a.find_albums_by_name()
    CONST = 26
    # CONST due to free spaces, vertical lines, see display function

    if len(albums_name) == 0:
        return None
    else:
        longest_strings = longest_strings_in_albums(albums_name)
        print(
            "\n{:^{l_s}}". format(
                "SEARCHED ALBUM",
                l_s=sum(longest_strings) + CONST))
        display_results(albums_name, longest_strings)
    return albums_name


def view_suggestions_by_album_name():
    """
    Take accurate and less accurate suggestions from
    first and second alubum_name elements.
    Calculate longest strings from those variables separelty,
    prints tables based on lengths and
    fills them with display results function call.
    """
    albums_name = find_a.find_suggestions_by_album_name()
    if albums_name == None:
        print("\nNo such album in database!")
    else:
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
    """
    Call display results based on albums with searched genre and
    their string lengths.
    """
    genre = find_a.find_albums_by_genre()
    if len(genre) == 0:
        print("\nNo such music genre in database!")
    else:
        longest_strings = longest_strings_in_albums(genre)
        display_results(genre, longest_strings)


def view_shortest_and_longest_album():
    """
    Call display results based on shortest and longest album and
    their string lenghts.
    """
    albums_sl = find_a.find_shortest_or_longest_album()
    longest_strings = longest_strings_in_albums(albums_sl)
    display_results(albums_sl, longest_strings)


def view_between_dates():
    """
    Call display results based on albums released between some dates and
    their string lenghts.
    """
    albums_by_release = find_a.find_between_dates()
    longest_strings = longest_strings_in_albums(albums_by_release)
    display_results(albums_by_release, longest_strings)


def display_statistics_about_albums():
    """
    Prints statistiscs of all records in file based on
    longest and shortest album,
    oldest and youngest album,
    number of albums in file and
    number of albums of each genre.
    """
    longest_shortest_album = find_a.find_shortest_or_longest_album()
    oldest_youngest_album = find_a.find_oldest_or_youngest_album()
    list_of_albums = file.read_data_from_file()
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
    """
    Return number albums of each genre.
    """
    list_of_albums = file.read_data_from_file()
    genre_list = []
    genre_stat = dict()
    for genre in list_of_albums:
        genre_list.append(genre[3])

    for i in genre_list:
        genre_stat[i] = genre_stat.get(i, 0) + 1

    return genre_stat
