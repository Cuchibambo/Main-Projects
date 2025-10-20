import random
import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(bg="#2b2b2b") 
frm = ttk.Frame(root, padding=10, style="Custom.TFrame")
frm.grid()
frm.configure(style="Custom.TFrame")
frm.pack(fill="both", expand=True)
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TFrame", background="#2b2b2b")

style.configure(
    "Custom.TButton",
    background="#454545",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    padding=10,
    borderwidth=0,
    focusthickness=0,
    focuscolor="none",
    relief="flat"
)

style.map(
    "Custom.TButton",
    background=[("active", "#357ABD"), ("pressed", "#2E5E9E")]
)

style.configure(
    "Custom.TLabel",
    background="#2b2b2b",
    foreground="white",
    font=("Segoe UI", 12, 'bold')
)

style.configure(
    "Category.TLabel",
    background="#2b2b2b",
    foreground="#bababa",
    font=("Segoe UI", 9)
)

class video():
    def __init__(self, titlefirstword, titlesecondword, titlethirdword):
        self.titlefirstword = titlefirstword
        self.titlesecondword = titlesecondword
        self.titlethirdword = titlethirdword
        options = [
            firstwordcategories.get(titlefirstword, "Not found"),
            secondwordcategories.get(titlesecondword, "Not found"),
            thirdwordcategories.get(titlethirdword, "Not found")
        ]
        self.category = random.choice(options)
    
    def __str__(self):
        return(f"-------------------------------------------------------------------------------------------\nA video titled: {self.titlefirstword} {self.titlesecondword} {self.titlethirdword}\nAbout: {self.category}\n-------------------")

data={}

# firstwordcategories = {
#     "Mastering": "Education",
#     "Exploring": "Entertainment",
#     "Unveiling": "Education",
#     "Discovering": "Entertainment",
#     "Creating": "Education",
#     "Transforming": "Education",
#     "Understanding": "Education",
#     "Navigating": "Education",
#     "Building": "DIY & How-To",
#     "Enhancing": "DIY & How-To"
# }

firstwordcategories = {
    "Apprendre" : "Éducation",
    "Explorer" : "Divertissement",
    "Découvrir": "Divertissement",
    "Transformé": "Éducation",
    "Comprendre" : "Éducation",
    "Entreprendre" : "Affaires et finances",
    "Construire" : "Bricolage et tutoriels",
    "Améliorer": "Bricolage et tutoriels"
}

# secondwordcategories = {
#     "Digital Marketing Strategies" : "Business & Finance",
#     "The Human Brain" : "Science",
#     "Artificial Intelligence" : "Technology",
#     "Culinary Arts" : "Food & Cooking",
#     "Personal Finance" : "Business & Finance",
#     "Travel Destinations" : "Travel",
#     "Fitness Routines" : "Health & Fitness",
#     "Photography Techniques" : "DIY & How-To",
#     "Home Decor Ideas" : "DIY & How-To",
#     "Mindfulness Practices" : "Health & Fitness"
# }

secondwordcategories = {
    "Le vélo": "Santé et fitness",
    "La natation": "Santé et fitness",
    "Les jeux vidéo": "Divertissement",
    "La musique": "Divertissement",
    "Le dessin": "Divertissement",
    "La photographie": "Divertissement",
    "Le cinéma": "Divertissement",
    "La cuisine": "Nourriture et cuisine"
}

# thirdwordcategories = {
#     "for Beginners" : "Education",
#     "on a Budget" : "Business & Finance",
#     "in 10 Minutes" : "DIY & How-To",
#     "You Need to Know" : "Education",
#     "Like a Pro" : "DIY & How-To",
#     "Step-by-Step" : "DIY & How-To",
#     "for this year" : "Education",
#     "That Will Change Your Life" : "Motivation & Inspiration",
#     "Revealed" : "Education",
#     "Made Easy" : "DIY & How-To"
# }

thirdwordcategories = {
    "pour les débutants": "Éducation",
    "à petit budget": "Affaires et finances",
    "en 10 minutes": "Bricolage et tutoriels",
    "que vous devez savoir": "Éducation",
    "comme un pro": "Bricolage et tutoriels",
    "étape par étape": "Bricolage et tutoriels",
    "cette année": "Éducation",
    "qui va changer votre vie": "Motivation et inspiration",
    "révélé": "Éducation",
    "facilement": "Bricolage et tutoriels"
}

