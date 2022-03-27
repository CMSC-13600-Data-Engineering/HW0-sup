from extract import _reddit_extract, \
						_ticker_extract, \
						count_ticker


def testExtraction():
	df = _reddit_extract('reddit.xml')

	try:
		cols = list(df.columns.values)
		cols.sort()
	except:
		return "[ERROR] The output of _reddit_extract doesn't look like a dataframe"

	if cols != ['link', 'title', 'updated']:
		return "[ERROR] Expected ['link', 'title', 'updated'], got = " + str(cols)

	N = len(df)

	if N != 25:
		return "[ERROR] Seems like you have too many rows"

	return "[PASSED] testExtraction()"

def testTicker():
	ticker = "The quick $BRWN fox jumped over the $LZY $DAWG"
	val = _ticker_extract(ticker)
	expected = set(['$BRWN','$LZY','$DAWG'])

	if val != expected:
		return "[ERROR] Expected set(['$BRWN','$LZY','$DAWG']), got = " + str(val)

	return "[PASSED] testTicker()"


def testAll():
	expected = {'$HITI': 1, '$GME': 3, '$MSFT': 1, '$ISWH': 1, \
			    '$ARBKF': 1, '$HCANF': 1, '$AMC': 1, '$OZOP': 1, \
			    '$VMNT': 2, '$CLIS': 1, '$EEENF': 2, '$GTII': 1}

	val = count_ticker('reddit.xml')
	if expected != val:
		return "[ERROR] Expected " + str(expected) + " , got = " + str(val)

	return "[PASSED] testAll()"

print(testExtraction())
print(testTicker())
print(testAll())

