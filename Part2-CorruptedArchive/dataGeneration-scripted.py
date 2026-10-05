import random 
from ListeningEvent import ListeningEvent

# declare team name and seed
TEAM_SEED = "Fantastic4"
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
# Initialize the random number generator with the team seed to ensure reproducibility of the generated data
listeners = [("L101", "Priya N.", "Salisbury"), ("L102", "Marcus T.", "Ocean City"),
             ("L103", "Wei L.", "Cambridge"), ("L104", "Ava R.", "Salisbury"),
             ("L105", "Diego F.", "Easton")]
# Initialize the list that will hold all generated streaming log lines
lines =[]

# Loop to generate 400 random streaming log entries
for _ in range (400):
    lid, lname, city = random.choice(listeners)
    title, artist, genre, dur = random.choice(songs)
    hour = random.randint(0,23)
    day = random.randint(1,28)
    played = random.randint(20,dur)
    line = (f"{lid} | {lname} | {title} | {artist} | "
            f"2026-03-{day:02d} {hour:02d}:00 | {played}")
    lines.append(line)

#Corrupt ~15% of the lines to simulate crash damage
for _ in range(60):
    i = random.randrange(len(lines))
    kind = random.choice(["blank", "missing_field", "bad_number"])
    if kind == "blank":
        lines[i] = ""
    elif kind == "missing_field":
        parts = lines[i].split(" | ")
        del parts[random.randrange(len(parts))]
        lines[i] = " | ".join(parts)
    else:
        parts = lines[i].split(" | ")
        parts[-1] = "N/A"
        lines[i] = " | ".join(parts)
# Shuffle the lines to further randomize the order before writing to the file
random.shuffle(lines)
with open("streambeats_log.txt", "w") as f:
    for line in lines:
        print(line, file=f)

#===============================================================================
#======Everything Below this line is the tasks given for Part 2=================
#===============================================================================

# TASK 1: parse_line(line) function
def parse_line(line):
    """Read line and splits one line on " | ", which then builds and returns a 
    ListeningEvent object. An exception should be raised if line is blank, has wrong
    number of fields, or has a non-numeric seconds_played value."""
    try:
        if not line.strip():
            raise ValueError("Line is blank")
        parts = line.split(" | ")
        if len(parts) != 6:
            raise IndexError("Line has missing fields")
        lid, lname, song_title, artist, timestamp, played = parts
        if not played.isdigit():
            raise ValueError("Non-numeric seconds_played value")
        return ListeningEvent(lid, lname, song_title, artist, timestamp, int(played))
    except IndexError:
        raise ValueError("Line has missing fields")
    except ValueError as e:
        raise ValueError(f"Error parsing line: {e}")

# TASK 2: Use with to open streambeats_log.txt, loop through each line, calling
# parse_line() inside a try/except block. On success append resulting ListeningEvent
# to a list called events, and failure increment a counter of skipped lines instead
# of crashing. 

events = []
skipped_lines = 0
with open("streambeats_log.txt", "r") as f:
    for line in f:
        try:
            event = parse_line(line)
            events.append(event)
        except ValueError:
            skipped_lines += 1

print(f"Total events parsed successfully: {len(events)}")
print(f"Total lines skipped: {skipped_lines}")

# TASK 3: Write short recovery report to recovery_report.txt using with and print(...,file=..)
# stating the total number of lines in log and how many were recovered successfully and how 
# many were skipped.


        