from reviews import neg_counter, pos_counter

review = "This crib was stable"
# calculate the P(positive) and P(negative)
# total_ reviews = len(pos_list) + len(neg_list)
# percent_pos = len(pos_list)/ total_reviews
# percent_neg = len(neg_list)/ total_reviews
percent_pos = 0.5
percent_neg = 0.5

total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())
#creating the varaibles that will track the probability
pos_probability = 1
neg_probability = 1
#spiltting the string in variable to a list of strings as values
review_words = review.split()
#looping through each word in the list review_words
for word in review_words:
  # we need to find the number of times a word "crib" appears in a positive review and likewise the same for the negative review
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  #finding each term to be multiplied together. For example, when word is "crib", smoothing out the probabilities (in case of typos or words not available in the counter)
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))

#Since both positive and negative probability of review are divided by the same denominator
# we don't need to include it as they are only used to compare rather than arranging them in order
final_pos = pos_probability * percent_pos
final_neg = neg_probability * percent_neg
print(final_pos, final_neg)
if final_pos > final_neg:
  print("The review is positive")
else:
  print("The review is negative")
