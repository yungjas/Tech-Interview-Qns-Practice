'''
WIP!!!

It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n.

Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. 

One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 

Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example:
q = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4, the queue will look like this: [1,2,3,5,4,6,7,8]. Only 1 bribe is required. Print 1

q = [4,1,2,3]
Person 4 had to bribe 3 people i.e. 1, 2, and 3 to the to the current position, Print Too chaotic

Function description:
minimumBribes takes a integer array q which shows the positions of the people after all bribes
'''

def minimumBribes(q):
    # Write your code here
    num_brides = 0
    
    for i in range(len(q)):
        if i != len(q) - 1:
            if q[i] - q[i+1] > 3:
                print("Too chaotic")
                return
            elif q[i] - i > 1:
                if q[i] > q[i+1]:
                    num_brides += 1
                if q[i] > q[i+2]:
                    num_brides += 1
                    

    print(num_brides)

if __name__ == "__main__":
	minimumBribes([2,1,5,3,4])