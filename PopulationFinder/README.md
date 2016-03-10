# Population Finder

I saw this in an article about possible interview questions.  So, in my quest to learn Python, I attempted to solve it.  

As stated: 'Given a group of people with their birth years and death years, find the year with the highest population'

I assume that the set of people is a list of lists of the form:

  ```people = [ [birth_year, death_year],
       [birth_year, death_year],
       [etc.],```

#### Known issues
1. No checking to verify that birth year comes BEFORE death year
2. Keeping track of year over year changes and then accumulating the changes through the whole list of years may not be the best way to keep track of everything.
  * What happens if I add people later?  
  * Does rebuilding the year, population data take too much time once the data set is big?
