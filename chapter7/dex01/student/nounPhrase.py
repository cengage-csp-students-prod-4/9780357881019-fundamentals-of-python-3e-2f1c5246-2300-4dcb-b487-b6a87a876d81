import random
articles = ["the", "a", "one", "some", "any"]
adjectives = ["big", "small", "blue", "green", "yellow", "red", "purple", "orange", "brown", "black", "white"]
nouns = ["apple", "peach", "banana", "pear", "orange", "grape", "strawberry", "blueberry", "raspberry", "cherry", "watermelon", "cantaloupe", "honeydew"]
#nounphrase = article [adjectivephrase] noun
def nounPhrase():
    """Builds and returns a noun phrase."""
    phrase = random.choice(articles) + " "
    # The adjective phrase is optional
    if random.randint(0, 1) == 1:
        phrase += adjectivePhrase() + " "
    return phrase + random.choice(nouns)

#adjectivephrase = adjective [adjectivephrase]
def adjectivePhrase():
    """Builds and returns an adjective phrase."""
    phrase = random.choice(adjectives)
    # Base case: stop adding adjectives about half the time
    if random.randint(0, 1) == 1:
        phrase += " " + adjectivePhrase()
    return phrase

print(nounPhrase())