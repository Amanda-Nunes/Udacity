import media
import fresh_tomatoes

#Media objects that used to create instances of movie class for each film in the website.
got = media.Movie("Game of Thrones 1 Season",
                  "1 hour 22min",
                  "https://upload.wikimedia.org/wikipedia/pt/thumb/a/a4/Game_of_Thrones_Temporada_1_Poster.jpg/220px-Game_of_Thrones_Temporada_1_Poster.jpg",
                  "https://www.youtube.com/watch?v=BpJYNVhGf1s")

aquaman = media.Movie("Aquaman",
                  "2 hour 22min",
                  "https://conteudo.imguol.com.br/c/entretenimento/be/2018/12/12/aquaman-e-e-seu-traje-classico-no-filme-1544637527838_v2_1295x1920.png",
                  "https://www.youtube.com/watch?v=WDkg3h8PCVU")


fantastic = media.Movie("Fantastic beasts the crimes of Grindelwald",
                  "2 hour 13min",
                  "https://m.media-amazon.com/images/M/MV5BZjFiMGUzMTAtNDAwMC00ZjRhLTk0OTUtMmJiMzM5ZmVjODQxXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                  "https://www.youtube.com/watch?v=8bYBOVWLNIs")


avengers = media.Movie("Avengers Infinity War",
                  "2 hour 40min",
                  "https://images-na.ssl-images-amazon.com/images/I/81oTRumvcRL._SY445_.jpg",
                  "https://www.youtube.com/watch?v=6ZfuNTqbHE8")


panther = media.Movie("Black Panther",
                  "2 hour 15min",
                  "https://upload.wikimedia.org/wikipedia/pt/thumb/9/90/Pantera_Negra_%28poster%29.jpg/250px-Pantera_Negra_%28poster%29.jpg",
                  "https://www.youtube.com/watch?v=xjDjIWPwcPU")


spider = media.Movie("Spider-Man Homecoming",
                  "2 hour 13min",
                  "https://upload.wikimedia.org/wikipedia/pt/thumb/2/2e/Homecomingposter.png/250px-Homecomingposter.png",
                  "https://www.youtube.com/watch?v=n9DwoQ7HWvI")


#List call "movies" that has all the movies I created previously in an array.
movies = [got,aquaman,fantastic,avengers,panther,spider]
#Use the movie list as input to open_movies_page function.
fresh_tomatoes.open_movies_page(movies)
