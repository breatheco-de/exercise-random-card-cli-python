import random
suites = ['♡', '♢', '♤', '♧']
numbers = list(range(1,14))

def get_random_card():
    random_suit = suites[random.randint(0,len(suites)-1)]
    random_number = numbers[random.randint(1,len(numbers)-1)]
    if(random_number == 1):
        random_number = "A"
    elif(random_number == 11):
        random_number = "J"
    elif(random_number == 12):
        random_number = "Q"
    elif(random_number == 13):
        random_number = "K"
    return str(random_number) + str(random_suit)

print(get_random_card())