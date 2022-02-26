# qn link: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        padding = len(bin(number)[2:])
        
        # for rjust method, need to put " " so that it will input the number of spaces according to the length of the binary of the input
        print(str(i).rjust(padding), end=" ")
        print(oct(i)[2:].capitalize().rjust(padding), end=" ")
        print(hex(i)[2:].rjust(padding), end=" ") 
        print(bin(i)[2:].rjust(padding), end=" ")
        print("")

if __name__ == "__main__":
    num_str = input("Please input a number between 1 and 99: ")
    num = int(num_str)
    print_formatted(num)