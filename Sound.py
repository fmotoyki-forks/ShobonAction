import pygame
import pathlib
import os

pygame.mixer.init(buffer=512)


class Sound:
    SE_list = {}  # 効果音を格納するリスト

    def __init__(self):
        file_list = pathlib.Path(f'SE/').glob('*.wav')

        for file in file_list:
            name = os.path.splitext(file.name)[0]
            data = pygame.mixer.Sound(f"SE/{file.name}")

            self.SE_list[name] = data

    @classmethod
    def play_BGM(cls, name):
        pygame.mixer.music.load(f'BGM/{name}.mp3')
        pygame.mixer.music.play(-1)

    @classmethod
    def stop_BGM(cls):
        pygame.mixer.music.stop()

    @classmethod
    def play_SE(cls, name):
        cls.SE_list[name].play()