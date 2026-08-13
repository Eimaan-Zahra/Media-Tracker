"""Command-line entry point for the media tracker."""

from models import Book, Movie, Game

collection=[]

'''Get a rating from 0 to 5.'''
def get_rating():
    while True:
        rating = float(input('Rating (0-5): '))
        if rating < 0 or rating > 5:
            print('Rating must be between 0 and 5. Try again.')
            continue
        return rating


'''ADD Items -> function for collection of data from user'''
def add_item(collection):
    choice=0
    while(True):
        print("Please select your media type:")
        print(f"1-Book \n2-Movie \n3-Game")
        choice=int(input('Enter your choice: '))
    
        #selection
        if (choice <= 0) or (choice>3):
            print('.\n.\n.\ninvalid choice (1-3)........try again \n.\n.\n.')
            continue
        else:
            break

    match choice:
        case 1:
            print(f'{'-'*4} Book Data Entry {'-'*4}')
            book_name=input(f'Name: ')
            status=input(f'Status (finished,in-progress,): ')
            rating=get_rating()
            pages=int(input(f'Pages: '))
            author=input(f'Author: ')
            collection.append(Book(book_name,status=status,rating=rating,pages=pages,author=author))
            print('\n\n')

            
        case 2:
            print(f'{'-'*4} Movie Data Entry {'-'*4}')
            movie_name=input(f'Name: ')
            status=input(f'Status (finished, in-progress): ')
            rating=get_rating()
            runtime_minutes=int(input(f'Run-Time-Minutes: '))
            director=input(f'director: ')
            collection.append(Movie(movie_name,status=status,rating=rating,runtime_minutes=runtime_minutes,director=director))
            print('\n\n')

        case 3:
            print(f'{'-'*4} Game Data Entry {'-'*4}')
            game_name=input(f'Name: ')
            status=input(f'Status (finished,in-progress,): ')
            rating=get_rating()
            hours_played=float(input(f'Hours Played: '))
            platform=input(f'Platform: ')
            collection.append(Game(game_name,status=status,rating=rating,hours_played=hours_played,platform=platform))
            print('\n\n')

'''view all->allows the user to veiw all collection and if list is empty'''
def view_all(collection):
    if collection == []:
        print(f" \n...No items yet...\n\n")
    else:
        for info in collection:
            print(info)
#main
view_all(collection)
add_item(collection)
add_item(collection)
view_all(collection)
