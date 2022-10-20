import numpy as np
import cv2
import mediapipe as mp
import math
import pygame

# configuraciones
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def convert_opencv_to_pygame(img, max_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, max_size)
    new_shape = img.shape[1::-1]
    new_img = pygame.image.frombuffer(img.tostring(), new_shape, "RGB")
    return new_img

def distance(p0, p1):
    return math.sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)

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
        self.pose = mp_pose.Pose(model_complexity=2)
        self.dist_threshold = 0.08
        self.circles = []

    def process_frame(self, frame):
        results = self.pose.process(frame)
        if not results.pose_landmarks:
            return frame
        out = frame.copy()
        
        mp_drawing.draw_landmarks(
            out,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing_styles.get_default_pose_landmarks_style(),
        )
        return out

    def update(self, keys):
        # get webcam frame
        ret, frame = self.cap.read()
        out_img = self.process_frame(frame)

        pygame_img = convert_opencv_to_pygame(out_img)
        

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
