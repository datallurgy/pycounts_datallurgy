#!/usr/bin/env python
# coding: utf-8

# # Example usage
# 
# Here we will demonstrate how to use `pycounts_datallurgy` to count the words in a text file and plot the top 5 results.
# 
# # Imports

# In[1]:


from pycounts_datallurgy.pycounts_datallurgy import count_words
from pycounts_datallurgy.plotting_datallurgy import plot_words


# # Create text file
# 
# We'll first create a text file to work using a famous quote from Einstein:

# In[2]:


quote = "Insanity is doing the same thing over and over and              expecting different results."
with open("einstein.txt", "w") as file:
        file.write(quote)


# # Count words
# 
# We can count the words in our text using the `count_words()` function. Note that this function removes punctuation and makes all words lowercase before counting.

# In[3]:


counts = count_words("einstein.txt")
print(counts)


# # Plot words
# 
# We can now plot the results using the `plot_words()` function.

# In[4]:


fig = plot_words(counts, n=5)

