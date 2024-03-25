class Classifying():
    def positive_score(self,st):
        ps = 0
        words = st.split(" ")
        positive_words = ["excellent", "fantastic", "wonderful", "amazing", "great",
        "good","nice","alright","fine","okay","satisfactory"
        "superb", "outstanding", "impressive", "awesome", "brilliant",
        "terrific", "fabulous", "phenomenal", "splendid", "stellar",
        "top-notch", "exceptional", "remarkable", "exemplary", "marvelous",
        "perfect", "ideal", "super", "incredible", "spectacular",
        "delightful", "joyful", "satisfying", "pleasurable", "enjoyable",
        "fantabulous", "glorious", "heartwarming", "uplifting", "blissful",
        "gratifying", "thrilling", "captivating", "charming", "refreshing",
        "radiant", "cheerful", "positive", "rewarding", "splendiferous",
        "delicious", "tremendous", "exhilarating", "exquisite", "lovely"]
        for word in words:
            word = word.lower()
            if word in positive_words:
                ps += 1
        return ps


    def negative_score(self,st):
        ns = 0
        words = st.split(" ")
        negative_words = ["terrible", "horrible", "awful", "bad", "poor",
        "disappointing", "unpleasant", "dreadful", "mediocre", "inferior",
        "subpar", "unacceptable", "unsatisfactory", "lousy", "miserable",
        "atrocious", "abysmal", "deplorable", "pathetic", "pitiful",
        "horrendous", "appalling", "shoddy", "woeful", "unfavorable",
        "unimpressive", "disgusting", "repulsive", "unpleasant", "offensive",
        "unappealing", "disastrous", "disheartening", "repugnant", "noxious",
        "vile", "gross", "shameful", "despicable", "unfortunate", "tragic",
        "disastrous", "unfortunate", "depressing", "distressing", "gloomy",
        "dreary", "miserable", "unhappy", "sorrowful"]
        for word in words:
            word = word.lower()
            if word in negative_words:
                ns += 1
        return ns



r_file = "reviewfile.txt"

with open(r_file, "a+") as  f:
    for i in range(5):
        review = input("Enter a review: ")
        f.write(review)

c = Classifying()

with open(r_file, "r") as f:
    data = f.read()
    reviews = data.split(".")
    
    positive_score = 0
    negative_score = 0

    for review in reviews:
        ps = c.positive_score(review)
        ns = c.negative_score(review)
        if ps>ns:
            positive_score += 1
        else:
            negative_score += 1

total_score = 5 
print("Positive reviews:" + str(positive_score/total_score*100) + "%")
print("Negative reviews:" + str(negative_score/total_score*100) + "%")