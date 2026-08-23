Amazon Sales Data Analysis

This project analyzes ~121,000 real Amazon orders (March–June 2022) to understand revenue distribution, sales trends over time, and order fulfillment outcomes.

Key Findings:

"Set" was by far the top revenue-generating category, while categories like Dupatta and Saree contributed almost nothing.
Monthly sales peaked in April, then gradually declined through May and June.
The vast majority of orders were successfully shipped or delivered; cancellations made up a small portion of total orders, and other issues (returns, damage, lost items) were negligible.
The dataset also contained a data quality issue: roughly 200+ orders marked "Shipped" had no recorded sale Amount — worth flagging as an inconsistency rather than treating as clean data.

Tools used: Python, Pandas, Matplotlib (in VS Code)


