import pyfiglet

def create_ascii_art(text,font, width):
    ascii_art = pyfiglet.figlet_format(text, font, width)
    return ascii_art

if __name__ == "__main__":
    text = "" 
    font = "" 
    width = "100"
    print(create_ascii_art(text,font, width))