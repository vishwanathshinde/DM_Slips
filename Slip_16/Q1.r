colors <- c("green", "orange")

months <- c("2001", "2002", "2003")

Values <- matrix(c(26, 35, 32, 40, 35, 50), nrow = 2)

barplot(Values, main = "Total Impo/Export", names.arg = months, xlab = "Year", ylab = "Impo/Export", col = colors, beside = TRUE)