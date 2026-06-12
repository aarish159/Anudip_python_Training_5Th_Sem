# Problem 9: Social Media Trend Analyzer

def analyze_hashtags():
    try:
        # Step 1: Read hashtags from file
        with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_challenge-3\hashtags.txt", "r") as f:
            hashtags = f.read().split()

        # Step 2: Count occurrences
        freq = {}
        for tag in hashtags:
            if tag in freq:
                freq[tag] += 1
            else:
                freq[tag] = 1

        # Step 3: Find top trending hashtag(s)
        max_count = max(freq.values())
        top_trending = [tag for tag, count in freq.items() if count == max_count]

        # Step 4: Create set of unique hashtags
        unique_hashtags = set(freq.keys())

        # Step 5: Identify hashtags used more than twice
        popular_hashtags = [tag for tag, count in freq.items() if count > 2]

        # Step 6: Generate trend report file
        with open("trend_report.txt", "w") as f:
            f.write("Hashtag Frequency:\n")
            for tag, count in freq.items():
                f.write(f"{tag} : {count}\n")
            f.write("\nTop Trending Hashtags: " + " ".join(top_trending) + "\n")
            f.write("Unique Hashtags: " + str(unique_hashtags) + "\n")
            f.write("Hashtags Used More Than Twice: " + " ".join(popular_hashtags) + "\n")

        # ---- Output ----
        print("Hashtag Frequency:")
        for tag, count in freq.items():
            print(f"{tag} : {count}")

        print("Top Trending Hashtags:", " ".join(top_trending))
        print("Unique Hashtags:", unique_hashtags)
        print("Hashtags Used More Than Twice:", " ".join(popular_hashtags))
        print("Trend Report Generated Successfully.")

    except FileNotFoundError:
        print("Error: hashtags.txt not found.")
    except Exception as e:
        print("Error occurred:", e)


# ---- Driver Code ----
analyze_hashtags()
