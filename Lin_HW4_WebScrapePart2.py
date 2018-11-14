"""
Created on Wed Nov 30 @way too late in th evening O'clock 2017

@author: Eric
"""
# INSTRUCTIONS: In the code below you will find each code
# section has either a "BONUS" or a "REQUIRED" comment tag
# at the front. If it has a "REQUIRED" comment tag, then it is
# part of the homework assignment and you must provide comments
# interpretting that portion of the code. Ideal comments will
# indicate what the code is for and, if it is a function, what
# the function does, what it takes in as input (if anything) and what
# it provides as output (if anything)
# The "BONUS" sections carry the same comment requirements but
# are NOT REQUIRED for a full score...however, they allow for
# extra points. The "BONUS" sections are ones you may not be familiar with.
# HINT: duckduckgo.com is YOUR FRIEND, there is NO SHAME in using
# any resources available to you to UNDERSTAND something.

# REQUIRED
import urllib.request # help in opening URLs  
import urllib.parse # help parse URLs into components 
from bs4 import BeautifulSoup # help pulling data out of HTML(used in this script) and XML files 
import re # re is the regular expression operations, used while matching the path and compile a pattern into a regular expression object 

# BONUS
from bs4.element import Comment  # used to append a comment into document
from string import ascii_lowercase  # used to return 'abcdefghijklmnopqrstuvwxyz'
import random  # the module implements pseudo-random number generators

# REQUIRED
# the ensure_absolute function check if the url is absolute, if not absolute then reconstruct a new URL.
def ensure_absolute(url):  #new function called ensure_absolute take url as the input
    if bool(urllib.parse.urlparse(url).netloc):  # this statement check the network location part
        return url # if true return the URL (url)
    else:
        return urllib.parse.urljoin(start,url)  # else rconstruct a full URL by combining a base URL (start) with another URL (url).

# REQUIRED
# ensure_urls_good function take the urls as input and check all the attributes in urls, then return whole list with correct URLs.
def ensure_urls_good(urls): # define a function call encure_urls_good and take urls as input
    result = [] #create an empty list call result
    basenetloc = urllib.parse.urlparse(start).netloc # create a base URL location, if value not present return empty string
    for url in urls: # use the for loop to go through all the url in the urls
        url = ensure_absolute(url) # call the ensure_absolute function, and assign the absolute URL to url.
        path = urllib.parse.urlparse(url).path # assign hierarchical path of the url, if value not present return empty string
        netloc = urllib.parse.urlparse(url).netloc # assign the network location of the url, if value not present return empty string
        query = urllib.parse.urlparse(url).query # assign the query componemnt of the url, if value not present return empty string
        fragment = urllib.parse.urlparse(url).fragment # assign the fragment identifier, if value not present return empty string
        param = urllib.parse.urlparse(url).params # assign parameters for last path element, if value not present return empty string
        if (netloc == basenetloc and re.match(r'^/wiki/', path) and query == '' and fragment == '' and param == ''): # use if statment check all the attribute of the URL
            result += [url] # store the correct url into the result list
    return result # return the result (urls)

# REQUIRED
# the getscourse function take the url as input read and parser the URL, return the document and data read.
def getsource(url): # define a function call getscource take url as input
    req=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}) #sends GET request to URL
    uClient=urllib.request.urlopen(req) # the urlopen function take the req as input and return the URL
    page_html=uClient.read() # read return data and put it in a variable call page_html
    uClient.close() # close the connection
    page_soup=BeautifulSoup(page_html,"html.parser") # applying BeautufulSoup to the obtained html
    return [page_soup, page_html] # return the document and data read from the html

# REQUIRED
# get anchors function find all the url in the document and return a list of all valid URLs
def getanchors(pagesoup): # define a function call getanchors and take pagesoup as input
    result = [] # create an empty list call result
    for anchor in pagesoup.find('div', {"id":'bodyContent'}).findAll('a'): # use for loop to find all the 'a' in the 'bodyContent'
        result += [anchor.get('href')] # get URLs
    result = ensure_urls_good(result) # check all URL with ensure_urls_good function
    return result #return a list of valid URLs

# BONUS
# tag_visible take element as input and check if the tag visible in the element
def tag_visible(element): #define a function call tag_visible and take element as input
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: # check if element parent name is 'style', 'script', 'head', 'title', 'meta', or '[document]'
        return False # then return false
    if isinstance(element, Comment): # check if any comment in the element
        return False # then return false
    return True # else return true

# BONUS
# the text_from_html take the page_html as input and find all the text in the html then return the texts
def text_from_html(page_html): # define a function call tex_for_html and take page_html as input, then return all the text in the html
    soup = BeautifulSoup(page_html, 'html.parser') # applying BeautufulSoup to the obtained html
    texts = soup.findAll(text=True) # use findall to find only the text
    visible_texts = filter(tag_visible, texts)  # filter out the tags
    return u" ".join(t.strip() for t in visible_texts) # return all the texts in the html

# BONUS
# the count_letters function take texts as input and get the frequency of all lowercase alphabets then return the final dicitionary.
def count_letters(texts): #define a function call count_letters and take texts as input
    alphabet = {}  # create a new dictionary call alphabet
    for letter in ascii_lowercase: # for loop use to go through all the lowercase alphabets
        alphabet[letter] = texts.count(letter) # count each letter's frequency and put into the dictionary(alphabet)
    return alphabet # return final dictionary(alphabet)

