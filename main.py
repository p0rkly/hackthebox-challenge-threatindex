import sys

KEYWORDS = {
    "scan": 1,
    "response": 2,
    "control": 3,
    "callback": 4,
    "implant": 5,
    "zombie": 6,
    "trigger": 7,
    "infected": 8,
    "compromise": 9,
    "inject": 10,
    "execute": 11,
    "deploy": 12,
    "malware": 13,
    "exploit": 14,
    "payload": 15,
    "backdoor": 16,
    "zeroday": 17,
    "botnet": 18,
}


def scan(phrase):
    score = 0
    phrase = "".join([char for char in phrase if char.isalpha()])

    for word in KEYWORDS:
        score = score + (phrase.count(word) * KEYWORDS.get(word))

    return score


if __name__ == "__main__":
    phrase = sys.argv[1]

    if phrase: print(scan(phrase))
