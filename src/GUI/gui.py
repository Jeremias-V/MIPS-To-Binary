import sys
import os
sys.path.append("..")

from src.Translator.Translate import translateMIPS
import tkinter as tk

def main():

    root = tk.Tk()
    root.geometry("1480x940")
    root.title("MIPS Translator")

    width = 65
    height = 40
    
    window = tk.Frame(root)
    # Input
    inputLabel = tk.Label(window, text="MIPS / HEX", font="consoles 12") 
    inputLabel.grid(row=0, column=0)
    inputCode = tk.Text(window, font = "consoles 10", width = width, height = height)
    inputCode.grid(row=1, column=0)

    # Output
    outputLabel = tk.Label(window, text="Translation", font="consoles 12") 
    outputLabel.grid(row=0, column=1)
    outputCode = tk.Text(window, font = "consoles 10", width = width, height = height)
    outputCode.grid(row=1, column=1)

    buttons = tk.Frame(root)

    def cleanCode(lines):
        final = list()
        cur_path = os.path.dirname(__file__)
        path = cur_path + '../Translator/Parser/instructions.txt'
        with open(path, 'r') as f:
            instructions = f.read().split()
        lines = lines.split('\n')
        for line in lines:
            originalLine = list(line.split('\n'))
            line = list(line.split())
            if not line or line[0] == '#' or line[0][0] == '.' or (line[0] not in instructions):
                pass
            else:
                tmp = ' '.join(originalLine)
                ans = tmp.split("#", 1)
                final.append(ans[0].split())
        return final

    def cleanButton():
        ## function to clean the code
        lines = inputCode.get(1.0, tk.END)
        inputCode.delete(1.0, tk.END)
        cleanerCode = cleanCode(lines)
        ans = ""
        for l in cleanerCode:
            ans += ' '.join(l) + '\n'
        inputCode.insert(tk.INSERT, ans)

    def translateMIPSButton():
        lines = inputCode.get(1.0, tk.END)
        outputCode.delete(1.0, tk.END)
        ans = translateMIPS(lines)
        outputCode.insert(tk.INSERT, ans)

    def translateHEXButton():
        pass

    def clear():
        inputCode.delete(1.0, tk.END)
        outputCode.delete(1.0, tk.END)

    clearButton = tk.Button(buttons, text="Clear", command = clear, bd = 5)
    clearButton.grid(row = 0, column = 0, pady = 5, padx=5)
    cleanButton = tk.Button(buttons, text="Clean Code", command = cleanButton, bd = 5)
    cleanButton.grid(row = 0, column = 1, pady = 5, padx=5)
    translateMIPSButton = tk.Button(buttons, text="Translate MIPS", command = translateMIPSButton, bd = 5)
    translateMIPSButton.grid(row = 1, column = 0, pady = 2, padx=5)
    translateHEXButton = tk.Button(buttons, text="Translate HEX", command = translateHEXButton, bd = 5)
    translateHEXButton.grid(row = 1, column = 1, pady = 2, padx=5)
    window.pack()
    buttons.pack()
    root.mainloop()

main()
