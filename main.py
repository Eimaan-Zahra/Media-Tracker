"""Command-line entry point for the media tracker."""
from datetime import date
from models import Book, Movie, Game
import json

DATA_FILE="media.json"

def get_integer(value):
    while True:
        try:
            return int(input(value))
        except ValueError:
            print('Please enter a valid number.')


def get_float(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print('Please enter a valid number.')


Status=['finished','not-started','in-progress']
def select_status():
    while True:
        print('Select status:')
        for i, s in enumerate(Status, start=1):
            print(f'{i}-{s}')

        while True:
            try:
                choice = int(input('Enter your choice: '))
                break
            except ValueError:
                print('Please enter a valid number.')
        
        if (choice <= 0) or (choice > len(Status)):
            print('.\n.\n.\ninvalid choice (1-3)........try again \n.\n.\n.')
            continue
        else:
            break

    return Status[choice-1]


'''Get a rating from 0 to 5.'''
def get_rating():
    while True:

        try:
            rating = float(input('Rating (0-5): '))
        except ValueError:
            print('Please enter a valid number.')
            continue

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

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Please enter a valid number.')
            continue
    
        #selection
        if (choice <= 0) or (choice>3):
            print('.\n.\n.\ninvalid choice (1-3)........try again \n.\n.\n.')
            continue
        else:
            break

    match choice:
        case 1:
            divider = '-' * 4
            print(f'{divider} Book Data Entry {divider}')
            book_name=input(f'Name: ')
            status=select_status()
            pages = get_integer('Pages: ')
            author=input(f'Author: ')
            rating=get_rating()
            collection.append(Book(book_name,status=status,rating=rating,pages=pages,author=author))
            print('\n\n')

            
        case 2:
            divider = '-' * 4
            print(f'{divider} Movie Data Entry {divider}')
            movie_name=input(f'Name: ')
            status=select_status()
            rating=get_rating()
            runtime_minutes = get_integer('Run-Time-Minutes: ')
            director=input(f'director: ')
            collection.append(Movie(movie_name,status=status,rating=rating,runtime_minutes=runtime_minutes,director=director))
            print('\n\n')

        case 3:
            divider = '-' * 4
            print(f'{divider} Game Data Entry {divider}')
            game_name=input(f'Name: ')
            status=select_status()
            rating=get_rating()
            hours_played = get_float('Hours Played: ')
            platform=input(f'Platform: ')
            collection.append(Game(game_name,status=status,rating=rating,hours_played=hours_played,platform=platform))
            print('\n\n')

'''view all->allows the user to veiw all collection and if list is empty'''
def view_all(collection):
    if collection == []:
        print(f" \n...No items yet...\n\n")
    else:
        for number, item in enumerate(collection, start=1):
            print(f'{number}. {item.title} - {item.status}')


def update_status(collection, item_number, new_status):
    index = item_number - 1

    if index < 0 or index >= len(collection):
        print('Invalid item number.')
        return

    collection[index].status = new_status
    print(f'Updated "{collection[index].title}" to {new_status}.')


def delete_item(collection, item_number):
    index = item_number - 1
    if index < 0 or index >= len(collection):
        print('Invalid item number.')
        return

    deleted_item = collection.pop(index)
    print(f'Deleted "{deleted_item.title}".')


'''search-by : to serach a tittle in the collection itmes'''
def search_by_title(collection,keyword):
    c=list(filter(lambda item:keyword.lower() in item.title.lower() ,collection ))
    # c=[keyword.lower() in item.lower()]
    return c


def filter_by_type(collection, media_type):
    media_classes = {
        'book': Book,
        'movie': Movie,
        'game': Game,
    }
    requested_class = media_classes.get(media_type.lower())

    if requested_class is None:
        return []

    return [item for item in collection if isinstance(item, requested_class)]


def filter_by_status(collection, status):
    return [item for item in collection if item.status.lower() == status.lower()]


def show_results(results):
    if not results:
        print('No matching items found.')
        return

    for item in results:
        print(item)
        print('-' * 25)

def show_stats(collection):
    if collection == []:
        print(f'collection is empty\n')
        return

    #first-stats on status
    status={
        'finished':0,
        'not-started':0,
        'in-progress':0
    }

    #type
    media_type={
        'book':0,
        'movie':0,
        'game':0
    }
    avg_sum=0
    rating_sum=0
    l=0
    for items in collection:
        if items.status.lower() in status:
            status[items.status.lower()]+=1

        if isinstance(items,Book):
            media_type['book'] +=1

        elif isinstance(items,Movie):
            media_type['movie'] +=1

        elif isinstance(items,Game):
            media_type['game'] +=1
        else :
            pass

        if (items.rating == None):
            pass
        else:
            rating_sum+=items.rating
            l+=1


    if l == 0:
        avg_sum = None
    else:
        avg_sum = rating_sum / l
    stats={
        'status':status,
        'type':media_type,
        'average rating':avg_sum
    }

    return stats


def print_stats(collection):
    stats = show_stats(collection)
    if stats is None:
        return

    print('\nItems by status:')
    for status, count in stats['status'].items():
        print(f'{status}: {count}')

    print('\nItems by type:')
    for media_type, count in stats['type'].items():
        print(f'{media_type}: {count}')

    if stats['average rating'] is None:
        print('\nAverage rating: No ratings yet')
    else:
        print(f"\nAverage rating: {stats['average rating']:.1f}")


def save_collection(collection,filename): #dict->json
    data=[]

    for items in collection:
        data.append(items.to_dict())

    with open(filename,"w") as file:
        json.dump(data,file,indent=4)


def rebuild_item(data): #jason->dict
    date_added=date.fromisoformat(data['date_added'])

    if data['type'] == 'book':
        return Book(data['title'],status=data['status'],rating=data['rating'],pages=data['pages'],author=data['author'],date_added=date_added)
    
    elif data['type'] == 'movie':
        return Movie(data['title'],status=data['status'],rating=data['rating'],runtime_minutes=data['runtime_minutes'],director=data['director'],date_added=date_added)
    
    elif data['type'] == 'game':
        return Game(data['title'],status=data['status'],rating=data['rating'],hours_played=data['hours_played'],platform=data['platform'],date_added=date_added)

    else:
        raise ValueError(f"Unknown media type in saved data: {data['type']!r}")


    
def load_data(filename): #jason->dict
    with open(filename,"r") as file:
        data=json.load(file)

    collection=[]

    for item in data:
        collection.append(rebuild_item(item))

    return collection


def main():
    try:
        collection = load_data(DATA_FILE)

    except FileNotFoundError:
        collection=[]

    except json.JSONDecodeError:
        print("Saved data is corrupted. Starting with an empty collection.")
        collection = []


    while True:
        print('\n--- Media Tracker ---')
        print('1. Add item')
        print('2. View all')
        print('3. Search or filter')
        print('4. Update status')
        print('5. Delete item')
        print('6. Stats')
        print('7. Save and exit')

        choice=None
        while True:
            try:
                choice = int(input('Enter your choice: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        match choice:
            case 1:
                add_item(collection)
            case 2:
                view_all(collection)
            case 3:
                search_choice = input('Search by: 1. Title  2. Type  3. Status: ')
                if search_choice == '1':
                    show_results(search_by_title(collection, input('Enter title keyword: ')))
                elif search_choice == '2':
                    show_results(filter_by_type(collection, input('Enter type (book/movie/game): ')))
                elif search_choice == '3':
                    show_results(filter_by_status(collection, input('Enter status: ')))
                else:
                    print('Invalid search option.')
            case 4:
                view_all(collection)
                while(True):
                    
                    try:
                        item_number = int(input('Enter item number: '))
                    except ValueError:
                        print('Please enter a valid number.')
                        continue


                    index=item_number-1
                    if index < 0 or index >= len(collection):
                        print('Invalid item number...try again...\n')
                        continue
                    else:
                        break
                new_status = select_status()
                update_status(collection, item_number, new_status)
            case 5:
                view_all(collection)
                while True:
                    try:
                        item_number = int(input('Enter item number: '))
                        break
                    except ValueError:
                         print('Please enter a valid number.')
                delete_item(collection, item_number)
            case 6:
                print_stats(collection)
            case 7:
                try:
                    save_collection(collection,DATA_FILE)
                    print('Collection saved successfully. Goodbye! :) ')
                    break
                except OSError:
                    print('Could not save collection')
            case _:
                print('Invalid option.')


if __name__ == '__main__':
    main()