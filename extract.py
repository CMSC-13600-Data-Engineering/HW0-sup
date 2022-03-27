'''extract.py 
In this first assignment, you will learn the basics of python 
data manipulation. You will process an XML file of reddit posts 
relating to stocks and count the frequency of certain ticker
symbols appearing
'''

#Two libraries that we will need for the helper functions
import pandas as pd
from xml.dom import minidom

'''count_ticker is the main function that you will implement.

Input: filename of a reddit RSS feed in XML format
Output: dictionary mapping 
ticker symbols => frequency of occurance in the post titles

Example Usage:
>>> count_ticker('reddit.xml')
{'$HITI': 1, '$GME': 3, '$MSFT': 1, 
'$ISWH': 1, '$ARBKF': 1, '$HCANF': 1, 
'$AMC': 1, '$OZOP': 1, '$VMNT': 2, 
'$CLIS': 1, '$EEENF': 2, '$GTII': 1}

'''
def count_ticker(file):
	raise ValueError('Count Ticker Not Implemented')


# TODO1 Helper Function to Extract XML
'''_reddit_extract is a helper function that extracts 
the post title, timestamp, and link into a pandas dataframe.

Input: filename of a reddit RSS feed in XML format
Output: 3 col pandas dataframe ('title', 'updated', 'link') 
with each row a reddit post from the RSS XML file.
'''
def _reddit_extract(file):
	raise ValueError('Count Ticker Not Implemented')

#TODO2 Helper Function to Extract Tickers
'''_ticker_extract is a helper function that extracts 
the mentioned ticker symbols in each title.

Input: string representing a post title
Output: set of ticker symbols mentioned each in consistent 
notation $XYZ
'''
def _ticker_extract(title):
	raise ValueError('Count Ticker Not Implemented')
	
