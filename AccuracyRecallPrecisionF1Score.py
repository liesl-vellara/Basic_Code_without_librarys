#We’ve given you two lists. labels represents the true labels of your dataset. Each 1 represents a test that you got above a B on, and each 0 represents a test that was below a B.
labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
#guesses represents the classifications a machine learning algorithm might return. For every test, the classifier guessed whether your grade was above or below a B.
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(guesses)):
  #True Positives
  if labels[i] == 1 and guesses[i] == 1:
    true_positives += 1
  #True Negatives
  if labels[i] == 0 and guesses[i] == 0:
    true_negatives += 1
  #False Positives
  if labels[i] == 0 and guesses[i] == 1:
    false_positives += 1
  #False Negatives
  if labels[i] == 1 and guesses[i] == 0:
    false_negatives += 1
# Accuracy measures how many classifications your algorithm got correct out of every classification it made   
accuracy = (true_positives + true_negatives) / len(guesses)
print(accuracy)

#Accuracy can be an extremely misleading statistic depending on your data.
#Recall measures the percentage of the relevant items your classifier was able to successfully find.
recall = true_positives / (true_positives + false_negatives)
print(recall)

#Unfortunately, recall isn’t a perfect statistic either.
#The statistic that will help demonstrate that this algorithm is flawed is precision.
#Precision and recall are statistics that are on opposite ends of a scale. If one goes down, the other will go up.
#Therefore, precision and recall are tied to each other.
precision = true_positives / (true_positives + false_positives)
print(precision)

#It is useful to consider the precision and recall of an algorithm, however, we still don’t have one number that can sufficiently describe how effective our algorithm is.
#This is the job of the F1 score — F1 score is the harmonic mean of precision and recall. The harmonic mean of a group of numbers is a way to average them together. 
#F1 score is a combination of precision and recall.
#F1 score will be low if either precision or recall is low
f_1 = (2*precision * recall) / (precision + recall)
print(f_1)
