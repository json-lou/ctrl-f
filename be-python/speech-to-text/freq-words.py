# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:17:06 2019

@author: rk549
"""

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

  
example_sent = "Hey so let's get started us so welcome to the second of the learning how to learn seminar series %HESITATION if you don't know my name is Dan well took and I'm a lecturer here and the faculty of mathematics and today I have the pleasure to talk to you about how to think about your thinking so I'm a lot of people I consider this ability to think about your thinking to be one of the most important skills you can have in every aspect of your life of course for our purposes today I will mostly focus on how we can use thinking about your thinking out super improve your academics so first a question for you %HESITATION how many of you have experienced this "
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens:
    if w == "HESITATION" or w == "%" or w == "I" or w == "'m":
        continue;
    elif w not in stop_words: 
        filtered_sentence.append(w) 
        
words = filtered_sentence

# Get the set of unique words.
uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

# Make a list of (count, unique) tuples.
counts = []
for unique in uniques:
  count = 0              # Initialize the count to zero.
  for word in words:     # Iterate over the words.
    if word == unique:   # Is this word equal to the current unique?
      count += 1         # If so, increment the count
  counts.append((count, unique))

counts.sort()            # Sorting the list puts the lowest counts first.
counts.reverse()         # Reverse it, putting the highest counts first.
# Print the ten words with the highest counts.
for i in range(min(10, len(counts))):
  count, word = counts[i]
  print(word)
  #ABOVE "WORD" REPRESENTS THE MOST FREQUENT KEYWORD SORTED IN ORDER

# Prints out array without stop words
print(filtered_sentence) 
