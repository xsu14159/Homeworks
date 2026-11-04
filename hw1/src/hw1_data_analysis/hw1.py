"""HW1: python data analysis basics."""
import pandas as pd
import matplotlib.pyplot as plt
# Part 1: Read the CSV file into a pandas dataframe. (1pt)
data_bicycle = pd.read_csv("hw1/src/hw1_data_analysis/bicycle_data.csv")

# Part 2: In a comment, describe the columns in the dataframe and what data types they should be.
# If the data types in the dataframe do not match what you think they should be, update them. (1pt)

# There are four columns in the dataframe:
# 1. Date: The date of the observation. Data type is string.
# 2. Total: The total number of bicycles observed (East + West). Data type is float.
# 3. West: The number of bicycles observed on the west side. Data type is float.
# 4. East: The number of bicycles observed on the east side. Data type is float.
# These counts should be integers but were read as floats
for col in data_bicycle.columns[1:]:
    data_bicycle[col] = data_bicycle[col].astype("Int64")

# Part 3: Add columns to the dataframe containing:
# The total (East + West) bicycle count. (1pt)
# The hour of the day. (1pt)
# The year. (1pt)
EAST = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk" # Column name for the east side bicycle counts
WEST = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk" # Column name for the west side bicycle counts
# Add a column for the total bicycle count (East + West)
data_bicycle["Total"] = data_bicycle[EAST] + data_bicycle[WEST] 
# Hour of the day (0-23): hh % 12 turns 12 into 0, then add 12 for PM.
hour_12 = data_bicycle["Date"].str[11:13].astype(int) % 12
is_pm = data_bicycle["Date"].str[-2:] == "PM"
data_bicycle["Hour"] = hour_12 + 12 * is_pm.astype(int)
# Year
data_bicycle["Year"] = data_bicycle["Date"].str[6:10].astype(int)

print(data_bicycle)

# Part 4: Create a new dataframe with the subset of data from
# the year 2016. (1pt)
data_2016 = data_bicycle[data_bicycle["Year"] == 2016].copy()
print(data_2016)

# Part 5: For the dataframe you created in 4, are there any time
# points with missing data? If so, make sure missing data does not
# impact parts 6 and 7. In a comment, write the number of missing
# time points. (1pt)
print(data_2016["Total"].isna().sum())
# There are 1 time points with missing data in 2016.
# Drop the rows with missing data to ensure they do not impact Parts 6 and 7.
data_2016 = data_2016.dropna(subset=["Total"])

# Part 6: For the dataframe you created in 4, use pandas and
# matplotlib to plot counts by hour: hour of the day on the x-axis
# and total daily counts on the y-axis. Add an appropriate title,
# label the axes, and save the image as counts_by_hour.png. (1pt)
ax = data_2016.groupby("Hour")["Total"].sum().plot(kind="bar")
ax.set_title("Fremont Bridge Bicycle Counts by Hour of Day (2016)")
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Total Bicycle Count")
plt.tight_layout()
plt.savefig("hw1/src/hw1_data_analysis/counts_by_hour.png")

# Part 7: For the dataframe you created in 4, use Python and pandas
# to determine the average busiest hour of the day computationally.
# In a comment, write the busiest hour. (1pt)
print(data_2016.groupby("Hour")["Total"].mean().idxmax())

# The busiest hour of the day on average is 17:00.

# Part 8: Describe your process for doing this homework. If you used
# an AI assist, include that here. Edit the README.md file to answer
# this question. (1pt)

# See README.md for a detailed description of the process.