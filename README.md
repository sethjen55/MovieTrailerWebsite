# MovieTrailerWebsite
### Project 1 for Full-Stack Nanodegree

This project is to show off some of my favorite movies.

First is the media.py file which is the class file that creates the Movie objects and their structure.
  - This file imports webbrowser for access to the browser function to open a browser window.

Next is the entertainment_center.py file which calls Movie class and passes it all the necesary trait information to create
the Movie objects for each movie passed to it.
  - This file imports media to access the class Movie() to define the movie content passed and the show_trailer function.
  - This file imports fresh_tomatoes to render the movie list to an html page.
  
Finally is the fresh_tomatoes.py file which builds the html file, fresh_tomatoes.html, of the movie content and displays the
webpage.
