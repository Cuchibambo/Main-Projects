import random
import json

class video():
    def __init__(self, titlefirstword, titlesecondword, titlethirdword, duration, views, likes, dislikes, nbcomments, day, month, year):
        self.titlefirstword = titlefirstword
        self.titlesecondword = titlesecondword
        self.titlethirdword = titlethirdword
        options = [
            firstwordcategories.get(titlefirstword, "Not found"),
            secondwordcategories.get(titlesecondword, "Not found"),
            thirdwordcategories.get(titlethirdword, "Not found")
        ]
        self.category = random.choice(options)
        self.duration = duration
        self.views = views
        self.likes = likes
        self.dislikes = dislikes
        self.nbcomments = nbcomments
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return(f"-------------------------------------------------------------------------------------------\nA video titled: {self.titlefirstword} {self.titlesecondword} {self.titlethirdword}\nDuration: {self.duration} minutes\nAbout: {self.category}\nViews: {round(self.views / 1000)}K\nLikes: {round(self.likes / 1000)}K\nDislikes: {round(self.dislikes / 1000)}K\nComments: {round(self.nbcomments)}\nDate: {self.day}/{self.month}/{self.year}\n-------------------")

firstwordcategories = {
    "Mastering" : "Education",
    "Exploring" : "Travel",
    "Unveiling" : "Entertainment",
    "Discovering" : "Education",
    "Creating" : "DIY & How-To",
    "Transforming" : "DIY & How-To",
    "Understanding" : "Education",
    "Navigating" : "Travel",
    "Building" : "DIY & How-To",
    "Enhancing" : "DIY & How-To"
}

secondwordcategories = {
    "Digital Marketing Strategies" : "Business & Finance",
    "The Human Brain" : "Science",
    "Artificial Intelligence" : "Technology",
    "Culinary Arts" : "Food & Cooking",
    "Personal Finance" : "Business & Finance",
    "Travel Destinations" : "Travel",
    "Fitness Routines" : "Health & Fitness",
    "Photography Techniques" : "DIY & How-To",
    "Home Decor Ideas" : "DIY & How-To",
    "Mindfulness Practices" : "Health & Fitness"
}

thirdwordcategories = {
    "for Beginners" : "Education",
    "on a Budget" : "Business & Finance",
    "in 10 Minutes" : "DIY & How-To",
    "You Need to Know" : "Education",
    "Like a Pro" : "DIY & How-To",
    "Step-by-Step" : "DIY & How-To",
    "for this year" : "Education",
    "That Will Change Your Life" : "Motivation & Inspiration",
    "Revealed" : "Education",
    "Made Easy" : "DIY & How-To"
}

def makingData():
    data = {
        "preferredfirstword": {
            "Mastering": 0, "Exploring": 0, "Unveiling": 0, "Discovering": 0, "Creating": 0,
            "Transforming": 0, "Understanding": 0, "Navigating": 0, "Building": 0, "Enhancing": 0
        },
        "preferredsecondword": {
            "Digital Marketing Strategies": 0, "The Human Brain": 0, "Artificial Intelligence": 0,
            "Culinary Arts": 0, "Personal Finance": 0, "Travel Destinations": 0, "Fitness Routines": 0,
            "Photography Techniques": 0, "Home Decor Ideas": 0, "Mindfulness Practices": 0
        },
        "preferredthirdword": {
            "for Beginners": 0, "on a Budget": 0, "in 10 Minutes": 0, "You Need to Know": 0,
            "Like a Pro": 0, "Step-by-Step": 0, "for this year": 0, "That Will Change Your Life": 0,
            "Revealed": 0, "Made Easy": 0
        },
        "preferredcategorie": {
            "Education": 0, "Travel": 0, "Entertainment": 0, "DIY & How-To": 0, "Business & Finance": 0, "Science": 0, "Technology": 0,
            "Food & Cooking": 0, "Health & Fitness": 0, "Motivation & Inspiration": 0 
        },
        # "preferredduration": {i: 0 for i in range(1, 21)},
        "preferredduration": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0},
        "preferredviews": {
            "0-10k": 0, "11k-100k": 0, "101k-500k": 0, "501k-1M": 0
        },
        "preferredlikes": {
            "0-10k": 0, "11k-100k": 0, "101k-500k": 0, "501k-1M": 0
        },
        "preferreddislikes": {
            "0-10k": 0, "11k-100k": 0, "101k-500k": 0, "501k-1M": 0
        },
        "preferrednbcomments": {
            "0-2000": 0, "2001-5000": 0, "5001-10000": 0, "10001-15k": 0
        },
        "preferredyear": {"2005": 0, "2006": 0, "2007": 0, "2008": 0, "2009": 0, "2010": 0, "2011": 0, "2012": 0, "2013": 0, "2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0, "2019": 0, "2020": 0, "2021": 0, "2022": 0, "2023": 0, "2024": 0}
    }
    return data

