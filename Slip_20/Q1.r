a <- c("a", "b", "c", "d")

b <- c("a", "m", "c", "f")

c <- c(1, 2, 3, 4)

d <- c(9, 8, 7, 6)

ab <- data.frame(a, b, c, d)

print("Original data frame: ")
print(ab)

print("Duplicate elements of data frame: ")
print(duplicated(a, b))