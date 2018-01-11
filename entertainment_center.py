import media
import fresh_tomatoes

# My favorite movie instances
transformers = media.Movie("Transformers: The last Knight", "",
"https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
"https://www.youtube.com/watch?v=AntcyqJ6brc")
avengers = media.Movie("Avengers", "",
"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
"https://www.youtube.com/watch?v=eOrNdBpGMv8")
thor = media.Movie("Thor", "",
"https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
"https://www.youtube.com/watch?v=JOddp-nlNvQ")
iron_man_3 = media.Movie("Iron Man 3", "",
"https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
captain_america = media.Movie("Captain America", "",
"https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg",
"https://www.youtube.com/watch?v=dKrVegVI0Us")
spider_man = media.Movie("Spider-Man: Homecoming", "",
"https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",
"https://www.youtube.com/watch?v=n9DwoQ7HWvI")

movies = [transformers, avengers,thor, iron_man_3, captain_america, spider_man]

# Open web page to view favorite movies
fresh_tomatoes.open_movies_page(movies)
