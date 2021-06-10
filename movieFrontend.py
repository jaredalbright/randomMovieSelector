import movieBackend
import re
from tkinter import *

global movie_info

def generate():
    genre = decision.get()
    rating = slider.get()
    movie = movieBackend.movieGen(genre,rating)

    movie_info = movie.get_movie()

    disp.config(state=NORMAL)
    disp.delete(1.0,END) #deletes the text from the display
    movie_string = 'Title: ' + movie_info['movie']
    disp.insert(END,movie_string)
    rating_string = '\nAverage Rating: ' + str(movie_info['votes'])
    disp.insert(END,rating_string)
    disp.config(state=DISABLED) #closes the display to editing again



#creates password creation window
window = Tk()
window.title('Random Movie Selector')

#creates list for drop down menu
decision = StringVar(window)
choices = ['Action', 'Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Horror', 'Music','Mystery','Romance','Science Fiction','TV Movie','Thriller','War','Western',]
decision.set('Action') #sets word as the first option

#creates option menu for password selection
drop = OptionMenu(window,decision,*choices)
Label(window,text="Choose Type").pack()
drop.pack()

#creates scale for rating
slider = Scale(window, from_=0.0, to=10.0, orient = HORIZONTAL, resolution = 0.1,  label = "Choose Minimum Rating")
#Label(window,text="Choose Rating").grid(row = 1, column =2)
slider.pack()

#creates original search
find = Button(window, text='Find Movie', command = generate)
find.pack()

disp = Text(window, height = 2, width = 40)    
disp.insert(END,"Title:\nAverage Rating:")
disp.config(state=DISABLED)
disp.pack()


#keeps the window open
window.mainloop()