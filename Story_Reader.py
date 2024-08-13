import os
import pygame
import sys
from gtts import gTTS
from io import BytesIO

# Retrieve the path from command-line arguments
path = sys.argv[1] if len(sys.argv) > 1 else ""
path = os.path.abspath(path)

# Initialize Pygame
pygame.init()

# Set the window dimensions
win_width, win_height = 1366, 720

# Create the Pygame window
windowSurface = pygame.display.set_mode((win_width, win_height))

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Initialize lists to store story and image files
story_files, image_files = [], []

# Loop through files in the specified directory
for file in os.listdir(path):
    if file.lower().endswith('.jpg'):
        image_files.append(file)
    elif file.lower().startswith('story'):
        story_files.append(file)

# Determine if stories have titles
story_has_title = len(story_files) > len(image_files)

# Sort the lists
story_files = sorted(story_files)
image_files = sorted(image_files)

# Initialize Pygame font
pygame.font.init()
font = pygame.font.Font(None, 36)

# Initialize Pygame mixer
pygame.mixer.init()

# Loop through each story file
for number, story in enumerate(story_files):
    # Determine image path
    if story_has_title:
        image_index = max(0, number - 1)
        image_path = os.path.join(path, image_files[image_index]) if image_index < len(image_files) else None
    else:
        image_path = os.path.join(path, image_files[number])

    # Display image if available
    if image_path:
        image_to_show = pygame.image.load(image_path)
        image_to_show = pygame.transform.scale(image_to_show, (win_width, win_height))
        windowSurface.blit(image_to_show, (0, 0))
        pygame.display.update()

    # Read the story content from file
    story_path = os.path.join(path, story)
    with open(story_path, "r", encoding="latin-1") as file:
        story_content = file.read()

    # Split the story content into sentences
    sentences = story_content.split('.')
    for sentence in sentences:
        sentence = sentence.strip()
        print("Sentence:", sentence)

        # Display image
        windowSurface.blit(image_to_show, (0, 0))
        pygame.display.update()

        # Fill background with black
        pygame.draw.rect(windowSurface, (0, 0, 0), (0, win_height - 70, win_width, 70))

        # Display sentence in two rows with a black background
        words = sentence.split()
        half_length = len(words) // 2
        first_half = ' '.join(words[:half_length])
        second_half = ' '.join(words[half_length:])

        text1 = font.render(first_half, True, (255, 255, 255))
        text2 = font.render(second_half, True, (255, 255, 255))

        windowSurface.blit(text1, (10, win_height - 60))
        windowSurface.blit(text2, (10, win_height - 30))
        pygame.display.update()

        # Read sentence using gTTS
        if sentence:
            tts = gTTS(text=sentence, lang='en')
            audio_stream = BytesIO()
            tts.write_to_fp(audio_stream)
            audio_stream.seek(0)
            pygame.mixer.music.load(audio_stream)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)
        else:
            print("Empty sentence, skipping...")

# Quit Pygame
pygame.quit()
