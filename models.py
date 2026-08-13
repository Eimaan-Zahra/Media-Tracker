"""Media model classes for the media tracker."""

from datetime import date

class Media:
    def __init__(self,title,status='Not started',rating=None):
        self.title=title
        self.status=status
        self.rating=rating
        self.date=date.today()

    def __str__(self):
        return f'Title : {self.title} \nStatus : {self.status} \nRating : {self.rating} \nDate added : {self.date}'

    def __rep__(self):
            return f'Title : {self.title!r} \nStatus : {self.status!r} \nRating : {self.rating!r} \nDate added : {self.date}'


    