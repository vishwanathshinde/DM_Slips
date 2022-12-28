fibonacci <- numeric(20)

fibonacci[1] <- fibonacci[2] <- 1

for (i in 3:20)
{
   fibonacci[i] <- fibonacci[i - 2] + fibonacci[i - 1]
}

fibonacci