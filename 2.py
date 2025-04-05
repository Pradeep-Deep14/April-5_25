numbers=[1,2,3,4,5,6,7,8,9,10]
#use filter function to filter out even numbers
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)
#Output: [2, 4, 6, 8, 10]
#use filter function to filter out odd numbers  
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)
#Output: [1, 3, 5, 7, 9]