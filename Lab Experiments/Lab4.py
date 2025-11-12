import pandas as pd

# Input number of students
n = int(input())

# Read student records
records = []
for _ in range(n):
    data = input().split()
    ID = int(data[0])
    Name = data[1]
    Marks = int(data[2])
    records.append({"ID": ID, "Name": Name, "Marks": Marks})

# Create DataFrame
df = pd.DataFrame(records)
print("Initial DataFrame:")
print(df)

# Insert operation
new_data = input().split()
new_record = {"ID": int(new_data[0]), "Name": new_data[1], "Marks": int(new_data[2])}
df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
print("After Insertion:")
print(df)

# Update operation
update_data = input().split()
update_id = int(update_data[0])
new_marks = int(update_data[1])
df.loc[df["ID"] == update_id, "Marks"] = new_marks
print(f"After Update (Marks Updated for ID {update_id}):")
print(df)

# Delete operation
delete_id = int(input())
df = df[df["ID"] != delete_id]
print(f"After Deletion (Record Deleted for ID {delete_id}):")
print(df)



# A data analyst named Rehan maintains student records containing ID, Name, and Marks.

# He wants to manage this data efficiently using Python and Pandas.

# Your task is to write a program that:

# Takes a list of student records as input from the user.

# Creates a Pandas DataFrame from that list.

# Performs CRUD operations on the DataFrame as follows:

# Insert: Add a new student record.

# Update: Update the marks of a student by their ID.

# Delete: Delete a student record by their ID.

# Display the DataFrame after each operation.

# Input format :
# The first line contains an integer n, the number of students.



# The next n lines each contain student details separated by spaces:



# ID Name Marks



# Next line contains new student details to be inserted.



# Next line contains student ID and new marks for updating.



# Next line contains student ID to delete

# Output format :
# Print the DataFrame after creation, after insertion, after update, and after deletion.

# Code constraints :
# 1 ≤ n ≤ 100



# 1 ≤ ID ≤ 10^4 (unique for each student)



# Name must be a non-empty string (alphabets only).



# 0 ≤ Marks ≤ 100



# Update and delete operations assume that the provided ID exists in the dataset.

# Sample test cases :
# Input 1 :
# 3
# 201 Alice 78
# 202 Bob 82
# 203 Charlie 88
# 204 Diana 91
# 201 80
# 203
# Output 1 :
# Initial DataFrame:
#     ID     Name  Marks
# 0  201    Alice     78
# 1  202      Bob     82
# 2  203  Charlie     88

# After Insertion:
#     ID     Name  Marks
# 0  201    Alice     78
# 1  202      Bob     82
# 2  203  Charlie     88
# 3  204    Diana     91

# After Update (Marks Updated for ID 201):
#     ID     Name  Marks
# 0  201    Alice     80
# 1  202      Bob     82
# 2  203  Charlie     88
# 3  204    Diana     91

# After Deletion (Record Deleted for ID 203):
#     ID   Name  Marks
# 0  201  Alice     80
# 1  202    Bob     82
# 3  204  Diana     91