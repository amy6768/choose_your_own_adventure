
import tkinter as tk
from PIL import Image, ImageTk

# Define the main window
root = tk.Tk()
root.config(bg='black')
root.title("Choose Your Own Adventure Game")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the main window
x = (screen_width / 2) - (500 / 2)
y = (screen_height / 2) - (500 / 2)

# Set the main window geometry and position
root.geometry("500x500+{}+{}".format(int(x), int(y)))

# Define the beginning story text
story_text = ''' 
    WELCOME TO CHOOSE YOUR OWN ADVENTURE!

    You will start your adventure by choosing one of the doors to enter.

    Option 1: Go through the yellow door
    Option 2: Go through the red door

    Which door will you choose?

    Click on the picture of the door you want to go through.
    '''

adventure_story = tk.Label(root, text=story_text, font=("Courier", 18))
adventure_story.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
adventure_story.config(bg='black')

# Define the images for the options
option1_image = ImageTk.PhotoImage(Image.open("myenv/images/yellow_door.jpg").resize((500,400)))
option2_image = ImageTk.PhotoImage(Image.open("myenv/images/red_door.jpg").resize((500,400)))


def yellow_door():
    story_text = '''
    You chose the yellow door.

    You are now in a forest, with towering trees and the occasional 
    rustle of unseen creatures, creating an ominous feeling of being watched.

    Option 1: Keep walking deeper into the forest
    Option 2: Turn back 

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update images
    change_option1_image("myenv/images/forest.jpg")
    change_option2_image("myenv/images/turn_back_forest.jpg")

    # Update the commands  
    option1.config(command=deeper_into_forest)
    option2.config(command=go_back)

def red_door():
    story_text = '''
    You chose the red door.

    You enter a city, and quickly realize there is trouble!
    There's a UFO hovering above, and a funnel cloud over 
    the water.

    Option 1: Explore the city
    Option 2: Turn back

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/city_ufo.jpg")
    change_option2_image("myenv/images/turn_back_city.jpg")

    # Update the commands  
    option1.config(command=explore_city)
    option2.config(command=go_back)

def go_back():
    story_text = '''
    WELCOME TO CHOOSE YOUR OWN ADVENTURE!

    You will start your adventure by choosing one of the doors to enter.

    Option 1: Go through the yellow door
    Option 2: Go through the red door

    Which door will you choose?

    Click on the picture of the door you want to go through.
    '''

    adventure_story.config(text=story_text)

    # Update images
    change_option1_image("myenv/images/yellow_door.jpg")
    change_option2_image("myenv/images/red_door.jpg")

    # Update the commands  
    option1.config(command=yellow_door)
    option2.config(command=red_door)

# Explore the forest in door one
def deeper_into_forest():
    story_text = '''
    You chose to walk deeper into the forest.

    As you are walking deeper into the forest, eventually you come to a clearing.
    
    In the middle of the clearing, there's a small pond. The water is crystal 
    clear, and you can see fish swimming around.

    Option 1: Drink from the pond
    Option 2: Keep walking

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/fish_pond.jpg")
    change_option2_image("myenv/images/keep_going.jpg")

    # Update the commands  
    option1.config(command=drink_from_pond)
    option2.config(command=keep_walking)
    
def drink_from_pond():
    story_text = '''
    You chose to drink from the pond.
    
    You immediately feel a strange energy coursing through your body. 
    You feel stronger and more focused
    than ever before.
    
    Suddenly, you hear a loud roar from behind you. 
    You turn around and see a giant bear is staring at you!

    Option 1: Fight the bear
    Option 2: Run away

    Which option will you choose?
    '''
    
    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/bear_growling.jpg")
    change_option2_image("myenv/images/run.jpg")

    option1.config(command=fight_bear)
    option2.config(command=run_away)

def keep_walking():
    story_text = '''
    You chose to keep walking.
    
    Soon you come to a bridge over a rushing river.
    The bridge looks unstable, but you have to cross it to continue
    on your journey.

    Option 1: Cross the bridge
    Option 2: Turn back

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/old_bridge.jpg")
    change_option2_image("myenv/images/old_bridge_turn_back.jpg")

    option1.config(command=cross_bridge)
    option2.config(command=turn_back)

