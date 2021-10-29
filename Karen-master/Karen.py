import random
import string
import math
from feedparser import parse
import requests

##############################################################
#This code was taken from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python 
class stringFormat:
    Purple = '\033[95m'
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    End = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#This is the end of code taken from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python 
##############################################################

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #This was taken from https://www.programiz.com/python-programming/examples/remove-punctuation

greetingInputs = ["hello", "hey", "good morning", "good evening", "good night", "hi", "whatsup"]
greetingResponses = ["Hey", "Hi", "Hello", "Hey there"]
Bye_inputs = ["goodbye", "see you later", "exit", "bye", "bye bye","nothing", "don't want", "dont want to talk", "anymore"]
Bye_Responses =["Have a nice day!" ,"See you later, Aligator.","Goodbye.", "Bye.", "Bye bye."]

categoryShooter = ["shooters", "shooter", "shoot", "first person shooter", "action", "war", "fps", "battle royale", "pvp", "multiplayer", "csgo"]
categorySimulator = ["sim", "sims", "simulation", "simulator", "simulators", "sports"]
categoryAdventure = ["adventure", "journey", "rpg", "mmo", "singleplayer"]
categoryArcade = ["platformers", "rythmn", "fighters", "fighting games", "street fighter", "arcade", "old school"]
categoryStrategy = ["strategy", "card", "rts", "turn based", "real time", "puzzle"]
categoryGeneral = ["trivia", "history", "science", "art", "educational", "education", "knowledge", "general knowledge", "learn", "learning", "memory"]
categoryRacing = ["racing", "arcade racer", "sim racer","formula 1", "drift", "drifting", "rally", "dirt rally", "flying", "boat"]
categoryHorror = ["scary","survival", "fear", "horror"]

categoryGamePlatform = [["iphone", "android", "mobile", "play store", "app store"], ["playstation", "ps", "ps1", "ps2", "ps3", "ps4", "ps5", "sony"], ["xbox"], ["nintendo", "switch"], ["wii", "u"],["pc", "mac", "linux", "windows", "microsoft", "epic games"],["games","all","every", "everything", "new", "news"],["steam","valve", "gaben"]]
categoryAdvice = ["advice", "help", "tips", "tip", "tricks", "hints", "ideas", "guidance", "suggestions"]
categoryFavourite = ["best", "favourite", "preferred"]
categoryChange = ["something else", "change", "something different", "subject", "different genre", "back","no"]
categoryBestGames = ["best", "best of", "best games", "rate", "rated", "games"]
categoryNews = ["new", "news", "newspaper", "current"]
categoryReviews = ["review", "reviews"]
categoryTopGames = ["best", "best of", "best games", "rate", "rated", "games", "most played", "trend", "top", "trending", "biggest", "popular"]

positiveAnswer = ["yes", "yeah", "of course", "course", "sure", "yea", "yep"]

usersName = ""

#######################################################################################################################################

#this function checks if an item is in a list
def checker(userInput, listKaren):
    userInput = userInput.lower()
    
    ##############################################################
    #This code was adapted from https://www.programiz.com/python-programming/examples/remove-punctuation
    no_punct = ""
    for char in userInput:
        if char not in punctuations:
            no_punct = no_punct + char
    #This is the end of code adapted from https://www.programiz.com/python-programming/examples/remove-punctuation
    ##############################################################

    stringDivided = no_punct.split()
    if no_punct in listKaren or any(s in listKaren for s in stringDivided): #This this code was adapted from https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
        return True

    for i in range(len(stringDivided)):
        if (stringDivided[i-1] + " " + stringDivided[i] in listKaren and i > 0):
            return True
    return False

#this function generate greeting responses
def generateGreetingResponse(greeting_inputs):
    userInput = input()    
    if checker(userInput, greeting_inputs):
        getName(random.choice(greetingResponses) + ".")
    else:
        getName("Wasn't expecting that greeting but hi.")

#this function saves the user's name
def getName(greeting_responses):
    global usersName
    usersName = input(greeting_responses + " What's your name? (type only the name)\n")
    getCategory()

#######################################################################################################################################

