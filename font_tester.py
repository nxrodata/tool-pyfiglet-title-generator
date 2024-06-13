# This file loops through all the fonts in 'pyfiglet_fonts.txt' and writes the output of each font to 'output.txt'
import pyfiglet

with open("pyfiglet_fonts.txt", "r", encoding="utf-8") as file:
    fonts = file.read().splitlines()

def test_fonts(fonts, text, width):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for font in fonts:
            out_file.write(f"{font}--------------------------\n\n")
            f = pyfiglet.Figlet(font=font, width=width)
            out_file.write(f.renderText(text))
            out_file.write("\n--------------------------------\n\n")
    
if __name__ == "__main__":
    text = ""
    width = 200
    output_file = "output.txt"
    test_fonts(fonts, text, width)