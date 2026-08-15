"""Media model classes for the media tracker."""

from datetime import date

class Media:
    def __init__(self,title,status='not-started',rating=None,date_added=None):
        self.title=title
        self.status=status
        self.rating=rating
        self.date_added = date_added if date_added is not None else date.today()

    def __str__(self):
        return f'Title : {self.title} \nStatus : {self.status} \nRating : {self.rating} \nDate added : {self.date_added}'

    def __repr__(self):
        return f'Title : {self.title!r} \nStatus : {self.status!r} \nRating : {self.rating!r} \nDate added : {self.date_added}'

    def to_dict(self):
        return{
            'title' : self.title,
            'status' : self.status,
            'rating' : self.rating,
            'date_added': self.date_added.isoformat()
        }
class Book(Media):

    def __init__(self,title,*,status='not-started',rating=None,pages,author,date_added=None):
        super().__init__(title,status,rating,date_added)
        self.pages=pages
        self.author=author

    def __str__(self):   
        return super().__str__() + f'\nPages : {self.pages} \nAuthor : {self.author}'
    
    def __repr__(self):
        return super().__repr__() + f'\nPages : {self.pages!r} \nAuthor : {self.author!r}'

    def to_dict(self):
        data= super().to_dict() 
        data.update({
            'pages' : self.pages,
            'author' : self.author,
            'type' : 'book' 
            })
        return data
            
class Movie(Media):

    def __init__(self,title,*,status='not-started',rating=None,runtime_minutes,director,date_added=None):
          super().__init__(title,status,rating,date_added)
          self.runtime_minutes=runtime_minutes
          self.director=director

    def __str__(self):   
        return super().__str__() + f'\nRun Time Minutes : {self.runtime_minutes} \nDirector : {self.director}'
    
    def __repr__(self):
        return super().__repr__() + f'\nRun Time Minutes : {self.runtime_minutes!r} \nDirector : {self.director!r}'

    def to_dict(self):
        data= super().to_dict() 
        data.update({
            'runtime_minutes' : self.runtime_minutes,
            'director' : self.director,
            'type' : 'movie'
            })
        return data
class Game(Media):

    def __init__(self,title,*,status='not-started',rating=None,hours_played,platform,date_added=None):
          super().__init__(title,status,rating,date_added)
          self.hours_played=hours_played
          self.platform=platform         

    def __str__(self):   
        return super().__str__() + f'\nHours Played : {self.hours_played} \nPlatform : {self.platform}'
    
    def __repr__(self):
        return super().__repr__() + f'\nHours Played : {self.hours_played!r} \nPlatform : {self.platform!r}'
    
    def to_dict(self):
        data= super().to_dict() 
        data.update({
            'hours_played' : self.hours_played,
            'platform' : self.platform,
            'type' : 'game'
            })
        return data