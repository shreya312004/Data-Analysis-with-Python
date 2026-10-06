import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\New Data AA\New_Training\Shreya\airlines_flights_data.csv")

print(data.head())

print(data.tail())

print(data.info())

print(data.describe())

print(data.isnull().sum())

print(data.duplicated().sum())

#q1: Find frequency of each airline
airline_frequency = data["airline"].value_counts()

print(airline_frequency)

#q2 Count flights for each departure time
departure_frequency = data["departure_time"].value_counts()

# Create bar graph
plt.figure(figsize=(10, 5))
departure_frequency.plot(kind="bar")

plt.title("Number of Flights by Departure Time")
plt.xlabel("Departure Time")
plt.ylabel("Number of Flights")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Count flights for each arrival time
arrival_frequency = data["arrival_time"].value_counts()

# Create bar graph
plt.figure(figsize=(10, 5))
arrival_frequency.plot(kind="bar")

plt.title("Number of Flights by Arrival Time")
plt.xlabel("Arrival Time")
plt.ylabel("Number of Flights")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#q3: graph for source and destination city frequency
# --------------------------------
# Source City
# --------------------------------

source_frequency = data["source_city"].value_counts()

plt.figure(figsize=(10, 5))
source_frequency.plot(kind="bar")

plt.title("Flight Frequency by Source City")
plt.xlabel("Source City")
plt.ylabel("Number of Flights")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# --------------------------------
# Destination City
# --------------------------------

destination_frequency = data["destination_city"].value_counts()

plt.figure(figsize=(10, 5))
destination_frequency.plot(kind="bar")

plt.title("Flight Frequency by Destination City")
plt.xlabel("Destination City")
plt.ylabel("Number of Flights")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#q4: Calculate average price for each airline
average_price = data.groupby("airline")["price"].mean().sort_values(ascending=False)

print("Average Price by Airline:")
print(average_price)

# Create bar graph
plt.figure(figsize=(10, 5))
average_price.plot(kind="bar")

plt.title("Average Flight Price by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Price")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#q5: Create pivot table
price_table = data.pivot_table(
    values="price",
    index="departure_time",
    columns="arrival_time",
    aggfunc="mean"
)

plt.figure(figsize=(12, 7))

plt.imshow(price_table, aspect="auto")

plt.colorbar(label="Average Ticket Price")

plt.xticks(
    range(len(price_table.columns)),
    price_table.columns,
    rotation=45
)

plt.yticks(
    range(len(price_table.index)),
    price_table.index
)

plt.title("Average Ticket Price: Departure Time vs Arrival Time")
plt.xlabel("Arrival Time")
plt.ylabel("Departure Time")

plt.tight_layout()
plt.show()

# qCreate route
data["route"] = (
    data["source_city"] + " → " + data["destination_city"]
)

# Calculate average price
route_price = (
    data.groupby("route")["price"]
    .mean()
    .sort_values(ascending=False)
)

# Select top 10 expensive routes
top_routes = route_price.head(10)

# Plot
plt.figure(figsize=(12, 6))

plt.plot(
    top_routes.index,
    top_routes.values,
    marker="o"
)

plt.title("Top 10 Routes by Average Ticket Price")
plt.xlabel("Source → Destination")
plt.ylabel("Average Ticket Price")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# q7:Select only tickets bought 1 or 2 days before departure

average_price = (
    data.groupby("days_left")["price"]
    .mean()
    .sort_index()
)

print(average_price)

# Line graph
plt.figure(figsize=(10, 6))

plt.plot(
    average_price.index,
    average_price.values,
    marker="o"
)

plt.title("Average Ticket Price vs Days Left Before Departure")
plt.xlabel("Days Left Before Departure")
plt.ylabel("Average Ticket Price")

plt.grid(True)
plt.tight_layout()
plt.show()

#q8: Compare ticket prices for Economy and Business class
economy_price = data[data["class"] == "Economy"]["price"]
business_price = data[data["class"] == "Business"]["price"]

plt.figure(figsize=(10, 6))

plt.hist(
    economy_price,
    bins=30,
    alpha=0.6,
    label="Economy"
)

plt.hist(
    business_price,
    bins=30,
    alpha=0.6,
    label="Business"
)

plt.title("Ticket Price Distribution: Economy vs Business")
plt.xlabel("Ticket Price")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()

# q9:Filter Vistara Delhi → Hyderabad
filtered_data = data[
    (data["airline"] == "Vistara") &
    (data["source_city"] == "Delhi") &
    (data["destination_city"] == "Hyderabad")
]

# Average price by class
average_price = filtered_data.groupby("class")["price"].mean()

print(average_price)

# Pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    average_price.values,
    labels=average_price.index,
    autopct="%1.1f%%"
)

plt.title(
    "Average Ticket Price Distribution\n"
    "Vistara: Delhi to Hyderabad"
)

plt.show()