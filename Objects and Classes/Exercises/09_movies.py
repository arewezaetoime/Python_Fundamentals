class Movie:
    __watched_movies = 0

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if self.watched is False:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: " \
               f"{Movie.__watched_movies}"


movie = Movie('Vuv filma', 'Ki4KoFF')
print(movie)
movie.watch()
print(movie)
movie.change_name('Deiba filma')
movie.change_director('Filmarq')
movie.watch()
print(movie)