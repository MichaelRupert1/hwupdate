'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
class Movie():
    def __init__(self,year, title,quote):
        self.year = year
        self.title = title
        self.quote = quote

    def famousquote(self):
        return f'{self.quote}'

    def __str__(self):
        return f'The movie \'{self.title}\' was made in the year {self.year}.'

class RomCom(Movie):
    def __init__(self,year, title,quote,pg=13):
        super().__init__(year, title, quote)
        self.pg = pg

    def __str__(self):
        return f'The movie \'{self.title}\'was made in the year {self.year} and is PG:{self.pg}.'
        
pf = Movie(1994,'Pulp Fiction', R"(Samuel Leroy Jackson)~Jules~ 'There's a passage I got memorized'.Ezekiel 25:17. The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers. And you will know I am the Lord when I lay My vengeance upon you.' Now... I been sayin' that shit for years. And if you ever heard it, that meant your ass. You'd be dead right now. I never gave much thought to what it meant. I just thought it was a cold-blooded thing to say to a motherfucker before I popped a cap in his ass. But I saw some shit this mornin' made me think twice. See, now I'm thinking: maybe it means you're the evil man. And I'm the righteous man. And Mr. 9mm here... he's the shepherd protecting my righteous ass in the valley of darkness. Or it could mean you're the righteous man and I'm the shepherd and it's the world that's evil and selfish. And I'd like that. But that shit ain't the truth. The truth is you're the weak. And I'm the tyranny of evil men. But I'm tryin', Ringo. I'm tryin' real hard to be the shepherd.'")
print(pf.famousquote())
print(pf.__str__())
print()
gd = RomCom(1993,'Groundhog Day',R"(Bill_Murray)~Phil Connors~ It's the same thing every day, Clean up your room, stand up straight, pick up your feet, take it like a man, be nice to your sister, don't mix beer and wine ever, Oh yeah, don't drive on the railroad tracks")
print(gd.famousquote())
print(gd.__str__())