import random 

# declare team name and seed
TEAM_SEED = "Fantastic Four"
random.seed(TEAM_SEED)

# define songs, listeners and initiliaze lines
songs = [
    ("Neon Tide", "Kalea Voss", "Synthpop", 222), 
    ("Grave Road", "Tomas Reyes", "Country", 198), 
    ("Static Bloom", "Night Jar", "Indie Rock", 251), 
    ("Midnight Ferry", "Yuna Cho", "R&B", 214), 
    ("Paper Lanterns", "The Lowlights", "Folk", 214), 
    ("Circus Heart", "Kalea Voss", "Synthpop", 205), 
    ("Dust and Static", "Nightjar", "Indie Rock", 233), 
]

listeners = [("L101", "Priya N.", "Salisbury"), ("L102", "Marcus T.", "Ocean City"),
             ("L103", "Wei L.", "Cambridge"), ("L104", "Ava R.", "Salisbury"),
             ("L105", "Diego F.", "Easton")]

lines =[]

# Loop 
for _ in range (400):
    lid, lname, city = random.choice(listeners)
    title, artist, genre, dur = random.choice(songs)
    hour = random.randint(0,23)
    day = random.randint(1,28)