def fight_bear():
    story_text = '''
    You chose to fight the bear.

    You fight the bear with all your might, dodging its attacks
    and landing powerful blows.
    
    Eventually, you defeat the bear and
    it runs away. You feel a surge of triumph and adrenaline.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def run_away():

    story_text = '''
    You chose to run away.

    You run away as fast as you can, your heart pounding in your chest.
    You manage to escape the bear.

    You come across a cave.
    
    Option 1: Go inside the cave
    Option 2: Take a nap
    
    Which optio will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/cave.jpg")
    change_option2_image("myenv/images/sleep_zzz.jpg")

    option1.config(command=explore_cave)
    option2.config(command=sleep_zzz)

def sleep_zzz():
    story_text = '''
    You chose to take a nap.
    
    As you are slumbering you are rudely awaken
    by a crazy raccoon!

    The raccoon is trying to steal your hat, so you jump up
    and hightail it out of there! 

    You are hungry, tired, and realize that you left your shoes
    behind. You decide it's time to go home.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''
    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def explore_cave():
    story_text = '''
    You chose to explore the cave.

    You turn your flashlight on and then enter the cave.
    
    As you walk slowly in, you spot something shiny 
    towards the back of the cave.

    You decide to check it out and find treasure!

    You load up the treasure in your backpack and head home
    to enjoy your new wealth.

    Option 1: Try again
    Option 2: End story

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)


def cross_bridge():
    story_text = '''
    You chose to cross the bridge.

    You carefully cross the bridge, and make it safely to the
    other side.
    
    You continue on your journey, feeling more
    confident and capable than ever before. Suddenly, you hear a rustling
    in the bushes.
    
    You turn around and see a group of bandits approaching you!

    Option 1: Fight the bandits
    Option 2: Try to negotiate

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/bandits.jpg")
    change_option2_image("myenv/images/negotiate.jpg")

    option1.config(command=fight_bandits)
    option2.config(command=try_to_negotiate)

def turn_back():
    story_text = '''
    You chose to turn back, feeling unsure and uncertain.

    You never reach your destination, and you spend the rest
    of your life wondering what might have been.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def fight_bandits():
    story_text = '''
    You chose to fight the bandits.

    You fight them with all your might, using the
    skills and strength you gained from the pond. The bandits
    are no match for you, and they flee in fear.

    You continue on your journey, feeling like a hero.
    Eventually, you come to a village where the people are being 
    terrorized by a dragon.

    Option 1: Fight the dragon
    Option 2: Try to find a peaceful solution

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/dragon.jpg")
    change_option2_image("myenv/images/peaceful_solution.jpg")

    option1.config(command=fight_dragon)
    option2.config(command=peaceful_solution)

def try_to_negotiate():
    story_text = '''
    You chose to try to attempt to negotiate with the bandits.

    They do not care what you have to say and take
    all your valuables.

    Then they tie you to a tree and you have to wait for help to come.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game.

    The end.'''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def fight_dragon():
    story_text = '''
    You bravely chose to face the dragon.

    Using all your strength and
    skill to defeat it. The villagers are overjoyed, and they reward
    you with riches beyond your wildest dreams.

    You become a legendary hero, known throughout the land for
    your courage and skill.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game.

    The end.'''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def peaceful_solution():
    story_text = '''
    You chose to find a peaceful solution.

    So you try talking to the dragon
    to understand its grievances. Eventually, you come up with a plan
    that satisfies both the dragon and the villagers.

    The villagers are grateful to you for your wisdom and diplomacy,
    and they reward you with riches beyond your wildest dreams.

    You become a wise and respected leader, known throughout the land
    for your diplomacy and intelligence.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game.

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)


# Explore the city in door two
def explore_city():
    story_text = '''
    You chose to explore the city.

    Marveling at its strange and
    wondrous sights, you eventually come to a dark alleyway.

    Option 1: Explore the alleyway
    Option 2: Go towards the bright lights in the distance

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/alley_way.jpg")
    change_option2_image("myenv/images/bright_lights.jpg")

    option1.config(command=dark_alleyway)
    option2.config(command=bright_lights)

def dark_alleyway():
    story_text = '''
    You chose to explore the dark alleyway.

    As you are walking down the alleyway, you suddenly see an alien!

    What do you want to do?

    Option 1: Talk to the alien
    Option 2: Run away

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/alien_in_alley.jpg")
    change_option2_image("myenv/images/run_fast.jpg")

    option1.config(command=talk_to_alien)
    option2.config(command=run_away_from_alien)

