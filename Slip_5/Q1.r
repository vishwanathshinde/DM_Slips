stud_name <- c("Ram", "Sham", "Karan", "arjun")

factor(stud_name)

roll_no <- c(1, 2, 3, 4)

factor(roll_no)

combined <- factor(c(stud_name, roll_no))

print("Combined factor is: ")
print(combined)