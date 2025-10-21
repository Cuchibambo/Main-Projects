import random
import json
from tkinter import *
from tkinter import ttk

# Start and setup tkinter
root = Tk()
root.configure(bg="#2b2b2b") 
frm = ttk.Frame(root, padding=10, style="Custom.TFrame")
frm.grid()
frm.configure(style="Custom.TFrame")
frm.pack(fill="both", expand=True)
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TFrame", background="#2b2b2b")

# Button Style
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

# Button react style
style.map(
    "Custom.TButton",
    background=[("active", "#357ABD"), ("pressed", "#2E5E9E")]
)

# Video title label style
style.configure(
    "Custom.TLabel",
    background="#2b2b2b",
    foreground="white",
    font=("Segoe UI", 12, 'bold')
)

# Category style
style.configure(
    "Category.TLabel",
    background="#2b2b2b",
    foreground="#bababa",
    font=("Segoe UI", 9)
)

# Video class
class video():
    def __init__(self, titlefirstword, titlesecondword, titlethirdword):
        # Choose name
        self.titlefirstword = titlefirstword
        self.titlesecondword = titlesecondword
        self.titlethirdword = titlethirdword
        # Choose cat
        options = [
            firstwordcategories.get(titlefirstword, "Not found"),
            secondwordcategories.get(titlesecondword, "Not found"),
            thirdwordcategories.get(titlethirdword, "Not found")
        ]
        self.category = random.choice(options)

# init vars
data = {}
nbVideos = 10

# Setup Title words along with their categories
firstwordcategories = {}
secondwordcategories = {}
thirdwordcategories = {}

# load tite from json file
try:
    with open("python\\algoworks\\VideoTitles.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        firstwordcategories = loaded_data['firstwordcategories']
        secondwordcategories = loaded_data['secondwordcategories']
        thirdwordcategories = loaded_data['thirdwordcategories']
except Exception as e:
    print(f"Error loading file: {e}")

# Setup Vars
titlefirstword = [i for i in firstwordcategories]
titlesecondword = [i for i in secondwordcategories]
titlethirdword = [i for i in thirdwordcategories]

# Init Data
def makingData():
    # data template(this shouldnt change)
    data = {
        "preferredfirstword": {},
        "preferredsecondword": {},
        "preferredthirdword": {},
        "preferredcategorie": {}
    }
    
    # Make all the entries in the data dict
    for i in titlefirstword:
        data["preferredfirstword"][i] = 0
    for i in titlesecondword:
        data["preferredsecondword"][i] = 0
    for i in titlethirdword:
        data["preferredthirdword"][i] = 0
    for i in titlethirdword:
        data["preferredthirdword"][i] = 0
    for i in firstwordcategories:
        data["preferredcategorie"][firstwordcategories.get(i)] = 0
    for i in secondwordcategories:
        data["preferredcategorie"][secondwordcategories.get(i)] = 0
    for i in thirdwordcategories:
        data["preferredcategorie"][thirdwordcategories.get(i)] = 0
        
    return data

data = makingData()

# Func to make videos
def makeVideos():
     
    videos = []
    for _ in range(nbVideos):
        Video = video(
            random.choice(titlefirstword),
            random.choice(titlesecondword),
            random.choice(titlethirdword),
        )
        videos.append(Video)

    return videos

def FindBestVideo():
    # Makes Videos and puts them in a list
    candidateVideos = makeVideos()
    # init Scores and tuple vars
    candidates = [i for i in range(len(candidateVideos))]
    
    # Make tuple to associate the video with its score
    for i in range(len(candidateVideos)):
        Firstword = data.get("preferredfirstword").get(candidateVideos[i].titlefirstword)
        Secondword = data.get("preferredfirstword").get(candidateVideos[i].titlefirstword)
        Thirdword = data.get("preferredfirstword").get(candidateVideos[i].titlefirstword)
        Category = data.get("preferredfirstword").get(candidateVideos[i].titlefirstword)
        candidates[i] = (candidateVideos[i], Firstword+Secondword+Thirdword+Category)
    
    # Sort Vids by score
    sortedcandidates = sorted(candidates, key=lambda x: x[1], reverse=True)
    selectedvideos=[]
    for i in range(3):
        selectedvideos.append(sortedcandidates[i][0])
    return selectedvideos

def changeCurrentScore(changeby, selectedvideo):
    data.get("preferredfirstword")[selectedvideo.titlefirstword] += changeby
    data.get("preferredsecondword")[selectedvideo.titlesecondword] += changeby
    data.get("preferredthirdword")[selectedvideo.titlethirdword] += changeby
    data.get("preferredcategorie")[selectedvideo.category] += changeby

def SaveData():
    try:
        with open("python\\algoworks\\preferences.json", "w") as file:
            json.dump(data, file, indent=4)
            print("JSON file saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def LoadData():
    try:
        with open("python\\algoworks\\preferences.json", "r") as file:
            loaded_data = json.load(file)
            data.update(loaded_data)
            print("JSON file loaded successfully!")
    except Exception as e:
        print(f"Error loading file: {e}")

# init vars for video interactions
watchbonus = 1
skippenalty = -1/3

# Corresponds to a selected video
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

# Main logic loop
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

# Start everything
MainLoop()
root.mainloop()