import random

def easy():
    with open("word.txt", "r") as allWords:
        wordList = allWords.read()
        wordList = wordList.split()
        bigWords = []
        easy1 = 3
        easy2 = 5
        for words in wordList:
            if (len(words) >= easy1 and len(words) <= easy2):
                bigWords.append(words.upper())
        return random.choice(bigWords)


def medium():
    with open("word.txt", "r") as allWords:
        wordList = allWords.read()
        wordList = wordList.split()
        bigWords = []
        letters = 5
        letters2 = 7
        for words in wordList:
            if (len(words) >= letters and len(words) <= letters2):
                bigWords.append(words.upper())
        return random.choice(bigWords)


def hard():
    with open("word.txt", "r") as allWords:
        wordList = allWords.read()
        wordList = wordList.split()
        bigWords = []
        hards = 8
        hard2 = 16
        for words in wordList:
            if (len(words) >= hards and len(words) <= hard2):
                bigWords.append(words.upper())
        return random.choice(bigWords)


def charposition(word , c):
    return [i for i, x in enumerate(word) if x == c]