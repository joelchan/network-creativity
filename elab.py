import string

def read_data(filename):
    """
    Read in data from a file and return a list with each element being one line from the file.
    Parameters:
    1) filename: name of file to be read from
    Note: the code now opens as a binary and replaces carriage return characters with newlines because python's read and readline functions don't play well with carriage returns.
    However, this will no longer be an issue with python 3.
    """
    with open(filename, "rb") as f:
        s = f.read().replace('\r\n', '\n').replace('\r', '\n')
        data = s.split('\n')
    return data

def get_stopwords():
    """Returns a list of stop words. Currently uses a list of words in
    a text file

    """
    return read_data("englishstopwords-jc.txt")

# gives ratio of non-stop words to total length, that is, the "density" of the idea
# gives percentage of non-stop words
def elab1(originidea):
    idea = ""
    for char in originidea:
        if char not in string.punctuation:
            idea += char
    stopwords = get_stopwords()
	# return (str.split(idea), len(str.split(idea)))
    wlst = str.split(idea)
    implst = 0
    for index in range(len(wlst)):
        if wlst[index] not in stopwords:
            implst += 1
    return (0.0 + implst) / len(wlst)


# gives total number of non-stop words
# essentially the same as scaling the pecentage of stop words proportional to the total number of words
def elab2(idea):
    #idea = ""
    #for char in originidea:
    #    if char not in string.punctuation:
    #        idea += char
    #print "idea: "+idea
    #print(repr(idea))
    stopwords = get_stopwords()
    wlst = str.split(idea)
    # print wlst
    implst = []
    for word in wlst:
        # print word
        if (string.strip(word, string.punctuation+string.whitespace)) not in stopwords:
            implst.append(string.strip(word, string.punctuation+string.whitespace))
            # print implst
    # print implst
    return len(implst)


# gives the number of unique words
def numUniqueWords(originidea):
    #idea = ""
    for char in originidea:
        # print char
        if char not in string.punctuation:
            idea += char
    # print idea
    uniqueWords = set()
    # stopwords = get_stopwords()
    wordList = str.split(idea)
    for word in wordList:
        uniqueWords.add(word)
    return len(uniqueWords)

# gives the percentage of unique words
def percentUniqueWords(originidea):
    idea = ""
    for char in originidea:
        if char not in string.punctuation:
            idea += char
    return (numUniqueWords(idea) + 0.0)/len(str.split(idea))

# gives the number of unique non-stop words
def numUniqueNonStops(idea):
    #idea = ""
    #for char in originidea:
    #    if char not in string.punctuation:
    #        idea += char
    stopwords = get_stopwords()
    wlst = str.split(idea)
    impwrdsset = set()
    for word in wlst:
        if (string.strip(word, string.punctuation+string.whitespace)) not in stopwords:
            impwrdsset.add(string.strip(word, string.punctuation+string.whitespace))
    return len(impwrdsset)

# gives the percentage of unique non-stop words
def percentUniqueNonStops(originidea):
    # print str.split(originidea)
    # print len(str.split(originidea))
    return (numUniqueNonStops(originidea)+0.0)/len(str.split(originidea))

# gives the percentage of unique non-stop words as a percentage of non-stop words
def percentUniqueOfNonStops(originidea):
    # print elab2(originidea)
    return (numUniqueNonStops(originidea)+0.0)/elab2(originidea)

'''
Have older relative, maybe mom or grandmother, do cooking video to display. in kitchen like a photo. This can be used as a fun family portrait. So that all family members can share their memories; it can be place in the living room.
A changeable room environment. Large panels of fabric hung like wallpaper on the walls of a room could create an entire environment to resemble a bamboo forest, for example, or an alpine lakeshore. The fabric could display moving wildlife such as pandas in the bamboo forest or birds on the shore of the mountain lake. The possibilities are endless!
Use banner sized fabric to display advertisements either on temporary construction areas, "Pardon our Dust" or "Coming soon - yet another Starbucks!"
Synchronization of clothing for public displays. [e.g. the opening ceremony of a grand event or for sports competitions.]
This could possibly make a very creative "flag" like item that could be out in the weather, and come in different sizes.  Perhaps a new way for a business to attract attention and replace neon signage.
stores could hang large fabric pieces over aisles to display what is in the aisles and what's currently on sale.
A bright pattern that activates at night when it notices oncoming traffic for safety.
group gathering wearing shirts that proclaim their group name and make them customizable
It could be used for a cheap means of advertising. Suddenly everyone could have access to their own billboards, signs, etc. that could be updated at any time digitally.
It could be used to make curtains that change color or shade based on the amount of sunlight coming in.
dish towel that doubles as a video player for recipes
Change the color of a car with a button
use for hospital blankets and sheet with get well messages
Dance floor carpet that flashes the next foot print spot after dancer hits appropriate spot.
A changing projected pattern on the clothes that reflects mood.
to use outdoors during holiday events such as 4th of July to show event schedule, holiday documentaries, pictures of local people having fun.
Cheaper alternative for touch displays where high resolution isn't a priority.
Use as a classroom smartboard without the need to take up space or move equipment around from room to room.
Fold able interactive maps. connect a small GPS unit and the map can tell you were you are going
A uniform for sports that changes depending on the place of the game.
They could be used by businesses to make ever changing interactive flyers
Camouflaged clothes for a stealth mission.
put in the floor to teach foot steps for dances
clothes that change color based on your mood by detecting body heat
Displayed in hotel bathrooms, etc for marking purposes.
watch movies on the back of an airplane seat
Use it on bedding to quickly change the look of your bedroom
night light for kids room
to use at museums and concerts to display things
Use it as a canvas for art, as it reacts to touch.
Project video games at a tournament.
Cover a couch in them and you can have a different colored couch every day.
In places where projectors are used, this can take the place of a large projector.
use it to display life size photos
Use it for a christmas display
Mood ring like clothes
sports teams gear
Kids toys
'''