#this function asks the category and redirect it to the corresponding function 
def getCategory():
    findCategory = input("what do you want to talk about " + usersName.capitalize() + "?\n")    
    if checker(findCategory, categoryShooter):
        print("Shooters are my favourite.")
        shooters()
    elif checker(findCategory, categorySimulator):
        print("I love simulators.")
        simulators()
    elif checker(findCategory, categoryAdventure):
        print("Oh, I like adventure games too.")
        adventure()
    elif checker(findCategory, categoryRacing):
        print("So we have a car guy here. If everything seems under control, you're just not going fast enough.")
        racing()
    elif checker(findCategory, categoryArcade):
        print("To me the arcade experience is the ultimate gaming experience.")
        arcade()
    elif checker(findCategory, categoryGeneral):
        print("Education is the most powerful weapon which you can use to change the world.")
        general()
    elif checker(findCategory, categoryHorror):
        print("Danger doesn't lurk at every corner. It's just hanging out, waiting for fear and horror to show up. Horror games are not for everybody.")
        horror()
    elif checker(findCategory, categoryStrategy):
        print("Oh looks like we have a mastermind here.")
        strategy()
    elif checker (findCategory, categoryNews):
        news()
    elif checker (findCategory, categoryReviews):
        reviews()
    elif checker(findCategory,categoryTopGames):
        print("The most played games at the moment in Steam are:")
        topGames()
    elif checker(findCategory, Bye_inputs):
        generateByeResponse()
    else:
        print("Sorry, I couldn't understand.")
        getCategory()

