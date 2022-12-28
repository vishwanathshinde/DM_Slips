
colors <- c("green", "orange")
months <- c("2001", "2002", "2003")
regions <- c("Export", "Import")

Values <- matrix(c(26, 35, 32, 40, 35, 50), nrow = 2, ncol = 3, byrow = TRUE)

barplot(Values, main = "Total Impo/Export", names.arg = months, xlab = "Year", ylab = "Impo/Export", col = colors, beside = TRUE)