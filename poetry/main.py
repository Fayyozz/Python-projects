from random import choice

verbs = ["kicks",
"jingles",
"bounces",
"slurps",
"meows",
"explodes", "curdles"]

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]

adjectives = ["furry",
"balding",
"incredulous",
"fragrant",
"exuberant", "glistening"]

prepositions = ["against",
"after",
"into",
"beneath",
"upon",
"for", "in", "like", "over", "within"]

adverbs = ["curiously",
"extravagantly",
"tantalizingly",
"furiously", "sensuously"]

noun1, noun2, noun3 = choice(nouns), choice(nouns), choice(nouns)
verb1, verb2, verb3 = choice(verbs), choice(verbs), choice(verbs)
adj1, adj2, adj3 = choice(adjectives), choice(adjectives), choice(adjectives)
prep1, prep2, prep3 = choice(prepositions), choice(prepositions), choice(prepositions)
adverb1 = choice(adverbs)

poet = f"""
A {adj1} {noun1}
A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""

print(poet)

