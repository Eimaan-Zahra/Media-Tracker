"""Media model classes for the media tracker."""

from datetime import date

class Media:
    def __init__(self,title,status='not-started',rating=None):
        self.title=title
        self.status=status
        self.rating=rating
        self.date_added=date.today()

    def __str__(self):
        return f'Title : {self.title} \nStatus : {self.status} \nRating : {self.rating} \nDate added : {self.date_added}'

    def __repr__(self):
        return f'Title : {self.title!r} \nStatus : {self.status!r} \nRating : {self.rating!r} \nDate added : {self.date_added}'
    
class Book(Media):

    def __init__(self,title,*,status='not-started',rating=None,pages,author):
        super().__init__(title,status,rating)
        self.pages=pages
        self.author=author

    def __str__(self):   
        return super().__str__() + f'\nPages : {self.pages} \nAuthor : {self.author}'
    
    def __repr__(self):
        return super().__repr__() + f'\nPages : {self.pages!r} \nAuthor : {self.author!r}'

class Movie(Media):

    def __init__(self,title,*,status='not-started',rating=None,runtime_minutes,director):
          super().__init__(title,status,rating)
          self.runtime_minutes=runtime_minutes
          self.director=director

    def __str__(self):   
        return super().__str__() + f'\nRun Time Minutes : {self.runtime_minutes} \nDirector : {self.director}'
    
    def __repr__(self):
        return super().__repr__() + f'\nRun Time Minutes : {self.runtime_minutes!r} \nDirector : {self.director!r}'
class Game(Media):

    def __init__(self,title,*,status='not-started',rating=None,hours_played,platform):
          super().__init__(title,status,rating)
          self.hours_played=hours_played
          self.platform=platform         

    def __str__(self):   
        return super().__str__() + f'\nHours Played : {self.hours_played} \nPlatform : {self.platform}'
    
    def __repr__(self):
        return super().__repr__() + f'\nHours Played : {self.hours_played!r} \nPlatform : {self.platform!r}'