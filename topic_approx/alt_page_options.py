from didyoumean import didyoumean

spell = "Poshgresql"
correctSpell = didyoumean.didYouMean(spell, ['hello', 'posgres', 'postgres', 'postgressql'])
print (correctSpell)