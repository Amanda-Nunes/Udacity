import media
import fresh_tomatoes

got = media.Movie("Game of Thrones 1 Season",
                  "https://upload.wikimedia.org/wikipedia/pt/thumb/a/a4/Game_of_Thrones_Temporada_1_Poster.jpg/220px-Game_of_Thrones_Temporada_1_Poster.jpg",
                  "https://www.youtube.com/watch?v=BpJYNVhGf1s")


movies = [got]
fresh_tomatoes.open_movies_page(movies)
