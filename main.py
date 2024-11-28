from pynput.keyboard import Controller, Key
import time

# Initialisation du contrôleur de clavier
keyboard = Controller()

# Fonction pour simuler l'appui sur Shift + F10
def press_shift_f10():
    # Appuyer sur les touches simultanément
    with keyboard.pressed(Key.shift):  # Maintenir Shift
        keyboard.press(Key.f10)       # Appuyer sur F10
        keyboard.release(Key.f10)     # Relâcher F10

# Attente de 30 secondes avant l'exécution
time.sleep(10)

# Exécution de la fonction
press_shift_f10()
