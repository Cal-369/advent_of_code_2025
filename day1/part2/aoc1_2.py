from test1 import input_data

STARTING_AT = 50

    
def password(given_rotations):
    counter = 0
    res = STARTING_AT
    res_list = []
    
    # L = '-' , R = '+'
    # REMEMBER THE LIMIT => nums = list(i for i in range(100))
    
    for rotation in given_rotations:
        k = int(rotation[1:])
        if rotation[0] == 'R':
            for n in range(k):
                if res < 99:
                    res += 1
                elif res == 99:
                    res = 0
                if n < (k-1) and res == 0:
                    counter += 1
            res_list.append(res)
        elif rotation[0] == 'L':
            for n in range(k):
                if res > 0:
                    res -= 1
                elif res == 0:
                    res = 99
                if n < (k-1) and res == 0:
                    counter+=1
            res_list.append(res)
    print(res_list)

    for i in res_list:
        if i == 0:
            counter += 1
        else:
            continue
    return counter

answer = password(input_data)
print(answer)
    

#5657
#yess. we did it...!!!