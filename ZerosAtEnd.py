def move_zeros(array):
    #your code here
    new = []
    zeros = []
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: new.append(array[i])
        else:
            new.append(array[i])   
    return new + zeros        

#tests
print(move_zeros([0,1,None,2,False,1,0]))