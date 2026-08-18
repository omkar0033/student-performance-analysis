import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("student_data.csv")

# Display basic information
print("Student Performance Analysis")
print("-" * 30)

print("\nFirst 5 Records:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

# Student with highest marks
top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Performing Student:")
print(top_student)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("student_performance.png")
plt.show()
