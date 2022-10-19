import numpy as np
import cv2
import mediapipe as mp
import math
import pygame

# configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def convert_opencv_to_pygame(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    new_shape = img.shape[1::-1]
    new_img = pygame.image.frombuffer(img.tostring(), new_shape, "RGB")
    return new_img


class App:
    def __init__(self, screen_width, screen_height, bg_color=(0, 0, 0)):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        # self.sprites es para renderizar
        self.sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.cap = cv2.VideoCapture(0)
        self.hands = mp_hands.Hands(model_complexity=0)

    def process_frame(self, frame):
        results = self.hands.process(frame)
        if not results.multi_hand_landmarks:
            return frame
        out = frame.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                out,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        return out

    def update(self, keys):
        # get webcam frame
        ret, frame = self.cap.read()
        out_img = self.process_frame(frame)
        pygame_img = convert_opencv_to_pygame(out_img)
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame_img, (0, 0))
        pygame.display.flip()
        # para mantener 30 frames por segundo
        self.clock.tick(self.fps)

    def run(self):
        self.is_running = True
        # pygame.time.set_timer(self.ADD_ENEMY_EVENT, 250)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                # if event.type == pygame.KEYDOWN:
                #     if event.key == K_SPACE:
                #         self.player.shoot()

            keys = pygame.key.get_pressed()

            self.update(keys)

        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.run()