# BONUS
#the count_ngrams function take texts and n as input, then match the texts and create a dictionary with the frequecy of each ngram
def count_ngrams(texts, n): #define a function call counr_grams and take texts and n as input
    ngrams = {} #create a dictionary call ngrams
    grams = [] #create a list call grams
    pattern = re.compile(r'\[\w+\]|([a-zA-Z]+\'{0,1}[a-zA-Z]+)') # create regular expression use to find the pattern
    for m in re.finditer(pattern, texts): # for loop use iterator over all non-overlapping matches for the RE pattern in string.
        if (str(m.group(1)) != 'None'): # if the first paranthesis pair locates matching expression 1 is not equal 'None'
            if (len(grams) < n): # if the length of grams less than input n
                grams += [m.group(1)] # grams append the first paranthesis pair locates matching expression 1
            else: #else the first paranthesis pair locates matching expression 1 equal to 'None'
                ngram = ' '.join(grams); #join space between all the grams
                if (ngram in ngrams): #check if any element in ngram match element in nrams
                    ngrams[ngram] = ngrams[ngram]+1 # add one into the list ngram
                else: #if they do not match
                    ngrams[ngram] = 1 # put in the new list
                grams = grams[1:] # shallow copied list of all elements starting from the 0-indexed 1
                grams += [m.group(1)] #grams append the first paranthesis pair locates matching expression 1
    return ngrams #return the final ngrams

# BONUS
# combinedicts function use to combine two dictionaries
def combinedicts(dict1,dict2): # define a function call combinedicts and take dict1 and dict2 as input
    result = { k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2) } # for loop in a new dictionary use to combine the two inputs (dict1,dict2)
    return result #return the combined result

# REQUIRED
# This function use to write the data into the csv file by the input name, the header of the file, and write the data into the csv file.
def write_dict_to_csv(fname,header,data): #define a function call write_dict_to_csv which request 3 inputs: file name, header, and data.
    f=open(fname,'w') # open the file name(fname)
    f.write(header) # write the header to the file
    f.write('\n') # skip to the next line in the file
    for item in sorted(data, key=lambda i: int(data[i]), reverse=True): # the for loop started from the highest frequencty to the lowest
        f.write(str(item)+','+str(data[item]))  #write the item into the file and frequency
        f.write('\n') # go to the next line
    f.close() #close the file
    return # this function do not return anything back

# REQUIRED
# the crawl function take the url and limit as input, do a for loop for all the data in the list, then combine the word dicts to the frequecy dicts, and finally return the numebr frequency and ngram frequency
def crawl(url, limit): #define a function call crawl which request 2 inputs: url and limt.
    result1 = {} # create a new dictionary call result1
    result2 = {} # create a new dictionary call result2
    pagedata = getsource(url) # create a new variable call pagedata and assign it with the value return from the getscource function
    anchors = getanchors(pagedata[0]) #create a new variable call anchors and assign it with the value return from the getanchors
    for i in range(0,limit): # for loop that start from zero to the limit
        secure_random = random.SystemRandom() #create a variable call secure_random and assign it with a random number
        random_url = secure_random.choice(anchors) #create a variable call random_url and assign it with a ramdom choice from the anchors
        pagedata = getsource(random_url) #assign the random_url to the page data
        texts = text_from_html(pagedata[1]).lower() #lowercase all the text in the pagedata[1]
        letterfreqs = count_letters(texts) #call the count_letters function to count the letters in the texts
        ngramfreqs = count_ngrams(texts, desired_ngram_level) #call the count_ngrams to get ngram
        anchors = getanchors(pagedata[0]) #call the getanchors function to return a list of valid URLs
        if len(result1) > 1: #check if the length of the result1 larger than 1
            result1 = combinedicts(result1,letterfreqs) # use the combinedicts function to combine two dictionaries
        else: #else: result1 do not larger than 1
            result1 = letterfreqs  #the result1 will assign to letter frequency
        if len(result2) > 1: #check if the the length of the result2 is greater than 1
            result2 = combinedicts(result2,ngramfreqs) #use the combinedicts function to combine two dictionaries
        else: #else: result1 do not larger than 1
            result2 = ngramfreqs #the result2 will assign to ngram frequency
    return [result1, result2] #return the final results

# REQUIRED
start="https://en.wikipedia.org/wiki/Special:Random" # create a new variable called start and assign a string of web address

# REQUIRED
pagestocrawl = 20 # create a new variable called pagestocrawl and assign integer 20 to it

# BONUS
desired_ngram_level = 2 # create a new variable called desired_ngram_level and assign integer 2 to it

# REQUIRED
freqs = crawl(start,pagestocrawl) # call the crawl function input the start(web address) and pagestocrawl(the number of pages). The output will assign to the new variable freqs
write_dict_to_csv('letter_freqs.csv','letter,frequency',freqs[0])  # call the write_dict_to_csv function input string of file name'letter_freqs.csv', string of the header 'letter,frequency', and the first row of the freq array
write_dict_to_csv('ngram_freqs.csv','ngram,frequency',freqs[1]) # call the write_dict_to_csv function input string of file name 'ngram_freqs.csv', string of the header 'ngram,frequency', and the first row of the freq array



