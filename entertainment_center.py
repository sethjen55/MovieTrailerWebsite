import fresh_tomatoes
import media

# Builds the instance for each class Movie
# Passes (Movie title, Movie Description, Movie Poster image, YouTube location of each trailer, Directors, Rating (with year made and genre, Actors)
matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://i.ytimg.com/vi/qEXv-rVWAu8/movieposter.jpg",
                     "https://www.youtube.com/watch?v=tGgCqGm_6Hs",
                     "Directora: Andy Wachowski (as The Wachowski Brothers) , Lana Wachowski (as The Wachowski Brothers)",
                     "Rated: R (1999) | Action, Sci-Fi",
                     "Actors: Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

matrix2 = media.Movie("The Matrix Reloaded",
                     "Neo and the rebel leaders estimate that they have 72 hours until 250,000 probes discover Zion and destroy it and its inhabitants. During this, Neo must decide how he can save Trinity from a dark fate in his dreams.",
                     "http://resizing.flixster.com/g0k3LxainE8qySe4Nwb1Y-KNDT4=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/96/11169699_ori.jpg",
                     "https://www.youtube.com/watch?v=NtGs6wIvnrI",
                     "Directora: Andy Wachowski (as The Wachowski Brothers) , Lana Wachowski (as The Wachowski Brothers)",
                     "Rated: R (2003) | Action, Sci-Fi",
                     "Actors: Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

matrix3 = media.Movie("The Matrix Revolutions",
                     "The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith.",
                     "http://ia.media-imdb.com/images/M/MV5BMTkyNjc4NTQzOV5BMl5BanBnXkFtZTcwNDYzMTQyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=dyZ_kGhiB4U",
                     "Andy Wachowski (as The Wachowski Brothers) , Lana Wachowski (as The Wachowski Brothers)",
                     "R (2003) | Action, Sci-Fi",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

edgeOfTomorrow = media.Movie("Edge of Tomorrow",
                     "A military officer is brought into an alien war against an extraterrestrial enemy who can reset the day and know the future. When this officer is enabled with the same power, he teams up with a Special Forces warrior to try and end the war.",
                     "http://ia.media-imdb.com/images/M/MV5BMTc5OTk4MTM3M15BMl5BanBnXkFtZTgwODcxNjg3MDE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=fWI1zbx3-Ak",
                     "Doug Liman",
                     "PG-13 (2014) | Action, Sci-Fi",
                     "Tom Cruise, Emily Blunt, Bill Paxton...")

guardians = media.Movie("Guardians of the Galaxy",
                     "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                     "http://ia.media-imdb.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=maIEaTm5gBE",
                     "James Gunn",
                     "PG-13 (2014) | Action, Adventure, Sci-Fi",
                     "Chris Pratt, Vin Diesel, Bradley Cooper...")

americanSniper = media.Movie("American Sniper",
                     "Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind.",
                     "http://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=5bP1f_1o-zo",
                     "Clint Eastwood",
                     "R (2014) | Action, Biography, Thriller",
                     "Bradley Cooper, Selina Miller, Kyle Gallner...")

# Generates a list of the movie instances that will get passed to the web page generator.
movies = [matrix, matrix2, matrix3, edgeOfTomorrow, guardians, americanSniper]

# Calls the open_movies_page() funtion in fresh_tomatoes.py and passes the list of movie references to display on the web page.
fresh_tomatoes.open_movies_page(movies)
