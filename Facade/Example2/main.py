from DVDPlayer import DVDPlayer
from HomeTheaterFacade import HomeTheaterFacade
from amplifier import Amplifier
from screen import Screen


if __name__ == "__main__":
    # Configurando o sistema
    amplifier = Amplifier()
    dvd_player = DVDPlayer()
    screen = Screen()

    # Criando a Facade
    home_theater = HomeTheaterFacade(amplifier, dvd_player, screen)

    # Assistindo a um filme usando a Facade
    home_theater.watch_movie("The Matrix")
