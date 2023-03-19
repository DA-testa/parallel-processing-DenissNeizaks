# python3

def parallel_processing(n, m, data):
    thread_list = []
    time_list = []
    for i in range (n):
        thread_list.append(i)
        time_list.append(0)

    counter = 0
    time = 0
    for i in range (m):
        print (thread_list[counter],time_list[counter])
        while(True):
            time_list[counter] = time_list[counter] + 1
            data[i] = data[i] - 1
            if data[i] == 0:
                break
        
        counter+=1
        if counter==len(thread_list):
            counter = 0
            time+=1
#    for i in range (m):
 #       for j in range (n):
            
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    a = input()
    b=a.split()
    n = int(b[0])
    m = int(b[1])

    data = list(map(int, input().split()))




    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
