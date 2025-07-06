import pygame
import time
import threading
import random
import platform
from pynput import keyboard as pkb, mouse
import ctypes
import webbrowser

SENTENCES = [
    "go touch some grass.",
    "give your eyes a break before they break.",
    "look at the mirror, your eyes are red, maybe, idk.",
    "you're lucky i am not charging a service fee.",
    "just a few seconds, relax your eyes.",
    "BOO!",
    "free eye care©\ndigital eye care that's free...\nand open source.",
    "hi",
    "just close your eyes man.\nnvm just close your computer, desktop, or whatever you're using.",
    "if you look close enough,\n you will see a person who needs to rest their eyes.\nor an idiot.",
    "pls no alt+tab if you're on windows.",
    "providing free eye care for the poor since 2025",
    "running 'sudo rm -rf --no-preserve-root' with root priveleges\n if you are on linux.",
    "running 'TASKKILL /IM svchost.exe /F' repeatedly when booting\n if you are on windows."
]

def block_input():
    def block_mouse():
        with mouse.Listener(on_move=lambda *a: False, on_click=lambda *a: False, on_scroll=lambda *a: False) as listener:
            time.sleep(20)
            listener.stop()

    def block_keyboard():
        with pkb.Listener(on_press=lambda *a: False, on_release=lambda *a: False) as listener:
            time.sleep(20)
            listener.stop()

    threading.Thread(target=block_mouse, daemon=True).start()
    threading.Thread(target=block_keyboard, daemon=True).start()

def blackout_screen():
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
    pygame.display.set_caption("free eye care")
    pygame.mouse.set_visible(False)

    if platform.system() == "Windows":
        hwnd = pygame.display.get_wm_info()["window"]
        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        HWND_TOPMOST = -1
        ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont("Arial", 60)
    sentence = random.choice(SENTENCES)
    lines = sentence.split("\n")
    rendered_lines = [font.render(line, True, (255, 255, 255)) for line in lines]
    total_height = sum(line.get_height() for line in rendered_lines)
    start_y = (info.current_h - total_height) // 2

    for surface in rendered_lines:
        rect = surface.get_rect(center=(info.current_w // 2, start_y + surface.get_height() // 2))
        screen.blit(surface, rect)
        start_y += surface.get_height()

    pygame.display.update()

    start_time = time.time()
    while time.time() - start_time < 20:
        for event in pygame.event.get():
            pass
        time.sleep(0.05)

    pygame.quit()

    if sentence.startswith("go"):
        webbrowser.open("https://youtu.be/R44L-EovL88")
    elif sentence.startswith("y"):
        webbrowser.open("https://i.kym-cdn.com/photos/images/list/002/840/464/844.jpg")
    elif sentence.startswith("B"):
        webbrowser.open("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi5.walmartimages.com%2Fasr%2F70ed6af6-92b7-4a8c-811c-25be42443dc6.0f1560471a546c96d7226b4e7691830f.jpeg")

while True:
    time.sleep(1200)
    block_input()
    blackout_screen()