def makingData():
    # data = {
    #     "preferredfirstword": {
    #         "Mastering": 0, "Exploring": 0, "Unveiling": 0, "Discovering": 0, "Creating": 0,
    #         "Transforming": 0, "Understanding": 0, "Navigating": 0, "Building": 0, "Enhancing": 0
    #     },
    #     "preferredsecondword": {
    #         "Digital Marketing Strategies": 0, "The Human Brain": 0, "Artificial Intelligence": 0,
    #         "Culinary Arts": 0, "Personal Finance": 0, "Travel Destinations": 0, "Fitness Routines": 0,
    #         "Photography Techniques": 0, "Home Decor Ideas": 0, "Mindfulness Practices": 0
    #     },
    #     "preferredthirdword": {
    #         "for Beginners": 0, "on a Budget": 0, "in 10 Minutes": 0, "You Need to Know": 0,
    #         "Like a Pro": 0, "Step-by-Step": 0, "for this year": 0, "That Will Change Your Life": 0,
    #         "Revealed": 0, "Made Easy": 0
    #     },
    #     "preferredcategorie": {
    #         "Education": 0, "Travel": 0, "Entertainment": 0, "DIY & How-To": 0, "Business & Finance": 0, "Science": 0, "Technology": 0,
    #         "Food & Cooking": 0, "Health & Fitness": 0, "Motivation & Inspiration": 0 
    #     },
    # }
    data = {
        "preferredfirstword": {
            "Apprendre" : 0, "Explorer" : 0, "Découvrir": 0, "Transformé": 0, "Comprendre" : 0, "Entreprendre" : 0,
            "Construire" : 0, "Améliorer": 0
        },
        "preferredsecondword": {
            "Le vélo": 0, "La natation": 0, "Les jeux vidéo": 0, "La musique": 0, "Le dessin": 0,
            "La photographie": 0, "Le cinéma": 0, "La cuisine": 0
        },
        "preferredthirdword": {
            "pour les débutants": 0, "à petit budget": 0, "en 10 minutes": 0, "que vous devez savoir": 0,
            "comme un pro": 0, "étape par étape": 0, "cette année": 0, "qui va changer votre vie": 0,
            "révélé": 0, "facilement": 0
        },
        "preferredcategorie": {
            "Éducation": 0, "Santé et fitness": 0, "Divertissement": 0, "Bricolage et tutoriels": 0,
            "Affaires et finances": 0, "Motivation et inspiration": 0, "Nourriture et cuisine": 0
        },
    }
    return data

data = makingData()

