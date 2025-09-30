# HackTheBox Coding Challenge "Threat Index" Solution
I wrote this script to solve the HackTheBox Coding CHallenge "Threat Index":
https://app.hackthebox.com/challenges/Threat%20Index/


## Disclaimer
I am not saying this is the right way, or even a good way. I **am** saying it worked for me. Use this at your own risk.


## Usage
Simply copy the code in `main.py`, and paste it into the editor provided by the challenge, run it, then profit.


## How it works
The challenge provides a list of weighted keywords. The goal is to scan a string of characters the challenge will feed the script for those phrases and return a "threat index" indicating the level of threat the string represents.

**Keywords**
```python
KEYWORDS = {
    "scan": 1,
    "response": 2,
    "control": 3,
    "callback": 4,
    "implant": 5,
    "zombie": 6,
    # ... snip ...
}
```
As you can see, `zombie` is worth 6 points, `scan` is worth 1, and so on.

Phrases are passed as arguments to the script `sys.args[1]` and can contain non-alpha characters. We pass that phrase to the `scan(<string>)` function.

Using a List Comprehnsion, we remove any non-alpha characters.
```python
phrase = "".join([char for char in phrase if char.isalpha()])
```

Here, we count occurrences of each keyword in the phrase and multiply that count by each keywords' weight, and return the total score for that phrase.
```python
for word in KEYWORDS:
    score = score + (phrase.count(word) * KEYWORDS.get(word))

return score
```

Print the result to ther console and you win.
```python
if __name__ == "__main__":
    phrase = sys.argv[1]

    if phrase: print(scan(phrase))
```

