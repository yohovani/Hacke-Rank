from multiprocessing.connection import answer_challenge


def breakingRecords(scores):
    # Write your code here
    lowest = 0
    highest = 0
    l = scores[0]
    h = scores[0]

    for s in range(1,len(scores)):
        if l > scores[s]:
            lowest +=1 
            l = scores[s]
        if h < scores[s]:
            highest +=1
            h = scores[s]

    return [highest, lowest]

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores=scores))