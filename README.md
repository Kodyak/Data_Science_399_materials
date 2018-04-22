# datascience_2
Supplemental code for datascience 2 class (focus on NLP & implementing standard algorithms)

Week1: Build and implement basic KNN predictor on sample Titanic passenger list dataset, to predict survival on name length / 'bag of characters' approach.

Week2: Build text parser to identify hate tweets from twitter data. Combined text parser with KNN from week1 using cosine-similarity metric. Used random sampling to evaluate KNN performance on a 32K tweet dataset - ran up against time inefficiency of KNN.

Week3: Build a flexible Naive Bayes function predict probabilities of a given tweet belonging to different categories (hate / not-hate tweets, but could use it on ≥ 3 classes). For now, Bayes computes probabilities using hashtag associations (with tweets belonging to diff classes) as 'evidence'. Achieved ~98% success on the dataset.