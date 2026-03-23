"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
3. Given a tuple of integers, create a new tuple with only even numbers."""
tuple1=(1,2,3,4,5,6,7,8,9,10)
tuple_even=tuple(num for num in tuple1 if num%2==0 )
print(tuple_even)
