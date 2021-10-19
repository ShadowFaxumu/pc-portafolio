
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    #dictionaryFile = open('dictionary.txt')
    dictionaryFile = open('dictEsp.txt',encoding='utf-8')
    spanishWords = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        spanishWords[word] = None
    dictionaryFile.close()
    return spanishWords

SPANISH_WORDS = loadDictionary()


def getSpanishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split() # Divide un str por cada ' '

    if possibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in SPANISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords) # El porcentaje


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isSpanish(message, wordPercentage=30, letterPercentage=85):
    # Por default, el 60% de las palabras deben existir en el diccionario, y
    # 85% de todos los caracteres en el mensaje deben ser letras o espacios
    # (no signos de puntuacion o numeros).
    wordsMatch = getSpanishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch