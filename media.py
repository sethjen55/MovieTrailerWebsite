import webbrowser

class Movie():
        """This Class is set up to be able to store Movie related information."""
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_directors, movie_rating, movie_actors):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
            
            """added option to add Direcor, Writer and Actor info"""
            self.directors = movie_directors
            self.rating = movie_rating
            self.actors = movie_actors

        def show_trailer(self):
            webbrowser.open(self.trailer_url)
