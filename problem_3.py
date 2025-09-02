"""
0 means no seismic activity while 1 senses an earth movement, an earthquake is identified as a sequence of 1-s
that follows at least 2 0-s and is followed by at least 2 0-s. For example, 01001111011 does not show
any earthquake, while 010011110011 identifies one earthquake of length 4.
Given a sequence of 0-s and 1-s from one seismometer, you are required to write a program to
find the maximum duration of an earthquake expressed in seconds.

"""


n = int(input())

s_a = []

s_l = input()

for i in s_l:
    s_a.append(i)

print(s_a)

a = s_a[0]
b = s_a[1]
c = s_a[2]

one_count = 0
counter = 0
total_eq = 0

i = 0

yes_eq = False

while counter < (len(s_a)-3):
    if yes_eq == False:
        if a == 0 and b == 0  and c == 1:
            yes_eq = True
            one_count+=1
        else:
            yes_eq = False

    if yes_eq == True:
        if (a == 0 or a == 1)and b == 1 and c == 1:
            one_count+=1
            yes_eq = True

        elif a==1 and b == 0 and c == 0:
            yes_eq = False
            total_eq == one_count

        elif (a == 0 or a == 1)and b == 1 and c == 0:
            yes_eq = False


    
    a = b
    b = c
    c = s_a[counter+3]
    counter+=1

print(total_eq)




