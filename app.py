
# Problem Statement: Compute the average number of books each student has read this year

student_books_list = [5, 3, 0, 7, 2, 4, 6, 8, 1, 3, 9, 5, 2, 6, 7, 4]

num_of_students = len(student_books_list)
print(f"There are {num_of_students} students in the class.")

# sum / num of students

#print(student_books_list[20])
total_books = 0
for invidual_books in student_books_list:
  total_books += invidual_books
print(f"total books {total_books}")

print(f"The averae number of books read per student is {total_books/ num_of_students :.2f}")