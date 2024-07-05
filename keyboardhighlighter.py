reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]


def styling_reviews(reviews):
    styled_reviews = []
    for review in reviews:
        each_word = review.split(" ")
        for word in each_word:
            if word == "good.":
                styled_reviews.append("GOOD.")
            elif word == "bad":
                styled_reviews.append("BAD")
            elif word == "excellent.":
                styled_reviews.append("EXCELLENT.")
            elif word == "Poor":
                styled_reviews.append("POOR")
            elif word == "average.":
                styled_reviews.append("AVERAGE.")
            else:
                styled_reviews.append(word)
    final_reviews = ' '.join(styled_reviews)
    print(final_reviews)
                

styling_reviews(reviews)