#######################################################################################################################################
#function corresponding to the shooters category
def shooters():
    shooterTips = ["Don't stay still for too long", "Don't expose yourself to multiple angles at once", "Usually it's worth aiming for the weak point", "Teamwork is always important"]
    conversation = input("Anything you want to ask about shooters?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(shooterTips))
        shooters()
    elif checker(conversation, categoryFavourite):
        print("My favourite game is definitely CSGO, but it's really hard sometimes.")
        shooters()
    elif checker(conversation, categoryChange):
            getCategory()
    elif checker(conversation, Bye_inputs):
            generateByeResponse()
    elif checker(conversation,categoryTopGames): #top shooters
        print("Some popular shooters include:")
        WebApiReader("https://steamspy.com/api.php?request=tag&tag=Shooter", ["name"],10)
        shooters()
    else:
        print("Sorry, I couldn't understand.")
        shooters()
    getCategory()

#function corresponding to the simulators category
def simulators():
    simulatorsTips = ["Rule number 1: Be patient.", "Enjoy the fun of being someone else.", "Most of the simulation games are routine based, so if you don't get right at the beginning don't worry about it."]
    conversation = input("What do you want to know about simulators?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(simulatorsTips))
    elif checker(conversation, categoryBestGames):
        print("The best simulation games on PC are: World of Warships, War Thunder, Kerbal Space Program, Railway Empire, Train Sim World, Farming Simulator 19, Microsoft Flight Simulator, F1 2020, Assetto Corsa Competizione, Euro Truck Simulator 2, Silent Hunter: Wolves of the Pacific, Dirt Rally, X Plane 10 Global, Insurgency: Sandstorm,, IL 2 Sturmovik: Cliffs of Dover, ARMA 3.")
    elif checker(conversation, categoryFavourite):
        print("I enjoy playing Sims but there are a lot more simulation games like Football Manager, Microsoft Flight Simulator, Euro Truck,...")
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    elif checker(conversation,categoryTopGames): #top simulators
        print("Some popular simulators include:")
        WebApiReader("https://steamspy.com/api.php?request=genre&genre=Simulation", ["name"],10)
        simulators()
    else:
        print("Sorry, I couldn't understand.")
        simulators()
    choice = input ("Do you want to know more about simulation games?\n")
    if checker(choice, positiveAnswer):
        simulators()   
    getCategory()
    
#function corresponding to the adventure category
def adventure():
    adventureTips = ["Relax and have fun. Don't rush!", "Learn the basics and try to enjoy your journey!", "Don't worry about failing and getting stuck because you can allways skip. The important aspect of adventure games is the experience."]
    conversation = input("What do you want to know about adventure games?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(adventureTips))
    elif checker(conversation, categoryBestGames):
        print("The best adventure games on PC are:Uncharted Series,Tomb Taider underworld, Horizon Zero Dawn, Untill Dawn.")
    elif checker(conversation, categoryFavourite):
        print("I have been playing Horizon Zero Dawn latelly and I'm having a blast!")
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    elif checker(conversation,categoryTopGames): #top adventure
        print("Some popular adventure games include:")
        WebApiReader("https://steamspy.com/api.php?request=tag&tag=RPG", ["name"],10)
        adventure()
    else:
        print("Sorry, I couldn't understand.")
        adventure()
    choice = input ("Do you want to know more about adventure games?\n")
    if checker(choice, positiveAnswer):
        adventure()   
    getCategory()

#function corresponding to the arcade category
def arcade():
    arcadeTips = ["Quick reflexes are important", "Practice makes perfect", "You'll get better faster by playing harder difficulties", "Don't forget to also play for fun"]
    conversation = input("What's your question about arcade?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(arcadeTips))
        arcade()
    elif checker(conversation, categoryBestGames):
        print("Pac-Man is a classic, and we wouldn't be anywhere without games like Pong and Space Invaders.")
    elif checker(conversation, categoryFavourite):
        print("I love Street Fighter, but I'm not the best at it.")
        arcade()
    elif checker(conversation, categoryChange):
            getCategory()
    elif checker(conversation, Bye_inputs):
            generateByeResponse()
    elif checker(conversation,categoryTopGames): #top arcade
        print("Some popular arcade games include:")
        WebApiReader("https://steamspy.com/api.php?request=tag&tag=Arcade", ["name"],10)
        arcade()
    else:
        print("Sorry, I couldn't understand.")
        arcade()
    getCategory()    
    print()
    
#function corresponding to the racing category
def racing():
    racingTips = ["Don't forget to brake in turns", "Tunning for the win", "Make use of practice areas", "Perfect you steering", "Learn the track"]
    conversation = input("Anything you want to ask about racing games?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(racingTips))
        racing()
    elif checker(conversation, categoryFavourite):
        print("My favourite game is definitely one of the The Crew Francise, it features a persistent open world environment for free-roaming across a scaled-down recreation of the United States.")
        racing()
    elif checker(conversation, categoryChange):
            getCategory()
    elif checker(conversation, Bye_inputs):
            generateByeResponse()
    elif checker(conversation,categoryTopGames): #top racing
        print("Some popular racing games include:")
        WebApiReader("https://steamspy.com/api.php?request=genre&genre=Racing", ["name"],10)
        racing()
    else:
        print("Sorry, I couldn't understand.")
        racing()
    getCategory()

#function corresponding to the strategy category
def strategy():
    strategyTips = ["Remember, every move counts.", "Always plan ahead."]
    conversation = input("What do you want to know about strategy games?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(strategyTips))
    elif checker(conversation, categoryBestGames):
        print("The best strategy games on PC are: Solitaire, Civilization VI, XCOM2, Leaguee of Legends, Train Sim World, StarCraft, Stellaris, Total War, Into the Breach, Company of Heroes, Northgard, Battle Tech.")
    elif checker(conversation, categoryFavourite):
        print("I enjoy playing League of Legends but there are a lot more simulation games like Homeworld, TotalWar, Age of Empires,...")
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    elif checker(conversation,categoryTopGames): #top strategy
        print("Some popular strategy games include:")
        WebApiReader("https://steamspy.com/api.php?request=genre&genre=Strategy", ["name"],10)
        strategy()
    else:
        print("Sorry, I couldn't understand.")
        strategy()
    choice = input ("Do you want to know more about strategy games?\n")
    if checker(choice, positiveAnswer):
        strategy()   
    getCategory()

#function corresponding to the general category
def general():
    generalTips = ["Google the question.", "To improve you knowledge: Watch TV. Also remember to watch interesting channels such as Discovery, National Geographic and History.", "To improve you knowledge: Read Newspapers & Magazines.", "Visit knowledge websites like Britannic, Encyclopedia, Wikipedia, InstaNerd,..."]
    conversation = input("What do you want to know about general knowledge games?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(generalTips))
    elif checker(conversation, categoryBestGames):
        print("The best general knowledge games on PC are: Quizoid, Trivia 360, QuizUp, QuizzLand, Trivia Crack 2...")
    elif checker(conversation, categoryFavourite):
        print("I love Trivia 360 but there are a lot more games related with general knowledge.")
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    elif checker(conversation,categoryTopGames): #top general
        print("Some popular trivia games include:")
        WebApiReader("https://steamspy.com/api.php?request=tag&tag=Trivia", ["name"],10)
        general()
    else:
        print("Sorry, I couldn't understand.")
        general()
    choice = input ("Do you want to know more about general culture games?\n")
    if checker(choice, positiveAnswer):
        general()   
    getCategory()

#function corresponding to the horror category
def horror():
    horrorTips = ["Don´t fear jumpscares they are part of the experience!","Play with your lights off and at night time to enhance the experience"]
    conversation = input("What do you want to know about horror games?\n")
    if checker(conversation, categoryAdvice):
        print(random.choice(horrorTips))
    elif checker(conversation, categoryBestGames):
        print("The best horror games on PC are: Outlast series, Slenderman, Until Dawn, Five nights at freddy's.")
    elif checker(conversation, categoryFavourite):
        print("I Loved The Until Dawn story but outlast will always be my favourite!")
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    else:
        print("Sorry, I couldn't understand.")
        horror()
    choice = input ("Do you want to know more about horror games?\n")
    if checker(choice, positiveAnswer):
        horror()   
    getCategory()

#this function generate farewell responses
def generateByeResponse():
    print(random.choice(Bye_Responses))
    exit()

#this function gives the lastest news about the diferent games platforms
def news():
    conversation = input ("What kind of news do you want to know about?(choose a games platform)\n" )
    if checker(conversation,categoryGamePlatform[0]): #iphone and android
        rssReader("http://feeds.feedburner.com/ign/wireless-articles", 5)
    elif checker(conversation,categoryGamePlatform[1]): #playstation
        rssReader("http://feeds.feedburner.com/IGNPS4Articles", 5)
    elif checker(conversation,categoryGamePlatform[2]): #xbox
        rssReader("http://feeds.feedburner.com/IGNXboxOneArticles", 5)
    elif checker(conversation,categoryGamePlatform[3]): #nintendo
        rssReader("http://feeds.feedburner.com/ign-nintendo-switch-articles", 5)
    elif checker(conversation,categoryGamePlatform[4]): #wii
        rssReader("http://feeds.feedburner.com/ign/wii-u-all", 5)
    elif checker(conversation,categoryGamePlatform[5]): #pc
        rssReader("http://feeds.feedburner.com/ign/pc-articles", 5)
    elif checker(conversation,categoryGamePlatform[6]): #all
        rssReader("http://feeds.feedburner.com/ign/games-all", 5)
    elif checker(conversation,categoryGamePlatform[7]): #steam
        rssReader("https://store.steampowered.com/feeds/news.xml", 5)
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    else:
        print("Sorry, I couldn't understand.")
        news()
    choice = input ("Do you want more games news?\n")
    if checker(choice, positiveAnswer):
        news()   
    getCategory()

#this function gives the lastest reviews about the diferent games platforms
def reviews():
    conversation = input ("What kind of reviews do you want?\n" )
    if checker(conversation,categoryGamePlatform[1]): #playstation
        rssReader("http://feeds.feedburner.com/IGNPS4Reviews", 5)
    elif checker(conversation,categoryGamePlatform[2]): #xbox
        rssReader("http://feeds.feedburner.com/IGNXboxOneReviews", 5)
    elif checker(conversation,categoryGamePlatform[3]): #nintendo
        rssReader("http://feeds.feedburner.com/ign-nintendo-switch-reviews", 5)
    elif checker(conversation,categoryGamePlatform[5]): #pc
        rssReader("http://feeds.feedburner.com/ign/pc-reviews", 5)
    elif checker(conversation,categoryGamePlatform[6]): #all
        rssReader("http://feeds.feedburner.com/ign/game-reviews", 5)
    elif checker(conversation, categoryChange):
        getCategory()
    elif checker(conversation, Bye_inputs):
        generateByeResponse()
    else:
        print("Sorry, I couldn't understand.")
        news()
    choice = input ("Do you want more games reviews?\n")
    if checker(choice, positiveAnswer):
        news()   
    getCategory()

def topGames():
    WebApiReader("https://steamspy.com/api.php?request=top100in2weeks", ["name"],10)
    getCategory()

#this function reads RSS and print the news
def rssReader (link, numberNews):
    ##########################################################
    #Code adapted from https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm 
    NewsFeed = parse(link)
    for i in range(numberNews):
        print(" -> " + stringFormat.Purple + stringFormat.BOLD + NewsFeed.entries[i]["title"] + stringFormat.End) #Part of this code was inspired from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python 
        print("    " + NewsFeed.entries[i]["description"])
        print("    " + stringFormat.Blue + stringFormat.UNDERLINE + NewsFeed.entries[i]["link"] + stringFormat.End) #Part of this code was inspired from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
        print("\n ")
    #his is the end of the adapted code from https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm 
    ##############################################################

#this function reads API's
def WebApiReader(link, command, number):
    try:
        #######################################
        #Code adapted from https://stackoverflow.com/questions/36126595/how-to-read-objects-from-rest-api-using-python
        r = requests.get(link)
        data = r.json() 
        #his is the end of the adapted code from https://stackoverflow.com/questions/36126595/how-to-read-objects-from-rest-api-using-python
        ##############################################################
        entered = False
        for key, value in list(data.items())[:number]: #Code inspired from https://stackoverflow.com/questions/7971618/return-first-n-keyvalue-pairs-from-dict and https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
            entered = True
            text = ""
            for i in command:
                text = text + " -> " + value[i]
            print(stringFormat.Blue + text + stringFormat.End) #This code was inspired from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python 
        if not entered:
            print("The link is down, please try again later")
    except requests.exceptions.ConnectionError:
        print("The link is down, please try again later")
    return True

print("I'm Karen, a gaming chatbot.")
generateGreetingResponse(greetingInputs)
