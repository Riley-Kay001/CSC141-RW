import random


#Review of movies

class Review:
    def __init__(self, rating, text):
        if not (0 <= rating <=5):
            raise ValueError ("Rating must be from 0 to 5.")
        self.rating = rating 
        self.text = text

    def __str__(self):
        return f"Rating: {self.rating}/5 = {self.text}"
    

#The Movie they reviewed

class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def add_review(self, reviews):
        self.reviews.append(reviews)

    def average_rating(self):
        if not self.reviews:
            return 0 
        return sum(r.rating for r in self.reviews) / len(self.reviews)
    
    def display_reviews(self):
        if not self.reviews:
            print ("No reviews have been placed yet.")
            return
        for reviews in self.reviews: 
            print(reviews)

    def best_review(self): 
        if not self.reviews:
            return None
        min_rating = min(r.rating for r in self.reviews)
        worst = [r for r in self.reviews if r.rating == min_rating]
        return random.choice(worst)
    
    def worst_review(self):
        return min(self.reviews)


#Driver Code to see if code works

movie = Movie("Notting Hill")

movie.add_review(Review(5, "The best romance movie!!"))
movie.add_review(Review(3, "Could have some more comedy in the movie to consider it a romcom."))
movie.add_review(Review(5, "Julia Roberts did great as an actor, and the movie all around was a real testiment to different lifestyles falling in LOVE!"))
movie.add_review(Review(1, "Not my kind of romance movie."))

print(f"Movie: {movie.title}")
print(f"Average Rating: {movie.average_rating():.3f}\n")

print("All Reviews:")
movie.display_reviews()

print("\nBest Review:")
print(movie.best_review())

print("\nWorst Review:")
print(movie.worst_review())