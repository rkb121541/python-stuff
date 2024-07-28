def transpose(matrix):
    for i in range(1,len(matrix)):
        if len(matrix[i]) != len(matrix[i-1]):
            return "Each row in matrix must be the same size"
    result=[]
    for i in range(len(matrix[0])):
        subresult = []
        for j in range(len(matrix)):
            subresult += [matrix[j][i]]
        result += [subresult]
    return result

def main():
    # this is how matrices will be represented v
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #          0,1,2 , 0,1,2 , 0,1,2
    #            0       1       2
    print(transpose(matrix))

if __name__ == "__main__":
    main()