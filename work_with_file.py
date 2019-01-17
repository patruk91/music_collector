import find_albums as find_a


def read_data_from_file():
    """
    Open file fill list of album with data form file and
    return it
    """
    list_of_albums = []
    with open("text_albums_data.txt") as file_object:
        for line in file_object:
            list_of_albums.append(line.lower().rstrip().split(","))
    return list_of_albums


def save_to_external_file():
    """
    Open file and create new file based on
    user input and
    writelines to new file
    """
    new_file_name = input("Enter desired file name: ")
    with open("text_albums_data.txt", "r") as file_object:
        with open(new_file_name, "w") as new_file_object:
            new_file_object.writelines(file_object)


def edit_file():
    """
    Find album by name and if there is more than one album,
    ask about artist name.
    Print options which record user wants to edit.
    Ask user for input and change.
    Overwrites file.
    """
    list_of_albums = read_data_from_file()
    album_result = find_a.find_albums_by_name()
    if album_result != []:
        if len(album_result) > 1:
            artist_name = input("Please give me artist name: ")
            for i in album_result:
                if artist_name in i:
                    album_result = []
                    album_result.append(i)
        album_result = album_result[0]
        index = list_of_albums.index(album_result)
        print("What would you like to change? ")
        print("1) Change artist name")
        print("2) Change album name")
        print("3) Change release year")
        print("4) Change genre name")
        print("5) Change duration")
        entered_option = input("Please enter your choice: ")
        entered_change = input("Please enter your change: ")
        if entered_option == "1":
            fool_proof_for_edit_file(entered_change)
            album_result[0] = entered_change

        elif entered_option == "2":
            fool_proof_for_edit_file(entered_change)
            album_result[1] = entered_change

        elif entered_option == "3":
            while True:
                try:
                    int(entered_change)
                    break
                except ValueError:
                    print("\nProvide correct value!")
                entered_change = input("Please enter your change: ")
            album_result[2] = entered_change

        elif entered_option == "4":
            fool_proof_for_edit_file(entered_change)
            album_result[3] = entered_change

        elif entered_option == "5":
            while True:
                try:
                    values = entered_change.split(":")
                    if len(values) == 2 and len(values[1]) == 2 and int(values[1]) <= 60:
                        [int(i) for i in values]
                        break
                except ValueError or IndexError:
                    print("\nProvide value in (MM:SS)")

                entered_change = input("Please enter your change in (MM:SS): ")
            album_result[4] = entered_change

        list_of_albums[index] = album_result
        overwrite_file(list_of_albums)
    else:
        print("\nNo such album in database!")


def fool_proof_for_edit_file(entered_change):
    """
    Special function for blank user input which
    prevents them.
    """
    while True:
        if entered_change is not "":
            break
        entered_change = input("Please enter your change: ")
    return entered_change


def overwrite_file(list_of_albums):
    """
    Open file and overwrites it with changes done.
    """
    with open("text_albums_data.txt", "w") as file_object:
        for album in list_of_albums:
            file_object.write(",".join(album))
            file_object.write("\n")


def add_new_album():
    """
    Add new album record and appends it to file.
    """
    while True:
        artist_name = input("Enter artist name: ")
        if artist_name is not "":
            break

    while True:
        album_name = input("Enter album name: ")
        if album_name is not "":
            break

    while True:
        release_year = input("Enter release date: ")
        try:
            int(release_year)
            break
        except ValueError:
            print("\nProvide correct value!")

    while True:
        genre_name = input("Enter genre name: ")
        if release_year is not "":
            break

    while True:
        duration = input("Enter duration of album (MM:SS): ")
        try:
            values = duration.split(":")
            if len(values) == 2 and len(values[1]) == 2 and int(values[1]) <= 60:

                [int(i) for i in values]

                break
        except ValueError or IndexError:
            print("\nProvide value in (MM:SS)")

    with open("text_albums_data.txt", "a") as file_object:
        file_object.write("{},{},{},{},{}\n" .format(
            artist_name, album_name, release_year, genre_name, duration))
