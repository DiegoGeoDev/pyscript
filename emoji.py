import emoji
import random


pyscript.write("result", emoji.emojize(":T-Rex:"))


def getEmoji(*args):
    emojis = [":T-Rex:", ":alien:", ":bug:", ":ghost:", ":glowing_star:"]
    random.shuffle(emojis)

    pyscript.write("result", emoji.emojize(emojis[0]))
