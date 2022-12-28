x <- c(84, 24, 72, 36, 48, 96)

labels <- c(1, 2, 3, 4, 5, 6)

pie(x, labels, main = "Frequency of getting each number on dice", col = rainbow(length(x)))