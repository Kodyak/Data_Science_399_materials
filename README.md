# datascience_2
Supplemental code for datascience 2 class (focus on NLP & implementing standard algorithms)

week-by-week breakdown of code:

Week1: Build and implement basic KNN predictor on sample Titanic passenger list dataset, to predict survival on name length / 'bag of characters' approach.

Week2: Build text parser to identify hate tweets from twitter data. Combined text parser with KNN from week1 using cosine-similarity metric. Used random sampling to evaluate KNN performance on a 32K tweet dataset - ran up against time inefficiency of KNN. Even restricting to random subsets of the data, KNN predictions I believe took on the order of 29 minutes. Also, poor (only ~50%) accuracy.

Week3: Build a flexible Naive Bayes function predict probabilities of a given tweet belonging to different categories (hate / not-hate tweets, but could use it on ≥ 3 classes). For now, Bayes computes probabilities using hashtag associations (with tweets belonging to diff classes) as 'evidence'. Achieved ~98% success on the dataset, and by building the complete hash table first, predictions for the entire 32K tweets can be computed in only 2.5 seconds.

Week4: Implement Naive Bayes for predicting text authorship using Multinomial event model to build a bag_of_words from books by 3 'gothic authors'. Achieved 94% accuracy predicting authorship from a sentence. Also implemented Naive Bayes with Bernoulli event model (only practical for predictions on small documents however, since the lookup scans over the entire bag_of_words).

Week5: Extend the bag_of_words to create document vectors, and use cosine similarity as a measure for comparing texts by various authors. Implemented a 'generate_dict' function to extract tokenized words and counts from a text (based on static given bag_of_words although in the future it would make sense to modify bag_of_words to not be static), and wrap this in a check_book function which scrapes text (.txt file) from a url and outputs cosine similarity agains the three 'gothic authors' (used to build bag_of_words).

/*/ Midterm1 Posted /*/ - implemented TF-IDF as part of the midterm. uploaded partial draft file for the midterm

Week6:

