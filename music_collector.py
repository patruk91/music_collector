

def read_data_from_file():
    list_of_albums = []
    with open("text_albums_data.txt") as file_object:
        for line in file_object:
            list_of_albums.append(line.lower().rstrip().split(","))
    return list_of_albums


def find_album_by_name():
    list_of_albums = read_data_from_file()
    album_names = []
    for album in list_of_albums:
        album_names.append(album[1])
    print(album_names)
    given_name = input("Give name of the album: ").lower()
    if given_name in album_names:
        return (list_of_albums[album_names.index(given_name)])
    else:
        print("\nNo such album name in database!")


def find_album_by_artist_name():
    list_of_albums = read_data_from_file()
    artist_names = []
    for album in list_of_albums:
        artist_names.append(album[0])
    print(artist_names)
    given_name = input("Give name of the artist: ").lower()
    indices = [i for i, x in enumerate(artist_names) if x == given_name.lower()]
    for index in indices:
        print(list_of_albums[index])


def main():
    read_data_from_file()
    # find_album_by_name()
    find_album_by_artist_name()


if __name__ == "__main__":
    main()
