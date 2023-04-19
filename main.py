import pygame
import random
import os

# Set up Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centers the game window
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Boston Guessing Game")
green_image = pygame.Surface((370, 370))
green_image.fill((0, 255, 0))
red_image = pygame.Surface((370, 370))
red_image.fill((255, 0, 0))

# Images from various popular spots in boston
prudential = pygame.image.load("areaphotos/prudential.jpeg")
copley = pygame.image.load('areaphotos/copley.jpeg')
northeastern = pygame.image.load('areaphotos/northeastern.jpeg')
boston_common = pygame.image.load("areaphotos/boston_common.jpeg")
boston_university = pygame.image.load("areaphotos/boston_university.png")
fenway = pygame.image.load("areaphotos/fenway.jpg")
northend = pygame.image.load('areaphotos/northend.jpeg')
garden = pygame.image.load('areaphotos/public_garden.jpeg')
charles = pygame.image.load('areaphotos/charles.png')
quincy = pygame.image.load('areaphotos/quincy.jpeg')
seaport = pygame.image.load('areaphotos/seaport.jpeg')
symphony = pygame.image.load('areaphotos/symphony.jpeg')
wentworth = pygame.image.load('areaphotos/wentworth.jpeg')
mfa = pygame.image.load('areaphotos/mfa.jpeg')
isabella = pygame.image.load('areaphotos/isabella.jpeg')
newbury = pygame.image.load('areaphotos/newbury.jpeg')
mit = pygame.image.load('areaphotos/mit.jpeg')
beacon = pygame.image.load('areaphotos/beacon-hill.jpeg')

prudential_atlas = pygame.image.load("atlasphotos/prudential_atlas.png")
copley_atlas = pygame.image.load('atlasphotos/copley_atlas.png')
northeastern_atlas = pygame.image.load('atlasphotos/northeastern_atlas.png')
boston_common_atlas = pygame.image.load("atlasphotos/boston_common_atlas.png")
boston_university_atlas = pygame.image.load("atlasphotos/boston_university_atlas.png")
fenway_atlas = pygame.image.load("atlasphotos/fenway_atlas.png")
northend_atlas = pygame.image.load('atlasphotos/northend_atlas.png')
garden_atlas = pygame.image.load('atlasphotos/public_garden_atlas.png')
charles_atlas = pygame.image.load('atlasphotos/charles_atlas.png')
quincy_atlas = pygame.image.load('atlasphotos/quincy_atlas.png')
seaport_atlas = pygame.image.load('atlasphotos/seaport_atlas.png')
symphony_atlas = pygame.image.load('atlasphotos/symphony_atlas.png')
wentworth_atlas = pygame.image.load('atlasphotos/wentworth_atlas.png')
mfa_atlas = pygame.image.load('atlasphotos/mfa_atlas.png')
isabella_atlas = pygame.image.load('atlasphotos/isabella_atlas.png')
newbury_atlas = pygame.image.load('atlasphotos/newbury_atlas.png')
mit_atlas = pygame.image.load('atlasphotos/mit_atlas.png')
beacon_atlas = pygame.image.load('atlasphotos/beacon_atlas.png')

choice_dict = {'Prudential': prudential,
               'Copley': copley,
               'Northeastern': northeastern,
               'Boston Commons': boston_common,
               'Boston University': boston_university,
               'Fenway Park': fenway,
               'Paul Revere Mall (northend)': northend,
               'Boston Public Garden': garden,
               'Charles River': charles,
               'Faneuil Hall': quincy,
               'Seaport': seaport,
               'Symphony': symphony,
               'Wentworth': wentworth,
               'Museum of Fine Arts': mfa,
               'Isabella Stewart Gardener': isabella,
               'Newbury St': newbury,
               'MIT': mit,
               'Beacon Hill': beacon}

atlas_dict = {'Prudential': prudential_atlas,
              'Copley': copley_atlas,
              'Northeastern': northeastern_atlas,
              'Boston Commons': boston_common_atlas,
              'Boston University': boston_university_atlas,
              'Fenway Park': fenway_atlas,
              'Paul Revere Mall (northend)': northend_atlas,
              'Boston Public Garden': garden_atlas,
              'Charles River': charles_atlas,
              'Faneuil Hall': quincy_atlas,
              'Seaport': seaport_atlas,
              'Symphony': symphony_atlas,
              'Wentworth': wentworth_atlas,
              'Museum of Fine Arts': mfa_atlas,
              'Isabella Stewart Gardener': isabella_atlas,
              'Newbury St': newbury_atlas,
              'MIT': mit_atlas,
              'Beacon Hill': beacon_atlas}

