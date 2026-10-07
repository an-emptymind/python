from collections import Counter
paragraph = "To run the test, you'll be connected to Measurement Lab (M-Lab) and your IP address will be shared with them and processed by them in accordance with their privacy policy."
text = paragraph.lower()
words = [w.strip(".,!?;:()") for w in text.split()]
unique_words=set([w.strip(".,!?;:()") for w in text.split()])

print(words)

print(f"word count:{len(words)}")
print(f"Unique word count: {len(unique_words)}")

word_count=(Counter(words))
print(f"Word count: {word_count}")

top5 = word_count.most_common(5)
print(top5)



