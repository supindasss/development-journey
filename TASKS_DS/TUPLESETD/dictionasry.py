"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
11. Create a dictionary of student names and marks. Print students who scored above 75."""
student_score={
    "Arjun":82,
    "supin":65,
    "raju":88,
    "chandru":72,
    "vipin":90,
    "anas":78
}
high_score={name:score for name,score in student_score.items() if score>75}
print(high_score)