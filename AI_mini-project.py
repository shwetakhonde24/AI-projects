import random

name = random.choice(["Gabriel", "Thor", "Jasper", "Raketh", "Tebbius", "David"])

mood = random.choice(["bright", "dark", "evil"])

if mood == "bright":
  adj = ["vast", "beautiful", "magestic", "colourful", "seemingly enchanted", "glittering", "magical", "seemingly peaceful", "peaceful"]
  enemy = random.choice(["Pokemon", "cat", "cuddly soft toy", "kangaroo", "koala"])

elif mood == "dark":
  adj = ["forboding", "imposing", "terrifying", "deathly", "cold", "desolate"]
  enemy = random.choice(["crow", "tiger", "swarm of wasps", "snake"])

elif mood == "evil":
  adj = ["evil", "cursed", "terrifying", "deathly", "frozen", "desolate", "horrific"]
  enemy = random.choice(["sorcerer", "necromancer", "zombie", "terminator", "army of aliens"])

intro1 = "Scurrying down the " + random.choice(adj) + " hill, I came across a " + random.choice(adj) + " field."
intro2 = "I couldn't believe my eyes; I peered through the " + random.choice(["long", "dry", "thick"]) + " grass on the edge of the clearing to see a " + random.choice(adj) + " valley."
intro3 = "After what seemed an eternity, I opened my " + random.choice(["sleepy", "weary", "droopy", "rested"]) + " eyes and looked out across the " + random.choice(adj) + " mountains."
char1 = "Unexpectedly, I had a preminition of a " + enemy + ". I had waited my whole life for this moment."
char2 = "After so long, could it possibly be that my journey had come to an end?"
char3 = "I thought longingly of my family back home. I could hear them calling my name: '" + name +"'."
prob1 = "Suddenly, a giant " + enemy + " attacked from nowhere, charging towards me."
prob2 = "Without warning, the " + enemy + " swooped, attacking me from the clear sky. '" + name + "', it seemed to scream."
prob3 = "I didn't suspect for a moment that I would have company here, let alone from another world. But now, the " + enemy + " appeared."
sol1 = "Ever since my childhood, I had been terrified of every " + enemy + " I had ever seen. I did the only thing I could in the situation. I fled."
sol2 = random.choice(["Grabbing", "Clutching"]) + " the hilt of my sword, I charged towards the menace. It ran like the wind."
sol3 = "Now was the time, I thought, to awaken the dark energy I possessed. Unleashing the terror upon the enemy, I saw no more."
end1 = "Those with the name of " + name + " were destined to wander on forever amongst the " + random.choice(adj) + " rocks and spindly grass. That I understand now."
end2 = "Months later, I was able to make it back home unscathed. Well, except the " + random.choice(adj) + " wound inflicted by the " + enemy + "."
end3 = "This was the first " + random.choice(adj) + " battle, of which there would be many more."


intros = [intro1, intro2, intro3]
characters = [char1, char2, char3]
problems = [prob1, prob2, prob3]
solutions = [sol1, sol2, sol3]
endings = [end1, end2, end3]


print("A Random Story...")
print ("")

print(random.choice(intros)),
print(random.choice(characters)),
print(random.choice(problems)),
print(random.choice(solutions)),
print(random.choice(endings));
