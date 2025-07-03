import numpy as np

# Example 4x4 matrix representing scores of 4 students in 4 subjects
# Order: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 85, 84, 86],
    [90, 87, 80, 88],
    [83, 89, 82, 90]
])

# Step 1: Calculate average score for each subject (column-wise mean)
average_scores = np.mean(student_scores, axis=0)

# Step 2: Find the subject with the highest average score
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_index]

# Output
for i, subject in enumerate(subjects):
    print("Average score in ",subject,": ",average_scores[i])

print("\nSubject with the highest average score: ",highest_avg_subject)