data = makingData()

def makecomplicatedvars():
        views = random.randint(0, 1000000)
        likes = random.randint(0, 500000)
        dislikes = likes * random.uniform(1, 1.5)  # More accurate scaling

        if likes > views:
            likes = max(0, views - random.randint(1000, 10000))
            dislikes = max(0, views - random.randint(1000, 10000))

        nbcomments = round(views * 0.005 + dislikes * 0.02)

        month = random.randint(1, 12)
        daysinmonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day = random.randint(1, daysinmonth[month])

        return {
            "views": views,
            "likes": likes,
            "dislikes": dislikes,
            "nbcomments": nbcomments,
            "month": month,
            "day": day
        }

def makeVideos():
    
    titlefirstword = ["Mastering","Exploring","Unveiling","Discovering","Creating","Transforming","Understanding","Navigating","Building","Enhancing"]
    titlesecondword = ["Digital Marketing Strategies","The Human Brain","Artificial Intelligence","Culinary Arts","Personal Finance","Travel Destinations","Fitness Routines","Photography Techniques","Home Decor Ideas","Mindfulness Practices"]
    titlethirdword = ["for Beginners","on a Budget","in 10 Minutes","You Need to Know","Like a Pro","Step-by-Step","for this year","That Will Change Your Life","Revealed","Made Easy"]
    
    videos = []
    for _ in range(10):
        stats = makecomplicatedvars()
        Video = video(
            random.choice(titlefirstword),
            random.choice(titlesecondword),
            random.choice(titlethirdword),
            str(random.randint(1, 20)),
            stats.get("views"),
            stats.get("likes"),
            stats.get("dislikes"),
            stats.get("nbcomments"),
            stats.get("day"),
            stats.get("month"),
            str(random.randint(2005, 2024))
        )
        videos.append(Video)

    return videos

