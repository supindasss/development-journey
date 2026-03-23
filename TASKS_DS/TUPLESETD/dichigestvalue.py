"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
13. Given a dictionary, print the key with the highest value."""
name={"supin":82,
      "das":72,
      "raju":92,
      "chandru":99}
if name:
    highest=max(name,key=name.get)
    print(highest)
        
