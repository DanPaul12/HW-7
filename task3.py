reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]


def truncated_reviews(review):
    i = 30   
    while True:
        if review[i]== " ":
            short_review = review[:i]
            return((short_review) + "...")
        elif review[i] != " ":  
            i += 1   

for review in reviews:
    print(truncated_reviews(review))