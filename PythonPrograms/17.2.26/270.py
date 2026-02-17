
#* find sum of even numbers at even positions

def summate_even_numbers(lst):
    sum1 = 0
    for i in range(0,len(lst),2):
        if lst[i]%2==0:
            sum1 += lst[i]

    return sum1

print(summate_even_numbers([0,1,2,3,4,5,6]))