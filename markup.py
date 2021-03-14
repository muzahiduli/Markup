fullText = ""

def plain():
    text = input("- Text: ")
    return text

def bold(): 
    text = input('- Text: ')
    bold_text = f"**{text}**"
    return bold_text

def italic(): 
    text = input('- Text: ')
    italic_text = f"*{text}*"
    return italic_text

def inline_code():
    text = input('- Text: ')
    code_text = f"`{text}`"
    return code_text

def link():
    label = input("- Label: ")
    url = input("- URL: ")
    link_text = f"[{label}]({url})"
    return link_text

def header():
    level = int(input("- Level: "))
    while (level < 1 or level > 6):
        level = int(input("- Level: "))
    
    levelStr = ""
    for i in range(level):
        levelStr += "#"
    
    text = input('- Text: ')
    header_text = f"{levelStr} {text}" + "\n"
    return header_text

def line_break():
    return "\n"

def listing(ordType=None):
    rows = int(input("- Number of rows: "))
    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("- Number of rows: "))
    row_list = [input(f"- Row #{i+1}: ") + "\n" for i in range(rows)]

    row_text = ""
    if ordType == "ordered-list":
        for index, row in enumerate(row_list):
            row = f"{index+1}. {row}"
            row_text += row
    elif ordType == "unordered-list":
        for row in row_list:
            row = f"* {row}"
            row_text += row
    return row_text

def done():
    file = open("output.md", "w")
    file.write(fullText)
    file.close()
    exit()

def help():
    print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
Special commands: !help !done""")

def main():
    global fullText
    formatCommands = {"plain": plain, "bold": bold, "italic": italic, "link": link, "inline-code": inline_code,
                    "header": header, "ordered-list": listing, "unordered-list": listing, "line-break": line_break}

    while True:
        inp = input("- Choose a formatter: ")
        if inp == "!help":
            help()
        elif inp == "!done":
            done()
        elif inp in formatCommands:
            if inp == "ordered-list":
                fullText += formatCommands[inp]("ordered-list")
            elif inp == "unordered-list":
                fullText += formatCommands[inp]("unordered-list")
            else:
                fullText += formatCommands[inp]()
            print(fullText)
        else:
            print("Unknown formatting type or command. Please try again")

if __name__ == "__main__":
    main()