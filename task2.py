reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good.", "excellent.", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews: 
    positive_counter = 0
    negative_counter = 0
    words_list = review.split(" ")
    for words in words_list:
        if words in positive_words:
            positive_counter += 1
        elif words in negative_words:
            negative_counter += 1
    print (f"The count of positive words in your review is {positive_counter}, and the count of negative words is {negative_counter}")