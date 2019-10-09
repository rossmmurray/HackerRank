from termcolor import colored
from functools import reduce

# def outputFormat(someList):
#     res = reduce(lambda x, y: expression)
#     return 

def minimumBribes(q):
   
    queue = q[:]
    print(len(queue))
    bribeNumbers = []
    while True:
        changeFlag = False
        for i in range(len(queue) - 1):

            # swap if next one is closer
            # diffCurr = abs(queue[i + 1] - (i + 1))
            # diffNext = abs(queue[i] - (i + 1)) 
            if queue[i] != i + 1 and (queue[i + 1] not in bribeNumbers) and abs(queue[i + 1] - (i + 1)) < abs(queue[i + 1] - (i + 2)):
                bribeNumbers.append(queue[i + 1])
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                changeFlag = True
                print(colored(queue, 'red'))
            else:
                print(queue)
            
        # formatting
        print('---------------')

        # if no change in swipe through, end
        if queue == list(range(len(queue) + 1))[1:]:
            return len(bribeNumbers)
        else:
            if changeFlag == False:
                return 'too chaotic'

    
if __name__ == "__main__":
    arrayString1 = '2 1 5 3 4' 
    arrayString2 = '2 5 1 3 4'
    arrayString3 = '5 1 2 3 7 8 6 4'
    arrayString4 = '1 2 5 3 7 8 6 4'
    # res = minimumBribes([2, 1, 5, 3, 4])
    queue = list(map(int, arrayString4.split()))
    res = minimumBribes(queue)
    print(res)