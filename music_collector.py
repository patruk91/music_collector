import os


import options
import display_functions as dis_fun
import work_with_file as file


def main():
    condition = True
    while condition:
        while True:
            os.system('clear')
            main_option = options.choose_main_option()
            os.system('clear')

            if main_option == "1":
                dis_fun.view_all_albums()
            elif main_option == "2":
                find_option = options.choose_find_option()
                os.system('clear')
                if find_option == "1":
                    dis_fun.view_albums_by_artist_name()
                elif find_option == "2":
                    dis_fun.view_suggestions_by_album_name()
                elif find_option == "3":
                    dis_fun.view_albums_by_genre()
                elif find_option == "4":
                    dis_fun.view_shortest_and_longest_album()
                elif find_option == "5":
                    dis_fun.view_between_dates()
                elif find_option == "9":
                    break
                if find_option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print("Error occurred!")
            elif main_option == "3":
                dis_fun.display_statistics_about_albums()
            elif main_option == "4":
                file.add_new_album()
            elif main_option == "5":
                file.edit_file()
            elif main_option == "6":
                file.save_to_external_file()
            elif main_option == "9":
                condition = False
                return condition
            input("\nPress Enter to main menu...\n")

        if condition and find_option != "9":
            break


if __name__ == "__main__":
    main()
