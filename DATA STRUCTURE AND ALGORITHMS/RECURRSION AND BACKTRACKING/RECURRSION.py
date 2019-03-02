## recurrsion
#always see the two things 1-->base case 2->> recurrsive property

# Q1 factorial of a number
def fact(n):
    #base case:
    if n==0:
        return 1
    else:
        return n*fact(n-1)

# Q2 power of a number
def pow(x,n):
    #base case
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)

## Q3 lenth of a string

def str_len(s):
    #base case:
    if s=="":
        return 0
    #recurrsive property
    else:
        return 1+str_len(s[1:])
##Q4 reverse of a string

def rev_str(s):
    #base case
    if s=="":
        return ""
    #recurrsive prooperty
    else:
        return rev_str(s[1:]) +s[0]

#q5 print first N odd natural number

print(fact(5))
print(pow(4,3))
print(str_len("abcd"))
print(rev_str("abcd"))
