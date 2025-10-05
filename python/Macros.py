import pyautogui
import time
import random
time.sleep(1)

nbStart = 90
nbEnd = 100
pyautogui.moveTo(1000, 990, duration=0)
for i in range(nbStart,nbEnd+1):
    pyautogui.click()
    pyautogui.typewrite(str(i))
    pyautogui.press('enter')

# words = [
#     "The spa attendant applied the deep cleaning mask to the gentlemans back.", 
#     "We have a lot of rain in June.",
#     "It was the best sandcastle he had ever seen.",
#     "Situps are a terrible way to end your day.",
#     "Love is not like pizza.",
#     "It had been sixteen days since the zombies first attacked.",
#     "Pat ordered a ghost pepper pie.",
#     "He kept telling himself that one day it would all somehow make sense.",
#     "Seek success, but always be prepared for random cats.",
#     "The quick brown fox jumps over the lazy dog.",
#     "Cursive writing is the best way to build a race track.",
#     "She had a habit of taking showers in lemonade.",
#     "The bird had a belief that it was really a groundhog.",
#     "Sometimes it is better to just walk away from things and go back to them later when youre in a better frame of mind.",
#     "With a single flip of the coin, his life changed forever.",
#     "The virus had powers none of us knew existed.",
#     "He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.",
#     "When he encountered maize for the first time, he thought it incredibly corny.",
#     "He strives to keep the best lawn in the neighborhood.",
#     "He didnt want to go to the dentist, yet he went anyway.",
#     "I cheated while playing the darts tournament by using a longbow.",
#     "The waitress was not amused when he ordered green eggs and ham.",
#     "When nobody is around, the trees gossip about the people who have walked under them.",
#     "The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.",
#     "After coating myself in vegetable oil I found my success rate skyrocketed.",
#     "He uses onomatopoeia as a weapon of mental destruction.",
#     "Joe discovered that traffic cones make excellent megaphones.",
#     "She insisted that cleaning out your closet was the key to good driving.",
#     "Thigh-high in the water, the fishermans hope for dinner soon turned to despair.",
#     "Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.",
#     "He wasn't bitter that she had moved on but from the radish.",
#     "He went back to the video to see what had been recorded and was shocked at what he saw.",
#     "The beauty of the African sunset disguised the danger lurking nearby.",
#     "He appeared to be confusingly perplexed.",
#     "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
#     "I want a giraffe, but I'm a turtle eating waffles.",
#     "We will not allow you to bring your pet armadillo along.",
#     "She wanted to be rescued, but only if it was Tuesday and raining.",
#     "Pantyhose and heels are an interesting choice of attire for the beach.",
#     "It took him a month to finish the meal.",
#     "Malls are great places to shop; I can find everything I need under one roof.",
#     "He said he was not there yesterday; however, many people saw him there.",
#     "She hadn't had her cup of coffee, and that made things all the worse.",
#     "Most shark attacks occur about 10 feet from the beach since that's where the people are.",
#     "The changing of down comforters to cotton bedspreads always meant the squirrels had returned.",
#     "I am happy to take your donation; any amount will be greatly appreciated.",
#     "She used her own hair in the soup to give it more flavor.",
#     "She felt that chill that makes the hairs on the back of your neck when he walked into the room.",
#     "Watching the geriatric mens softball team brought back memories of 3 yr olds playing t-ball.",
#     "There's an art to getting your way, and spitting olive pits across the table isn't it."
#     ]
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# # pyautogui.moveTo(500, 130, duration=0)
# for __ in range(3):
#     pyautogui.click()
#     # pyautogui.hotkey('ctrl','a')
#     pyautogui.press('backspace')
#     for ___ in range(random.randint(1, 10)):
#         for _ in range(random.randint(1, 10)):
#             pyautogui.typewrite(random.choice(letters))
#         pyautogui.typewrite(" ")
#     pyautogui.press('enter')
                    