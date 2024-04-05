# Displaying the main menu of the Movie Library Management System
print("""
|=====Movie Library Management System======[-][o][x]
|           M O V I E   M  E  N  U                 | 
|   1- Add Movie                                   | 
|   2- Edit Movie                                  | 
|   3- View Collection                             | 
|   4- Delete Movie                                | 
|   5- Exit                                        | 
|               version 1.02                       |       
|           copyright@vit4 group2                  |
|==================================================| 
""")

# Dictionary to store movie data
movie_collection = {}

# Function to add a movie to the collection
def add_movie():
    movie_name = input("Enter the Movie Name:")
    director = input("Enter the Director:")
    release_year = input("Enter the Release Year:")
    genre = input("Enter the Genre :")

    # Creating a dictionary to store movie details
    movie_dictionary = {
        "Movie": movie_name,
        "Director": director,
        "Release Year": release_year,
        "Genre": genre
    }

    # Adding movie to the collection
    movie_collection[movie_name] = movie_dictionary

    print(f"({movie_name}) added to the collection")

# Function to edit movie details
def edit_movie(movie_name):
    if movie_name in movie_collection:
        print(f"Editing {movie_name}...")
        new_data = {}
        # Updating movie details
        new_data['Movie'] = input(f"Enter a new movie({ movie_collection[movie_name]['Movie']}):")
        new_data['Director'] = input(f"Enter a New Director ({movie_collection[movie_name]['Director']}):")
        new_data['Release Year'] = input(f"Enter a New Release Year ({movie_collection[movie_name]['Release Year']}):")
        new_data['Genre'] = input(f"Enter a New Genre ({movie_collection[movie_name]['Genre']}):")

        movie_collection[movie_name] = new_data
        print(f"({new_data}) updated")
    else:
        print(f"({movie_name}) not found in the collection.")

# Function to view the movie collection
def view_collection():
    print("\nMovie Collection:")
    for movie_name, data in movie_collection.items():
        print(f"Movie Name: {data['Movie']}")
        print(f"Director: {data['Director']}")
        print(f"Release Year: {data['Release Year']}")
        print(f"Genre: {data['Genre']}")
        print("-" * 30)

# Function to delete a movie from the collection
def delete_movie(movie_name):
    if movie_name in movie_collection:
        del movie_collection[movie_name]
        print(f"{movie_name} deleted from the collection.")
    else:
        print(f"{movie_name} not found in the collection.")

# Function to save movie data to a JSON file
import json

def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(movie_collection, file)

# Function to load movie data from a JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Main function to run the program
def main():
    global movie_collection
    # Loading movie data from file
    movie_collection = load_data('movie_data.json')

    while True:
        # Displaying the menu and asking for user input
        menu_choose = input("Please choose a number: ")
        print('=' * 51)

        # Performing actions based on user input
        if menu_choose == "1":
            add_movie()
            print('=' * 51)

        elif menu_choose == "2":
            movie_name = input("Enter the film name to edit: ")
            edit_movie(movie_name)
            print('=' * 51)

        elif menu_choose == "3":
            view_collection()
            print('=' * 51)

        elif menu_choose == "4":
            movie_name = input("Enter the Movie name to delete: ")
            delete_movie(movie_name)
            print('=' * 51)

        elif menu_choose == "5":
            # Saving data and exiting the program
            save_data('movie_data.json')
            print("Exiting the program")
            print('=' * 51)
            break

        else:
            print("Invalid option! Please try again.")
            print('=' * 51)

if __name__ == "__main__":
    main()