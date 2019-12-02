def combination(numbers, num, start, answer):
    if(num == 6):
        #print (answer)
        print (' '.join(answer))# list to string
        return
    for i in range(start, int(numbers[0])+1):
        answer[num] = numbers[i]
        combination(numbers, num+1, i+1, answer)

while True:
    numbers = list(input().split())
    if numbers[0] is '0':
        break
    else:
        answer = ['0']*6
        combination(numbers, 0, 1, answer)
        print (' ')
