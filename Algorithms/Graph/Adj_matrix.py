'''
                  A
           2    /   \ 6
              /       \
            B -------- C
          /\      3    |
        5/  \  4       |8
        /    \         |
       D       E-------F   
                  1
'''

def printMatrix(matrix,vertices):
    [print(" "+i,end="") for i in vertices]
    print()
    for i in range(len(matrix)-1):
        print(vertices[i],end=" ")
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()


if __name__=="__main__":
    edge=[("A","B",2),("A","C",6),("B",'D',5),("B","E",4),("B","C",3),("E","F",1),("C","F",8)]
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', ]
    matrix=[[0]*len(vertices) for _ in range(len(vertices))]
    for v in edge:
        i=ord(v[0])-ord('A')
        j=ord(v[1])-ord('A')
        weight=v[2]
        matrix[i][j]=weight
        matrix[j][i]=weight
    printMatrix(matrix,vertices)
    