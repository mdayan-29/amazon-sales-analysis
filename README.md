Amazon Sales Data Analysis

This project analyzes ~121,000 real Amazon orders (March–June 2022) to understand revenue distribution, sales trends over time, and order fulfillment outcomes.

Key Findings:

"Set" was by far the top revenue-generating category, while categories like Dupatta and Saree contributed almost nothing.
Monthly sales peaked in April, then gradually declined through May and June.
The vast majority of orders were successfully shipped or delivered; cancellations made up a small portion of total orders, and other issues (returns, damage, lost items) were negligible.
The dataset also contained a data quality issue: roughly 200+ orders marked "Shipped" had no recorded sale Amount — worth flagging as an inconsistency rather than treating as clean data.

Tools used: Python, Pandas, Matplotlib (in VS Code)

This is stronger than project 1's write-up in one way — you caught and reported an actual data quality issue, which is a genuinely valuable analyst skill.

Same as before, this goes in your README.md on a new GitHub repo. Want to walk through GitHub setup again (repo → README → upload files), or do you remember the steps from last time and just want confirmation as you go?

what will be the repository name

Something clear and descriptive works best — recruiters/visitors should understand what it is just from the name. I'd suggest:

amazon-sales-analysis

Clean, lowercase, hyphens instead of spaces (GitHub convention), and immediately tells anyone what the project is about — matches the style of your first repo (personal-finance-analysis) too, so your profile looks consistent.


