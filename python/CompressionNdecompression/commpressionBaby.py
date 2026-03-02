import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import ttk
root = TkinterDnD.Tk()

def sortDict(dict, reverse:bool) -> dict:
        return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=reverse)}

def getCharFrequencies(text:str) -> dict:
    char_frequencies = {}
    for char in text:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1
    return char_frequencies

def CombineLeastFrequentChars(dict:dict):
    k1 = next(iter(dict))
    v1 = dict.pop(k1)
    k2 = next(iter(dict))
    v2 = dict.pop(k2)

    rk = (k1,k2)
    rv = v1+v2
    dict[rk] = rv
    return dict, k1, k2

def GenerateTree(text:str):
    char_frequencies = getCharFrequencies(text)
    TupleCodes = {}
    TupleHierarchy = {}
    while len(char_frequencies) > 1:
        char_frequencies = sortDict(char_frequencies,False)
        char_frequencies, k1, k2 = CombineLeastFrequentChars(char_frequencies)
        TupleHierarchy[k1] = (k1,k2)
        TupleHierarchy[k2] = (k1,k2)
        TupleCodes[k1] = 0
        TupleCodes[k2] = 1
    
    return next(iter(char_frequencies)), TupleCodes, TupleHierarchy

def GetCharCode(char:str,TupleCodes:dict,TupleHierarchy:dict) -> str:
    code = ''
    while True:
        if TupleCodes.get(char) != None:
            code = str(TupleCodes.get(char)) + code
            char = TupleHierarchy.get(char)
        else:
            break
    return code

def GetByteSize(data:int) -> int:
    counter = 0
    while data > 0:
        data = data >> 8
        counter += 1
    return counter

def GetCharFromCode(code:str,tree):
    for bit in code:
        tree = tree[int(bit)]
    
    return tree

def DecompressFile(compressed_file:str,decompressed_file:str):
    with open(compressed_file, 'rb') as f:
        filedata = f.read()
    cutoff = filedata.find(b'\xFF\xFF')
    code = filedata[:cutoff]
    code = bin(int(code.hex(),16))[3:]
    Tree = filedata[cutoff+2:]
    Tree = str(Tree)[2:-1]
    Tree = eval(Tree)
    
    decompressed_text = ''
    while len(code) > 0:
        i = 0
        while type(GetCharFromCode(code[:i],Tree)) == tuple:
            i += 1
        decompressed_text += GetCharFromCode(code[:i],Tree)
        code = code[i:]
    
    with open(decompressed_file, 'w') as f:
        f.write(decompressed_text)

def CompressFile(original_file:str,compressed_file:str):
    with open(original_file, 'r') as f:
        original_text = f.read()

    Tree, TupleCodes, TupleHierarchy = GenerateTree(original_text)
    code = '1'
    charCodes = {}
    for char in original_text:
        if char in charCodes:
            code += charCodes.get(char)
        else:
            charCodes[char] = GetCharCode(char,TupleCodes,TupleHierarchy)
            code += charCodes.get(char)
    code = int(code,2)
    
    
    byteSize = GetByteSize(code)
    code = code.to_bytes(byteSize,'big')
    code += b'\xFF\xFF'
    with open(compressed_file, "wb") as f:
        code = bytearray(code)
        f.write(code)
        
    with open(compressed_file, '+a') as f:
        f.write(str(Tree))

def RemoveFileNameFromPath(path:str) -> str:
    if path.find('/') == -1:
        return ''
    while path.endswith('/') == False:
        path = path[:-1]
    return path

def InputFileHandler(event):
    global InputFile
    InputFileLabel.config(text=event.data)
    InputFile = event.data
    
def CompressButtonHandler():
    OutputFileName = OutputFileTextInput.get('1.0','end-1c')
    OutputPath = RemoveFileNameFromPath(InputFile)
    OutputPath += OutputFileName + '.b'
    CompressFile(InputFile,OutputPath)
    
def DecompressButtonHandler():
    OutputFileName = OutputFileTextInput.get('1.0','end-1c')
    OutputPath = RemoveFileNameFromPath(InputFile)
    OutputPath += OutputFileName + '.txt'
    DecompressFile(InputFile,OutputPath)

InputFile = ''

root.title("Cuchi's compressor")
root.geometry("700x300")
padx, pady = 10, 8

# -------------------- Styles --------------------
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#2b2b2b")

style.configure("Title.TLabel",
                background="#2b2b2b",
                foreground="white",
                font=("Segoe UI", 12, "bold"))

style.configure("Drop.TLabel",
                background="#3c3f41",
                foreground="white",
                anchor="center",
                font=("Segoe UI", 11))

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                padding=10)

style.map("TButton",
          background=[("active", "#4a90e2")],
          foreground=[("active", "white")])

# -------------------- Main Layout --------------------
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=padx, pady=pady)

main_frame.columnconfigure(0, weight=1, uniform='col')  # left
main_frame.columnconfigure(1, weight=1, uniform='col')  # middle buttons
main_frame.columnconfigure(2, weight=1, uniform='col')  # right
main_frame.rowconfigure(0, weight=1)

# -------------------- Left: Drag & Drop --------------------
left_frame = ttk.Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew", padx=padx, pady=pady)

InputFileLabel = ttk.Label(left_frame,
                           text="Drag & Drop\nInput File",
                           style="Drop.TLabel",
                           anchor="center",
                           justify="center")
InputFileLabel.pack(expand=True, fill="both")

InputFileLabel.drop_target_register(DND_FILES)  # type: ignore
InputFileLabel.dnd_bind('<<Drop>>', InputFileHandler)  # type: ignore

# -------------------- Middle: Buttons --------------------
middle_frame = ttk.Frame(main_frame)
middle_frame.grid(row=0, column=1, sticky="nsew", padx=padx, pady=pady)

middle_frame.columnconfigure(0, weight=1)
middle_frame.rowconfigure(0, weight=1)
middle_frame.rowconfigure(1, weight=0)
middle_frame.rowconfigure(2, weight=1)

buttons_frame = ttk.Frame(middle_frame)
buttons_frame.grid(row=1, column=0)

CompressButton = ttk.Button(
    buttons_frame,
    text="Compress",
    style="TButton",
    command=CompressButtonHandler
)
CompressButton.pack(fill="x", pady=(0, 10), ipadx=20)

DecompressButton = ttk.Button(
    buttons_frame,
    text="Decompress",
    style="TButton",
    command=DecompressButtonHandler
)
DecompressButton.pack(fill="x", ipadx=20)

# -------------------- Right: Output Path --------------------
right_frame = ttk.Frame(main_frame)
right_frame.grid(row=0, column=2, sticky="nsew", padx=padx, pady=pady)
right_frame.rowconfigure(1, weight=1)

OutputFileLabel = ttk.Label(right_frame,
                            text="Output Name",
                            style="Title.TLabel")
OutputFileLabel.grid(row=0, column=0, sticky="w", pady=(0, 5))

OutputFileTextInput = tk.Text(right_frame,
                              height=2,
                              font=("Consolas", 11),
                              bg="#3c3f41",
                              fg="white",
                              wrap="char",
                              insertbackground="white",
                              padx=8,
                              pady=6,
                              undo=True,
                              relief="flat")
OutputFileTextInput.grid(row=1, column=0, sticky="nsew")
right_frame.columnconfigure(0, weight=1)
root.mainloop()