
def read_data_from_file():
    list_of_albums = []
    with open("text_albums_data.txt") as file_object:
        for line in file_object:
            list_of_albums.append(line.rstrip().split(","))
    return list_of_albums


def main():
    read_data_from_file()


if __name__ == "__main__":
    main()
