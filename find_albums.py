import display_functions as dis_fun
import work_with_file as file


def find_albums_by_name():
    """
    Return list with records on searched albums
    """
    list_of_albums = file.read_data_from_file()
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
    """
    Return list of accurate and less suggestions
    found by function based on
    genre and album name.
    """
    album_name = dis_fun.view_albums_by_name()
    if album_name == None:
        return None
    else:

        list_of_albums = file.read_data_from_file()
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
    """
    Return list of albums found by artist name based on
    list of all albums.
    """
    list_of_albums = file.read_data_from_file()
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
    """
    Return list of albums found by genre based on
    list of all albums.
    """
    list_of_albums = file.read_data_from_file()
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
    """
    Return shortest and longest album records based on
    list of all albums.
    """
    list_of_albums = file.read_data_from_file()
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


def find_between_dates():
    """
    Return albums found in release year range based on
    list of albums,
    input(begin year) and
    input(end year).
    """
    list_of_albums = file.read_data_from_file()
    release_dates = []
    albums_by_release_date = []

    for date in list_of_albums:
        release_dates.append(date[2])
    release_dates = [int(date) for date in release_dates]
    while True:
        try:
            entered_begin_year = int(input("Please enter date from which to search: "))
            entered_end_year = int(input("Please enter date to which to search: "))
            break
        except ValueError:
            print("Please provide a correct value!\n")

    for year_range in range(entered_begin_year, entered_end_year + 1):
        if year_range in release_dates:
            year_indices = [index for index, year in enumerate(
                release_dates) if year == year_range]

            for index in year_indices:
                albums_by_release_date.append(list_of_albums[index])

    return albums_by_release_date


def find_oldest_or_youngest_album():
    """
    Return oldest and youngest album based on
    list of all albums
    """
    list_of_albums = file.read_data_from_file()
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
