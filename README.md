# Homework 1. Introduction to Data Extraction
In this assignment, you will extract meaningful information from unstructured data.

Due Date: *Monday April 4, 2021 11:59 pm*

## Initial Setup
These initial setup instructions assume you've done ``HW0``. Like before, you need to first accept the assignment and clone your repository:
```
https://classroom.github.com/a/Q7PBqqHQ
```
In this homework assignment, you will only modify ``extract.py``. Once you are done, you must add 'extract.py' to git:
```
$ git add extract.py 
```
After adding your files, to submit your code you must run:
```
$ git commit -m"My submission"
$ git push
```
We will NOT grade any code that is not added, committed, and pushed to your submission repository. You can confirm your submission by visiting the web interface[https://mit.cs.uchicago.edu/cmsc13600-spr-20/skr]

## Background
RSS  is a web standard that allows users and applications to access updates to websites in a standardized, computer-readable format. These feeds can, for example, allow a user to keep track of many different websites in a single news aggregator. The news aggregator will automatically check the RSS feed for new content, allowing the list to be automatically passed from website to website or from website to user. 
Recent events have shown how important tracking online media is for financial markets. 

In this project, you will scan through a series of reddit posts and count the frequency that certain stock ticker symbols are mentioned. You're essentially implementing one important function that scans through posts in an XML file of posts and returns the number of posts in which a ticker symbol occurs:
```
>>> count_ticker('reddit.xml')
{'$HITI': 1, '$GME': 3, '$MSFT': 1, '$ISWH': 1, '$ARBKF': 1, '$HCANF': 1, '$AMC': 1, '$OZOP': 1, '$VMNT': 2, '$CLIS': 1, '$EEENF': 2, '$GTII': 1}
```
However, before we get there we will break the implemention up into a few smaller parts.

## Data Files
You are given a data file to process `reddit.xml`.  This file contains an RSS feed taken from a few Reddit pages covering stocks. RSS feeds are stored in a semi-structured format called XML. XML defines a tree elements, where you have items and subitems (which can be named). This example is shamelessly taken from this link: https://stackabuse.com/reading-and-writing-xml-files-in-python/
```
<data>
    <items>
        <item name="item1">item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>
```
These tags can be extracted using built in modules in most programming languages. Let's what happens when we process this with python. I stored the above data in a test file (also included) test.xml. We can first try to extract the *item* tags.
```
from xml.dom import minidom

mydoc = minidom.parse('test.xml')
items = mydoc.getElementsByTagName('item')
for elem in items:
    print(elem.firstChild.data)
```
The code above: (1) gets all the tags labeld *item*, (2) then iterates those those items, (3) gets the child data aka the data contained between `> * </`. The output is:
```
item1abc
item2abc
```
If I wanted to grab the names instead, I could write the following code:
```
from xml.dom import minidom

mydoc = minidom.parse('test.xml')
items = mydoc.getElementsByTagName('item')
for elem in items:
    print(elem.attributes['name'].value)
```
The code above: (1) gets all the tags labeld *item*, (2) then iterates those those items, (3) gets the attribute data aka the data contained in `< * attr=value > `.


### TODO 1. Extract Title, Links, and Post Times
Your first todo will be to use the examples above to extract *titles*,
```
<title>$EEENF Share Price Valuation Model | Low Range Estimate increase of 1700% in Current Share Price Equaling $0.49 Per Share| Average Range Estimate Increase in Current Share Price of 3600% Equaling $1.05 Per Share</title>
```
then extract *links* (only extract the URL),
```
<link href="https://www.reddit.com/r/pennystocks/comments/mdexsk/eeenf_share_price_valuation_model_low_range/" />
```
and *post times* for each reddit post in the RSS feed:
```
<updated>2021-03-26T02:44:10+00:00</updated>
```
It is up to you to read the documentation on the python xml module if you are confused on how to use it. You must write a helper function:
```
def _reddit_extract(file)
```
That returns a Pandas DataFrame with three columns (*title*, *link*, *updated*). On `reddit.xml` your output should be a 25 row, 3 column pandas data frame. 
Hint: if you are getting 26 rows, you are probably extracting the first dummy header row as well--this can be safely skipped.

### TODO 2. Extract Ticker Symbols
Each title of a reddit post might mention a stock of interest and most use a consistent format to denote a ticker symbol (starting with a dollar sign). For example: "$ISWH Takes Center Stage at Crypto Conference". You will now write a function called extract ticker which given a single title extracts all of the ticker symbols present in the title:
```
def _ticker_extract(title)
```

## TODO 3. Count Ticker Frequency
Using the two helper functions you defined above. Finally, you will count the frequency (the number of posts) in which each ticker symbol occurs. 
```
def count_ticker(file)
```
Your result should be a dictionary of ticker to count and look as follows:
```
>>> count_ticker('reddit.xml')
{'$HITI': 1, '$GME': 3, '$MSFT': 1, '$ISWH': 1, '$ARBKF': 1, '$HCANF': 1, '$AMC': 1, '$OZOP': 1, '$VMNT': 2, '$CLIS': 1, '$EEENF': 2, '$GTII': 1}
```

## Testing
We've provided a sample dataset ``reddit.xml`` which can be used to test your code by seeing if you can reproduce the output above. We have also provided an autograder that will check for some basic issues. 
