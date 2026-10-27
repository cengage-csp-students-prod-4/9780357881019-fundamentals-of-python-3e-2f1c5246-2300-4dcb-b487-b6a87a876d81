"""
Program: recognizer.py
Author: Michael Guillen

Recognizes sentences with any number of independent clauses,
using a recursive grammar (Section 7.1):

sentence = independentclause [conjunction sentence]
independentclause = nounphrase verbphrase
nounphrase = article [adjective] noun
verbphrase = verb nounphrase [prepositionalphrase]
prepositionalphrase = preposition nounphrase
"""

# The vocabulary
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
adjectives = ("RED",)
conjunctions = ("AND",)

def main():
    """Inputs sentences and checks them for grammatical correctness
    until the user presses return."""
    while True:
        text = input("Enter a sentence or press return to quit: ")
        if text == "":
            break
        words = text.upper().split()
        # The sentence must match the grammar with no words left over
        if sentence(words) and len(words) == 0:
            print("Ok, grammatically correct")
        else:
            print("Not ok, grammatically incorrect")

def sentence(words):
    """sentence = independentclause [conjunction sentence]"""
    if not independentClause(words):
        return False
    # A conjunction means another sentence must follow (recursive case)
    if accept(words, conjunctions):
        return sentence(words)
    # No conjunction: this was the last clause (base case)
    return True

def independentClause(words):
    """independentclause = nounphrase verbphrase"""
    return nounPhrase(words) and verbPhrase(words)

def nounPhrase(words):
    """nounphrase = article [adjective] noun"""
    if not accept(words, articles):
        return False
    accept(words, adjectives)   # The adjective is optional
    return accept(words, nouns)

def verbPhrase(words):
    """verbphrase = verb nounphrase [prepositionalphrase]"""
    if not (accept(words, verbs) and nounPhrase(words)):
        return False
    # The prepositional phrase is optional, but if a preposition
    # is present, a noun phrase must follow it
    if len(words) > 0 and words[0] in prepositions:
        return prepositionalPhrase(words)
    return True

def prepositionalPhrase(words):
    """prepositionalphrase = preposition nounphrase"""
    return accept(words, prepositions) and nounPhrase(words)

def accept(words, wordSet):
    """If the first word in words is in wordSet, removes that word
    and returns True. Otherwise, returns False."""
    if len(words) > 0 and words[0] in wordSet:
        words.pop(0)
        return True
    else:
        return False

if __name__ == "__main__":
    main()
