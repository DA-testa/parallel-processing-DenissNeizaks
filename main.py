# python3

def parallel_processing(n, m, data):
    thread_list = []
    time_list = []
    output = []
    for i in range (n):
        thread_list.append(i)
        time_list.append(0)

    counter = 0
    time = 0
    for i in range (m):
        output.append (thread_list[counter])
        output.append (time_list[counter])
        while(True):
            time_list[counter] = time_list[counter] + 1
            data[i] = data[i] - 1
            if data[i] == 0:
                break
        
        counter+=1
        if counter == len(thread_list):
            counter = 0
            time+=1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    first_input = input()
    split_input = first_input.split()
    n = int(split_input[0])
    m = int(split_input[1])
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)

    
    # TODO: print out the results, each pair in it's own line
    for i in range (0,len(result),2):
        print (result[i],result[i+1])

if __name__ == "__main__":
    main()
