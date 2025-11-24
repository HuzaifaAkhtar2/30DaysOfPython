from requests import *
from json import *
from statistics import *

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cats_api = get("https://api.thecatapi.com/v1/breeds").json()
weights = []
for i in cats_api:
    weight = i["weight"]["metric"]
    parts = weight.split(" - ")
    first = float(parts[0])
    second = float(parts[1])
    avg = (first + second) / 2
    weights.append(avg)

lifespans = []
for i in cats_api:
    lifespan = i["life_span"]
    parts = lifespan.split(" - ")
    first = float(parts[0])
    second = float(parts[1])
    avg = (first + second) / 2
    lifespans.append(avg)

# the min, max, mean, median, standard deviation of cats' weight in metric units.
min_weight = min(weights)
max_weight = max(weights)
mean_weight = mean(weights)
median_weight = median(weights)
std_weight = stdev(weights)
print("WEIGHT (kg)")
print("Min:", int(min_weight))
print("Max:", int(max_weight))
print("Mean:", int(mean_weight))
print("Median:", int(median_weight))
print("Standard Deviation:", int(std_weight))

# the min, max, mean, median, standard deviation of cats' lifespan in years.
min_life = min(lifespans)
max_life = max(lifespans)
mean_life = mean(lifespans)
median_life = median(lifespans)
std_life = stdev(lifespans)
print("\nLIFESPAN (years)")
print("Min:", int(min_life))
print("Max:", int(max_life))
print("Mean:", int(mean_life))
print("Median:", int(median_life))
print("Standard Deviation:", int(std_life))

# Create a frequency table of country and breed of cats
country_table = {}
for cat in cats_api:
    country = cat.get("origin", "Unknown")
    breed = cat["name"]
    if country not in country_table:
        country_table[country] = []
    country_table[country].append(breed)
print("\nCountry : Breed")
for i, j in country_table.items():
    print(i, ":", j)