def FindBestVideo():
    
    candidateVideo1 = makeVideos()[0]
    candidateVideo2 = makeVideos()[1]
    candidateVideo3 = makeVideos()[2]
    candidateVideo4 = makeVideos()[3]
    candidateVideo5 = makeVideos()[4]
    candidateVideo6 = makeVideos()[5]
    candidateVideo7 = makeVideos()[6]
    candidateVideo8 = makeVideos()[7]
    candidateVideo9 = makeVideos()[8]
    candidateVideo10 = makeVideos()[9]
    
    def candidateviewscalculator(candidateVideo):
        if candidateVideo.views <= 10000:
            candidateviewscore = "0-10k"
        elif candidateVideo.views <= 100000:
            candidateviewscore = "11k-100k"
        elif candidateVideo.views <= 500000:
            candidateviewscore = "101k-500k"
        else:
            candidateviewscore = "501k-1M"
        return candidateviewscore
    
    def candidatelikescalculator(candidateVideo):
        if candidateVideo.likes <= 10000:
            candidatelikesscore = "0-10k"
        elif candidateVideo.likes <= 100000:
            candidatelikesscore = "11k-100k"
        elif candidateVideo.likes <= 500000:
            candidatelikesscore = "101k-500k"
        else:
            candidatelikesscore = "501k-1M"
        return candidatelikesscore
    
    def candidatedislikescalculator(candidateVideo):
        if candidateVideo.dislikes <= 10000:
            candidatedislikescore = "0-10k"
        elif candidateVideo.dislikes <= 100000:
            candidatedislikescore = "11k-100k"
        elif candidateVideo.dislikes <= 500000:
            candidatedislikescore = "101k-500k"
        else:
            candidatedislikescore = "501k-1M"
        return candidatedislikescore
    
    def candidatenbcommentscalculator(candidateVideo):
        if candidateVideo.nbcomments <= 2000:
            candidatenbcommentsscore = "0-2000"
        elif candidateVideo.nbcomments <= 100000:
            candidatenbcommentsscore = "2001-5000"
        elif candidateVideo.nbcomments <= 500000:
            candidatenbcommentsscore = "5001-10000"
        else:
            candidatenbcommentsscore = "10001-15k"
        return candidatenbcommentsscore
    
    candidate1score = data.get("preferredfirstword",{}).get(candidateVideo1.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo1.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo1.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo1.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo1.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo1), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo1), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo1), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo1), "Not found") + data.get("preferredyear",{}).get(candidateVideo1.year, "Not found")
    candidate3score = data.get("preferredfirstword",{}).get(candidateVideo3.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo3.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo3.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo3.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo3.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo3), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo3), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo3), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo3), "Not found") + data.get("preferredyear",{}).get(candidateVideo3.year, "Not found")
    candidate4score = data.get("preferredfirstword",{}).get(candidateVideo4.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo4.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo4.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo4.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo4.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo4), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo4), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo4), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo4), "Not found") + data.get("preferredyear",{}).get(candidateVideo4.year, "Not found")
    candidate2score = data.get("preferredfirstword",{}).get(candidateVideo2.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo2.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo2.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo2.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo2.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo2), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo2), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo2), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo2), "Not found") + data.get("preferredyear",{}).get(candidateVideo2.year, "Not found")
    candidate5score = data.get("preferredfirstword",{}).get(candidateVideo5.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo5.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo5.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo5.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo5.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo5), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo5), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo5), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo5), "Not found") + data.get("preferredyear",{}).get(candidateVideo5.year, "Not found")
    candidate6score = data.get("preferredfirstword",{}).get(candidateVideo6.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo6.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo6.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo6.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo6.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo6), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo6), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo6), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo6), "Not found") + data.get("preferredyear",{}).get(candidateVideo6.year, "Not found")
    candidate7score = data.get("preferredfirstword",{}).get(candidateVideo7.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo7.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo7.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo7.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo7.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo7), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo7), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo7), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo7), "Not found") + data.get("preferredyear",{}).get(candidateVideo7.year, "Not found")
    candidate8score = data.get("preferredfirstword",{}).get(candidateVideo8.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo8.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo8.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo8.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo8.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo8), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo8), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo8), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo8), "Not found") + data.get("preferredyear",{}).get(candidateVideo8.year, "Not found")
    candidate9score = data.get("preferredfirstword",{}).get(candidateVideo9.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo9.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo9.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo9.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo9.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo9), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo9), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo9), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo9), "Not found") + data.get("preferredyear",{}).get(candidateVideo9.year, "Not found")
    candidate10score = data.get("preferredfirstword",{}).get(candidateVideo10.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo10.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo10.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo10.category, "Not found") + data.get("preferredduration",{}).get(candidateVideo10.duration, "Not found") + data.get("preferredviews",{}).get(candidateviewscalculator(candidateVideo10), "Not found") + data.get("preferredlikes",{}).get(candidatelikescalculator(candidateVideo1), "Not found") + data.get("preferreddislikes",{}).get(candidatedislikescalculator(candidateVideo10), "Not found") + data.get("preferrednbcomments",{}).get(candidatenbcommentscalculator(candidateVideo10), "Not found") + data.get("preferredyear",{}).get(candidateVideo10.year, "Not found")
    
    candidates = [
        (candidateVideo1, candidate1score),
        (candidateVideo2, candidate2score),
        (candidateVideo3, candidate3score),
        (candidateVideo4, candidate4score),
        (candidateVideo5, candidate5score),
        (candidateVideo6, candidate6score),
        (candidateVideo7, candidate7score),
        (candidateVideo8, candidate8score),
        (candidateVideo9, candidate9score),
        (candidateVideo10, candidate10score)
    ]
    
    if random.randint(1, 10) == 1:
        sortedcandidates = sorted(candidates, key=lambda x: x[1])
        selectedvideo = random.choice(sortedcandidates[:3])[0]
        return selectedvideo
    else:
        sortedcandidates = sorted(candidates, key=lambda x: x[1], reverse=True)
        selectedvideo = random.choice(sortedcandidates[:3])[0]
        return selectedvideo

