#A blueprint to create multiple instances of it for every film of the website
#with all parameters necessary to fulfill the films descriptions.
class Movie():
    def __init__(self,movie_title,movie_duration,poster_image,trailer_youtube):
        self.title = movie_title
        self.duration= movie_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
