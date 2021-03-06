import fresh_tomatoes
import media

# Create movie instances
frozen = media.Movie("Frozen", "http://t0.gstatic.com/images?q=tbn:ANd9GcTIaSaZM-kGnMKWNNMW9-_yv008JrEh58Ab3DAV1geUNJvXeyXS",  # NOQA
                               "https://www.youtube.com/watch?v=FLzfXQSPBOg")

short = media.Movie("The Big Short", "http://t0.gstatic.com/images?q=tbn:ANd9GcTXyM8ObeZ-zWDqxf0Q40iOeWw26uXJ7CTfGVoxyez5PVokMYqB",  # NOQA
                    "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

nemo = media.Movie("Finding Nemo", "https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0",  # NOQA
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")

stellar = media.Movie("Interstellar", "http://posterposse.com/wp-content/uploads/2014/10/interstellar-poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=ePbKGoIGAXY")

zootopia = media.Movie("Zootopia", "http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi",  # NOQA
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

inside = media.Movie("Inside Out", "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",  # NOQA
                     "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

# Create a list of movies
movies = [frozen, short, nemo, stellar, zootopia, inside]

# Show movies in a html file
fresh_tomatoes.open_movies_page(movies)
