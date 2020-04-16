import random
suites = ['♡', '♢', '♤', '♧']
values = list(range(1,14))

def get_random_card():
    suite_position = random.randint(0,len(suites)-1)
    value_position = random.randint(0,len(values)-1)
    return suites[suite_position] + str(values[value_position])
    
print(get_random_card())