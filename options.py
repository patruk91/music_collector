def choose_main_option():
    print("1) View all albums")
    print("2) Find...")
    print("3) Overall statistics")
    print("4) Add new album")
    print("5) Edit album in database")
    print("6) Save albums to external file")
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