def VideoInfo(selectedvideo):
    print(selectedvideo)

def changeCurrentScore(changeby, selectedvideo):
    data.get("preferredfirstword")[selectedvideo.titlefirstword] += changeby
    data.get("preferredsecondword")[selectedvideo.titlesecondword] += changeby
    data.get("preferredthirdword")[selectedvideo.titlethirdword] += changeby
    data.get("preferredcategorie")[selectedvideo.category] += changeby
    data.get("preferredduration")[selectedvideo.duration] += changeby
        
    if selectedvideo.views <= 10000:
        data.get("preferredviews")["0-10k"] += changeby
    elif selectedvideo.views <= 100000:
        data.get("preferredviews")["11k-100k"] += changeby
    elif selectedvideo.views <= 500000:
        data.get("preferredviews")["101k-500k"] += changeby
    else:
        data.get("preferredviews")["501k-1M"] += changeby
        
    if selectedvideo.likes <= 10000:
        data.get("preferredlikes")["0-10k"] += changeby
    elif selectedvideo.likes <= 100000:
        data.get("preferredlikes")["11k-100k"] += changeby
    elif selectedvideo.likes <= 500000:
        data.get("preferredlikes")["101k-500k"] += changeby
    else:
        data.get("preferredlikes")["501k-1M"] += changeby
    
    if selectedvideo.dislikes <= 10000:
        data.get("preferreddislikes")["0-10k"] += changeby
    elif selectedvideo.dislikes <= 100000:
        data.get("preferreddislikes")["11k-100k"] += changeby
    elif selectedvideo.dislikes <= 500000:
        data.get("preferreddislikes")["101k-500k"] += changeby
    else:
        data.get("preferreddislikes")["501k-1M"] += changeby
    
    if selectedvideo.nbcomments <= 2000:
        data.get("preferrednbcomments")["0-2000"] += changeby
    elif selectedvideo.nbcomments <= 5000:
        data.get("preferrednbcomments")["2001-5000"] += changeby
    elif selectedvideo.nbcomments <= 10000:
        data.get("preferrednbcomments")["5001-10000"] += changeby
    else:
        data.get("preferrednbcomments")["10001-15k"] += changeby
        
    data.get("preferredyear")[selectedvideo.year] += changeby

def SaveData():
    try:
        with open("preferences.json", "w") as file:
            json.dump(data, file, indent=4)
            print("JSON file saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def LoadData():
    try:
        with open("preferences.json", "r") as file:
            loaded_data = json.load(file)
            data.update(loaded_data)
            print("JSON file loaded successfully!")
    except Exception as e:
        print(f"Error loading file: {e}")

# Possible interations with the video:
likebonus = 0.1
dislikepenalty = -0.2
commentbonus = 0.1
skippenalty = -0.1
watchbonus = 0.05

def VideoInteractions(selectedvideo):
    while True:
        watchorskip = input("Watch: 1 | Skip: 2: ").strip()
        if watchorskip == "1":
            changeCurrentScore(watchbonus, selectedvideo)
            while True:
                likedislike = input("Like: 1 | Dislike: 2 | Do nothing: 3: ").strip()
                if likedislike in {"1", "2", "3"}:
                    if likedislike == "1":
                        changeCurrentScore(likebonus, selectedvideo)
                    elif likedislike == "2":
                        changeCurrentScore(dislikepenalty, selectedvideo)
                    elif likedislike == "3":
                        pass
                    break
                else:
                    print("Invalid input")
            while True:
                comment = input("Comment (y/n): ").strip().lower()
                if comment in {"y", "n"}:
                    if comment == "y":
                        changeCurrentScore(commentbonus, selectedvideo)
                    elif comment == "n":
                        pass
                    MainLoop()
                    break
                else:
                    print("Invalid input")
            break
        elif watchorskip == "2":
            changeCurrentScore(skippenalty, selectedvideo)
            MainLoop()
            break
        elif watchorskip == "save":
            SaveData()
        elif watchorskip == "load":
            LoadData()
        else:
            print("Invalid input")

def MainLoop():
    bestvideo = FindBestVideo()
    VideoInfo(bestvideo)
    VideoInteractions(bestvideo)

MainLoop()