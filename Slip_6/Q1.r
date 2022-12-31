a <- c("a", "b", "c", "d")

b <- c("a", "m", "c", "f")

ab <- data.frame(a, b)

print("Original data frame: ")
print(ab)

print("Duplicate elements of data frame: ")
print(duplicated(ab))