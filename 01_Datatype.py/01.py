#Program-1
print("Let's start the fun")
print("Welcome","Just Enjoy", sep=" & ")
print("1","2","3","4", sep="@")

#Program-2 Multiple line command
nm = input("Enter your name:")
age = input("Enter your age")
print(nm,age,sep="\n")

#Program-3
age = int(input("Enter your age:"))
print("After 20 years you will be",age+20)
print(type(nm))
print(type(age))

#Program-4
marks = [78, 85, 98, 76] # Integres 
Average = sum(marks)/len(marks)  # float 
print("Average Score:",Average)

#Program-5
name = "Jayshree"
subject = "Python"
message = f"Hello {name}, you are learning {subject}"
print(message)

#Program-6
score = 25
passed = score >= 30 # boolean
print(passed)

#Program-7 - Sequence
print("aditi", "chandni", "harsh", "joshwa")

#Program-8 - dictionary 
students = {
    "aditi": 20,
    "chandni": 21,
    "harsh": 22,
    "joshwa": 23
}
for chandni in students:
    print(chandni)

# Sequence datatype with append, slicing and range
# List (mutable sequence)
students = ["aditi", "chandni", "harsh", "joshwa"]
print("List of students:",students)
students.append("jayshree") # add new element to the list

print("Updated List:",students)
print("student", students[0])   # access the first element of the list

# Range Datatype
for i in range(5):
    print(i)

for i in range(2,7):
    print(i)

for i in range(2,7,2):
    print(i)

