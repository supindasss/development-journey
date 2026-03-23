"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
1. Write a program to swap two tuples."""
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
print(f"the tuple before swap is T1={tuple1} and T2={tuple2}")
tuple1,tuple2=tuple2,tuple1
print(f"after swaping the tuples are t1={tuple1} T2={tuple2}")