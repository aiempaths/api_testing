What this API is forThis tool looks at a short sequence of numbers (a recent window of values) and compares the shape of that sequence to similar shapes it has seen before. It then returns a simple prediction and a confidence score.It is best used when you have a single stream of numbers over time (for example sensor readings, price movements, activity levels, or any other univariate series) and you want a quick, local signal about whether the recent pattern looks more like past cases that went one way or the other.How to think about it
You send a short recent window of values (at least 6 numbers).
The system finds past windows that had a similar geometric shape.
It returns a vote based on what happened after those similar past windows, along with how confident that vote is.
