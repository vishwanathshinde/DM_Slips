rev_number <- function(n) {
    rev <- 0
    r <- 0
    sum <- 0
    while (n > 0) {
        r <- n %% 10
        sum <- sum + r
        rev <- rev * 10 + r
        n <- n %/% 10
    }
    cat("Reverse no is: ", rev)
    cat("\nSum of digit is ", sum)
}

rev_number(123)