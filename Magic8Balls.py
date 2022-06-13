import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again Later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'

r = random.randint(1,6)
fortune = getAnswer(r)

print(fortune)
