"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
15. Write a program to sort a dictionary by its values."""
name={"supin":55,
      "das":100,
      "raju":40,
      "chandru":9}
orders_list=[[v,k] for k,v in name.items()]
print(sorted(orders_list))
