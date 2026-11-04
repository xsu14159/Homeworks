## Process

1. Set up the folder structure and files in VS Code.
2. Created a virtual environment and installed pandas, numpy, and matplotlib.
3. Downloaded the data with `curl` and added it to `.gitignore`.
4. Inspected the data with `info()` and `head()`.
5. Found that the count columns were floats because of missing values, so I converted them to `Int64`.
6. Found that the `Date` format is `MM/DD/YYYY hh:mm:ss AM/PM`, so I sliced the string to get the year and converted the 12-hour clock to a 24-hour hour.
7. Filtered the 2016 data, counted and dropped rows with missing values.
8. Plotted total counts by hour and saved the figure.
9. Used `groupby` and `idxmax()` to find the busiest hour on average.

## AI Use

I used Claude to guide me through the setup, explain pandas and shell commands, and help write and debug the code.