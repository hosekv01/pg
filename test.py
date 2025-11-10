#Otevře link v chromu

import webbrowser

def link_otevreni(url):
    webbrowser.open(url)

if __name__ == "__main__":
    odkaz = input("Zadej URL odkaz: ")
    link_otevreni(odkaz)