def bright_lights():
    story_text = '''
    You chose to explore the bright lights.

    As you get closer you are mesmerized by their beauty,
    but unsure what these bright structures are used for.

    Option 1: Find the entrance
    Option 2: Get out of there to take pictures of the funnel cloud

    Which option will you choose? 
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/bright_entrance.jpg")
    change_option2_image("myenv/images/funnel_cloud.jpg")

    option1.config(command=bright_entrance)
    option2.config(command=funnel_cloud)

def bright_entrance():
    story_text = '''
    You chose to find the entrance to the brightly lit structures

    You enter the door and fall into a portal.
    You are taken to another planet and are never
    seen again.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def funnel_cloud():
    story_text = '''
    You chose to take pics of the funnel cloud.

    As you are taking pics, you notice
    a baby alien watching you. It appears he's 
    by himself.

    Option 1: Go help the baby alien
    Option 2: Leave the baby alien and get out of there

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/baby_alien.jpg")
    change_option2_image("myenv/images/run_fast.jpg")

    option1.config(command=help_baby_alien)
    option2.config(command=leave_baby_alien)

def help_baby_alien():
    story_text = '''
    You chose to help the baby alien.

    You approach the baby alien and he reaches his arms up.
    You pick him and he clings to you tightly with his arms.

    Option 1: Find his parents
    Option 2: Take him home

    Which option will you choose?
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/alien_parents.jpg")
    change_option2_image("myenv/images/time_to_go_home.jpg")

    option1.config(command=alien_parents)
    option2.config(command=take_alien_home)

def leave_baby_alien():
    story_text = '''
    You to leave the baby alien and get out of there.

    You are tired of the exploring the city and
    want to go home.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def alien_parents():
    story_text = '''
    You chose to find the baby alien's parents.

    They are forever grateful to humankind for the
    return of their baby.

    They leave Earth to find another planet to inhabit.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def take_alien_home():
    story_text = '''
    You chose to take the alien home.

    You name your baby alien Sirius and he becomes
    part of your family. You are the most
    popular person in town.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def talk_to_alien():
    story_text = '''
    You chose to talk to the alien.

    The alien abducts you.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game.

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def run_away_from_alien():
    story_text = '''
    You chose to run away from the alien.

    You find yourself sucked into the funnel cloud 
    and whisked away to a far away deserted island.

    You remain on the island for the rest of your life.

    Your story has ended.

    Option 1: Try again
    Option 2: End game

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

def give_thieves_what_they_want():
    story_text = '''
    You give the thieves what they want, and they let you go.
    You continue exploring the city, but you can't help feeling violated and powerless.

    Your story has ended. 
    
    Option 1: Try again
    Option 2: End game.

    The end.
    '''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/try_again.jpg")
    change_option2_image("myenv/images/end_story.jpg")

    option1.config(command=start_over)
    option2.config(command=end_game)

# End game function option
def end_game():
    story_text = ''''''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/game_over_1.jpg")
    change_option2_image("myenv/images/game_over_2.jpg")

    option1.config(command='disabled')
    option2.config(command='disabled')

# Start over function option
def start_over():
    story_text = ''' 
    YOU CHOSE TO TRY AGAIN! GOOD LUCK!
    You will start your adventure by choosing one of the doors to enter.\n
    Option 1: Go through the first door
    Option 2: Go through the second door\n
    Which door will you choose?\n
    Click on the picture of the door you want to go through.'''

    adventure_story.config(text=story_text)

    # Update the option images
    change_option1_image("myenv/images/yellow_door.jpg")
    change_option2_image("myenv/images/red_door.jpg")

    option1.config(command=yellow_door)
    option2.config(command=red_door)

def change_option1_image(img):
    global option1_image  
    option1_image = ImageTk.PhotoImage(Image.open(img).resize((500,400)))   
    option1.config(image=option1_image)
    
def change_option2_image(img):
    global option2_image
    option2_image = ImageTk.PhotoImage(Image.open(img).resize((500,400)))
    option2.config(image=option2_image)

# Create a frame to center the buttons
frame = tk.Frame(root, bg='black')
frame.grid(row=1, column=0, columnspan=2, pady=20)

# Create buttons for story options
option1 = tk.Button(frame, image=option1_image, command=yellow_door)
option1.pack(side="left", padx=10)

option2 = tk.Button(frame, image=option2_image, command=red_door)
option2.pack(side="right", padx=10)

# Center the widgets inside the main window
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Start the main loop
root.mainloop()
