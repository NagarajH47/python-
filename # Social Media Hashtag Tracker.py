# Social Media Hashtag Tracker

hashtags = ["#fun", "#python", "#fun", "#code", "#python"]

frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

# Most repeated hashtag
most_repeated = max(frequency, key=frequency.get)

# Unique hashtags
unique_tags = list(set(hashtags))

# Remove duplicates
removed_duplicates = []

for tag in hashtags:
    if tag not in removed_duplicates:
        removed_duplicates.append(tag)

print("Hashtags:", hashtags)
print("Most Repeated Hashtag:", most_repeated)
print("Unique Hashtags:", unique_tags)
print("Frequency of Each Hashtag:", frequency)
print("After Removing Duplicates:", removed_duplicates)