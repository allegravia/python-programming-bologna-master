def times_table(n):
    ''' 
    This function takes a number as input and returns
    the times-table of that number
    '''
    times_table = []
    for i in range(1, 11):
        times_table.append([i, i*n])
    return times_table    

def print_table(table):
    ''' 
    This function takes a 2x2 table as input and print it 
    '''
    for i in range(len(t)):
        print('{0:4d}*{1:1d} {2:4d}'.format(t[i][0], N, t[i][1]))

N = input("Type the number for which you want the times_table: ")
t = times_table(N)
print_table(t)  

