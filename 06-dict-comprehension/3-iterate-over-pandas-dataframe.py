student_dict = {
    "student": ["Karan", "Khushi", "Priyanka"],
    "score": [56, 76, 89]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# loop through rows of data frame

for (index, row) in student_data_frame.iterrows():
    print(row["student"])
    print(row["score"])