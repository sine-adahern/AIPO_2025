"""
0 means no seismic activity while 1 senses an earth movement, an earthquake is identified as a sequence of 1-s
that follows at least 2 0-s and is followed by at least 2 0-s. For example, 01001111011 does not show
any earthquake, while 010011110011 identifies one earthquake of length 4.
Given a sequence of 0-s and 1-s from one seismometer, you are required to write a program to
find the maximum duration of an earthquake expressed in seconds.


"""


n = (input())

num_list = []

for i in n:
    num_list.append(int(i))
    
#print(num_list)

a = num_list[0]
b = num_list[1]


turn = 0
eq = False
eq_counter = 0
eq_list = [0]


while turn < (len(num_list)-2):
    if ((a+b) == 0) or eq == True:
        eq  = True 
        a = b
        b = num_list[turn+2]
        if (b ==1) and (a == 1 or a == 0):
            eq_counter += 1
    else: 
        eq = False
    
    if(eq == True) and (a == 1 and b == 0):
        eq = False
        eq_list.append(eq_counter)
        eq_counter = 0
        
        

    a = b
    b = num_list[turn+2]
    turn += 1
    
print(max(eq_list))

