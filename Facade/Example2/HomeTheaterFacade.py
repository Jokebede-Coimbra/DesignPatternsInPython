# Facade para o Home Theater
class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, screen):
        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.screen = screen

    def watch_movie(self, movie):
        print("Preparando para assistir um filme...")
        self.screen.down()
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.play_movie(movie)