def makeVideos():
    
    # titlefirstword = ["Mastering","Exploring","Unveiling","Discovering","Creating","Transforming","Understanding","Navigating","Building","Enhancing"]
    # titlesecondword = ["Digital Marketing Strategies","The Human Brain","Artificial Intelligence","Culinary Arts","Personal Finance","Travel Destinations","Fitness Routines","Photography Techniques","Home Decor Ideas","Mindfulness Practices"]
    # titlethirdword = ["for Beginners","on a Budget","in 10 Minutes","You Need to Know","Like a Pro","Step-by-Step","for this year","That Will Change Your Life","Revealed","Made Easy"]
    titlefirstword = ["Apprendre","Explorer","Découvrir","Transformé","Comprendre","Entreprendre","Construire","Améliorer"]
    titlesecondword = ["Le vélo","La natation","Les jeux vidéo","La musique","Le dessin", "La photographie", "Le cinéma", "La cuisine"]
    titlethirdword = ["pour les débutants","à petit budget","en 10 minutes","que vous devez savoir","comme un pro","étape par étape","cette année","qui va changer votre vie","révélé","facilement"]
    
    videos = []
    for _ in range(10):
        Video = video(
            random.choice(titlefirstword),
            random.choice(titlesecondword),
            random.choice(titlethirdword),
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
    
    candidate1score = data.get("preferredfirstword",{}).get(candidateVideo1.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo1.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo1.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo1.category, "Not found")
    candidate3score = data.get("preferredfirstword",{}).get(candidateVideo3.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo3.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo3.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo3.category, "Not found")
    candidate4score = data.get("preferredfirstword",{}).get(candidateVideo4.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo4.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo4.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo4.category, "Not found")
    candidate2score = data.get("preferredfirstword",{}).get(candidateVideo2.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo2.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo2.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo2.category, "Not found")
    candidate5score = data.get("preferredfirstword",{}).get(candidateVideo5.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo5.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo5.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo5.category, "Not found")
    candidate6score = data.get("preferredfirstword",{}).get(candidateVideo6.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo6.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo6.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo6.category, "Not found")
    candidate7score = data.get("preferredfirstword",{}).get(candidateVideo7.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo7.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo7.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo7.category, "Not found")
    candidate8score = data.get("preferredfirstword",{}).get(candidateVideo8.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo8.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo8.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo8.category, "Not found")
    candidate9score = data.get("preferredfirstword",{}).get(candidateVideo9.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo9.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo9.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo9.category, "Not found")
    candidate10score = data.get("preferredfirstword",{}).get(candidateVideo10.titlefirstword, "Not found") + data.get("preferredsecondword",{}).get(candidateVideo10.titlesecondword, "Not found") + data.get("preferredthirdword",{}).get(candidateVideo10.titlethirdword, "Not found") + data.get("preferredcategorie",{}).get(candidateVideo10.category, "Not found")
    
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
    
    sortedcandidates = sorted(candidates, key=lambda x: x[1], reverse=True)
    selectedvideos=[]
    for i in range(3):
        selectedvideos.append(sortedcandidates[i][0])
    return selectedvideos

def VideoInfo(selectedvideo):
    print(selectedvideo)

def changeCurrentScore(changeby, selectedvideo):
    data.get("preferredfirstword")[selectedvideo.titlefirstword] += changeby
    data.get("preferredsecondword")[selectedvideo.titlesecondword] += changeby
    data.get("preferredthirdword")[selectedvideo.titlethirdword] += changeby
    data.get("preferredcategorie")[selectedvideo.category] += changeby

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

watchbonus = 1
skippenalty = -1/3

# def VideoInteractions(selectedVideo,watchorskip):
#     while True:
#         watchorskip = input("To watch type the number corresponding to the desisred video: ").strip()
#         if watchorskip == 0:
#             changeCurrentScore(watchbonus,selectedVideo[0])
#             changeCurrentScore(skippenalty,selectedVideo[1])
#             changeCurrentScore(skippenalty,selectedVideo[2])
#             return 0
#         elif watchorskip == 1:
#             changeCurrentScore(skippenalty,selectedVideo[0])
#             changeCurrentScore(watchbonus,selectedVideo[1])
#             changeCurrentScore(skippenalty,selectedVideo[2])
#             return 0
#         elif watchorskip == 2:
#             changeCurrentScore(skippenalty,selectedVideo[0])
#             changeCurrentScore(skippenalty,selectedVideo[1])
#             changeCurrentScore(watchbonus,selectedVideo[2])
#             return 0

def FirstVideoSelected(bestvideos):
    changeCurrentScore(watchbonus,bestvideos[0])
    changeCurrentScore(skippenalty,bestvideos[1])
    changeCurrentScore(skippenalty,bestvideos[2])
    MainLoop()
    
def SecondVideoSelected(bestvideos):
    changeCurrentScore(skippenalty,bestvideos[0])
    changeCurrentScore(watchbonus,bestvideos[1])
    changeCurrentScore(skippenalty,bestvideos[2])
    MainLoop()
    
def ThirdVideoSelected(bestvideos):
    changeCurrentScore(skippenalty,bestvideos[0])
    changeCurrentScore(skippenalty,bestvideos[1])
    changeCurrentScore(watchbonus,bestvideos[2])
    MainLoop()
    
def SkippedAll(bestvideos):
    changeCurrentScore(skippenalty,bestvideos[0])
    changeCurrentScore(skippenalty,bestvideos[1])
    changeCurrentScore(skippenalty,bestvideos[2])
    MainLoop()

def MainLoop():
    for widget in frm.winfo_children():
        widget.destroy()
    bestvideos = FindBestVideo()
    ttk.Label(frm, text="Video 1", style="Custom.TLabel").grid(column=0, row=0)
    ttk.Label(frm, text="Video 2", style="Custom.TLabel").grid(column=1, row=0)
    ttk.Label(frm, text="Video 3", style="Custom.TLabel").grid(column=2, row=0)
    ttk.Button(frm, text=f'{bestvideos[0].titlefirstword}\n{bestvideos[0].titlesecondword}\n{bestvideos[0].titlethirdword}',style="Custom.TButton", command=lambda: FirstVideoSelected(bestvideos)).grid(column=0, row=1, padx=10, pady=10)
    ttk.Button(frm, text=f'{bestvideos[1].titlefirstword}\n{bestvideos[1].titlesecondword}\n{bestvideos[1].titlethirdword}',style="Custom.TButton", command=lambda: SecondVideoSelected(bestvideos)).grid(column=1, row=1, padx=10, pady=10)
    ttk.Button(frm, text=f'{bestvideos[2].titlefirstword}\n{bestvideos[2].titlesecondword}\n{bestvideos[2].titlethirdword}',style="Custom.TButton", command=lambda: ThirdVideoSelected(bestvideos)).grid(column=2, row=1, padx=10, pady=10)
    ttk.Label(frm, text=f"Categorie: {bestvideos[0].category}", style="Category.TLabel").grid(column=0, row=2)
    ttk.Label(frm, text=f"Categorie: {bestvideos[1].category}", style="Category.TLabel").grid(column=1, row=2)
    ttk.Label(frm, text=f"Categorie: {bestvideos[2].category}", style="Category.TLabel").grid(column=2, row=2)
    ttk.Button(frm, text='Save',style="Custom.TButton", command=lambda: SaveData()).grid(column=0, row=3, pady=10)
    ttk.Button(frm, text='Load',style="Custom.TButton", command=lambda: LoadData()).grid(column=1, row=3, pady=10)
    ttk.Button(frm, text='Quit',style="Custom.TButton", command=root.destroy).grid(column=2, row=3, pady=10)
    ttk.Button(frm, text='Skip All',style="Custom.TButton", command=lambda: SkippedAll(bestvideos)).grid(column=1, row=4, padx=10, pady=10)

MainLoop()
root.mainloop()