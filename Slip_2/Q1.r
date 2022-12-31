mult_table <- function(n) {
    for (i in 1:10)  {
        cat(n, "X", i, "=", n * i, "\n")
    }
}
mult_table(9)