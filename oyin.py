import pygame
import sys

# O'yinning boshlanish funksiyasi
def run_game():
    # Pygame ni boshlash
    pygame.init()
    # Ekran o'lchami
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mouse bilan mashina boshqarish")

    # Mashina rasmi
    car_image = pygame.image.load('car.png')
    car_rect = car_image.get_rect()
    car_rect.centerx = screen_width // 2
    car_rect.centery = screen_height // 2

    # Mashinaning tezligi
    car_speed = 5

    # O'yin davomiyligi
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mouse ni o'qib olish
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Mashinaning o'rnini yangilash
        if mouse_x > car_rect.centerx:
            car_rect.centerx += car_speed
        elif mouse_x < car_rect.centerx:
            car_rect.centerx -= car_speed

        if mouse_y > car_rect.centery:
            car_rect.centery += car_speed
        elif mouse_y < car_rect.centery:
            car_rect.centery -= car_speed

        # Ekran tozalash
        screen.fill((255, 255, 255))

        # Mashinaning tasvirini joylash
        screen.blit(car_image, car_rect)

        # Yangilanish
        pygame.display.flip()

# O'yin dasturini ishga tushirish
if __name__ == "__main__":
    run_game()
