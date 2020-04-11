'''
Program - Natural Language Processing
Developer - Joydeep Banerjee
Description - The program is built to do language processing and identify the 
              main content theme or perception of a webpage that is scraped.
              The program uses BeautifulSoup and Requests libraries for scraping and 
              NLTK library for the natural language processing. 
'''

import nltk
from nltk.corpus import stopwords
import re
import scraper

def main():
    '''
    The text is the scraped content from the webpage. The text is converted to 
    all lowercase to avoid redundancy and is next cleaned off of all punctuations.
    '''

    text = scraper.wikiscraper().lower()
    clean_text = re.sub(r'[^\w]', ' ', text)
    tokens = [token for token in clean_text.split()]

    '''
    The text is splitted next into individual tokens. As a last step of data 
    preparation, the token list is scrubbed off of common English stopwords. 
    A stopword is a commonly used word (such as “the”, “a”, “an”, “in”) 
    that can be ignored to keep the token list clean and crisp.
    '''
    stpwords = stopwords.words('english')
    clean_tokens = tokens[:]

    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    frequency = nltk.FreqDist(clean_tokens)
    for k,v in frequency.items():
        print(str(k) + ':' + str(v))

    frequency.plot(15, cumulative=False) # Only plotting 15 samples here


if __name__ == "__main__":
    main()