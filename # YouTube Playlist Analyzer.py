# YouTube Playlist Analyzer

videos = [12, 4, 8, 15, 3, 20]

total_time = sum(videos)
longest_video = max(videos)
average = total_time / len(videos)

short_videos = []

for v in videos:
    if v < 5:
        short_videos.append(v)

print("Video Durations:", videos)
print("Total Watch Time:", total_time, "minutes")
print("Longest Video:", longest_video, "minutes")
print("Average Duration:", average, "minutes")
print("Videos shorter than 5 minutes:", short_videos)