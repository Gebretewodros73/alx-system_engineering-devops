# Reddit API Advanced Tasks

This repository contains solutions for advanced tasks involving querying the Reddit API. The tasks are as follows:

## Task 0: How Many Subs?

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is given, the function should return 0.

- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.

Example usage:
```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```
## Task 1: Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

* Prototype: `def top_ten(subreddit)`
* If not a valid subreddit, print None.

Example usage:
```bash
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
... (more titles)
$ python3 1-main.py this_is_a_fake_subreddit
None
```

## Task 2: Recurse it!

Write a recursive function that queries the Reddit API and returns a list of titles for all hot articles in a given subreddit.

* Prototype: `def recurse(subreddit, hot_list=[])`
* If not a valid subreddit, return None.

Example usage:
```bash
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

## Task 3: Count it! (Advanced)

Write a recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.

* Prototype: 'def count_words(subreddit, word_list)'
Example usage:
```bash
$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
$ python3 100-main.py programming 'JavA java'
java: 54
```