asked_already = set()


# Generates a question from the list of choices returns a tuple with of the format (Name of Area, Top Question Image,
# List of Indices not including the index of the answer)
def generate_question():
    while True:
        question_image_index = random.randint(0, len(choice_dict) - 1)
        answer = list(choice_dict.keys())[question_image_index]
        indices = list()
        if answer in asked_already:
            continue
        else:
            asked_already.add(answer)
            indices = list(range(0, len(choice_dict)))
            indices.remove(question_image_index)
            break

    question_image = choice_dict[answer]
    return answer, question_image, indices


def check_answer(index):
    global score
    if index == location:
        score += 1
        return True
    return False


# Set the timer for 45 seconds
clock = pygame.time.Clock()
time_remaining = 45
waiting = True
timer_font = pygame.font.Font(None, 64)
font = pygame.font.Font(None, 36)
question_text = font.render('Which atlas corresponds to this image?', True, (0, 0, 0))
toggle_text = font.render("Press 'n' to toggle the name", True, (0, 0, 0))
screen.blit(toggle_text, (800, 100))
screen.blit(question_text, (370, 30))
location = -1
score = 0
questions_asked = 0
name = False
current_name = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the correct answer
            mouse_pos = pygame.mouse.get_pos()
            correct = False
            if 770 >= mouse_pos[1] >= 400:
                coords = (0, 0)
                if 395 >= mouse_pos[0] >= 25:
                    correct = check_answer(0)
                    coords = (25, 400)
                    waiting = True
                    questions_asked += 1
                elif 785 >= mouse_pos[0] >= 415:
                    correct = check_answer(1)
                    coords = (415, 400)
                    waiting = True
                    questions_asked += 1
                elif 1180 >= mouse_pos[0] >= 810:
                    correct = check_answer(2)
                    coords = (810, 400)
                    waiting = True
                    questions_asked += 1
                else:
                    continue
                if correct:
                    screen.blit(green_image, coords)
                else:
                    screen.blit(red_image, coords)
                pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                name = not name

    if waiting:
        if questions_asked == len(choice_dict):
            break
        pygame.time.delay(500)
        atlases = list()
        # Generates, and displays the question and answer choices
        question = generate_question()
        current_name = question[0]
        image = pygame.transform.scale(question[1], (350, 300))
        screen.blit(image, (420, 60))
        wrong_choices = list()

        option1, option2 = random.sample(question[2], 2)
        wrong_choices.append(list(choice_dict.keys())[option1])
        wrong_choices.append(list(choice_dict.keys())[option2])

        location = random.randint(0, 2)

        for i in range(3):
            if i == location:
                atlas = question[0]
                image = pygame.transform.scale(atlas_dict[atlas], (370, 370))
                atlases.append(image)
            else:
                atlases.append(pygame.transform.scale(atlas_dict[wrong_choices.pop()], (370, 370)))

        screen.blit(atlases[0], (25, 400))
        screen.blit(atlases[1], (415, 400))
        screen.blit(atlases[2], (810, 400))
        waiting = False
        name = False

    # Handle timer
    screen.fill((255, 255, 255), (30, 30, 230, 50))
    time_remaining -= clock.tick(60) / 1000
    timer_text = timer_font.render(f'Time: {int(time_remaining)}', True, (0, 0, 0))
    screen.blit(timer_text, (30, 30))

    # Toggles the name of the area
    name_text = font.render("Area: {}".format(current_name), True, (255, 100, 100))

    if name:
        screen.blit(name_text, (800, 150))
    else:
        screen.fill((255, 255, 255), (800, 150, 400, 250))

    if time_remaining <= 0:
        break

    pygame.display.update()

# Display the final score
font = pygame.font.Font(None, 36)
score_text = font.render("Your score: {}".format(score), True, (255, 0, 255))
screen.blit(score_text, (40, 100))
pygame.display.flip()

# Wait for user to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
