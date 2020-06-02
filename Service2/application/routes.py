from random import randint
import requests
from application import app

@app.route('/', methods=['GET', 'POST'])
def number_gen(): # 143 numbers in list
    listOfNumbers=[4, 3, 2, 4, 1, 3, 2, 3, 6, 4, 5, 3, 4, 3, 4, 5, 3, 6, 4, 5, 4, 1, 3, 2, 4, 5, 4, 3, 2, 4, 1, 3, 2, 3, 6, 4, 5, 3, 4, 3, 4, 5, 3, 6, 4, 5, 4, 1, 3, 2, 4, 2, 4, 3, 2, 4, 1, 3, 2, 3, 6, 4, 5, 3, 4, 3, 4, 5, 3, 6, 4, 5, 4, 1, 3, 2, 4, 2, 4, 3, 2, 4, 1, 2, 6, 4, 5, 3, 4, 3, 4, 5, 3, 6, 4, 5, 4, 1, 3, 2, 4, 5, 4,3,2,4,1,3,2,3,6,4,5,3,4,3,4,5,3,6,4,5,4,1,3,2,4,5,4,3,2,4,1,3,2,3,6,4,5,3,4]
    length = len(listOfNumbers)-1
    sum = 0
    for i in range(0, 10):
        sum += listOfNumbers[randint(0, length)]
    print(sum)
    return str(sum)