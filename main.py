"""Command-line entry point for the media tracker."""

from models import Book, Movie, Game


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
        'watched':0,
        'in-progress':0
    }

    #type
    type={
        'book':0,
        'movie':0,
        'game':0
    }
    avg_sum=0
    sum=0
    l=0
    for items in collection:
        if items.status.lower() in status:
            status[items.status.lower()]+=1

        if isinstance(items,Book):
            type['book'] +=1

        elif isinstance(items,Movie):
            type['movie'] +=1

        elif isinstance(items,Game):
            type['game'] +=1
        else :
            pass

        if (items.rating == None):
            pass
        else:
            sum+=items.rating
            l+=1


    if l == 0:
        avg_sum = None
    else:
        avg_sum = sum / l
    stats={
        'status':status,
        'type':type,
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





        


def main():
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

        choice = input('Enter your choice: ')

        match choice:
            case '1':
                add_item(collection)
            case '2':
                view_all(collection)
            case '3':
                search_choice = input('Search by: 1. Title  2. Type  3. Status: ')
                if search_choice == '1':
                    show_results(search_by_title(collection, input('Enter title keyword: ')))
                elif search_choice == '2':
                    show_results(filter_by_type(collection, input('Enter type (book/movie/game): ')))
                elif search_choice == '3':
                    show_results(filter_by_status(collection, input('Enter status: ')))
                else:
                    print('Invalid search option.')
            case '4':
                view_all(collection)
                item_number = int(input('Enter item number: '))
                new_status = input('Enter new status: ')
                update_status(collection, item_number, new_status)
            case '5':
                view_all(collection)
                item_number = int(input('Enter item number: '))
                delete_item(collection, item_number)
            case '6':
                print_stats(collection)
            case '7':
                print('Goodbye! Saving will be added in the JSON phase.')
                break
            case _:
                print('Invalid option.')


if __name__ == '__main__':
    main()
