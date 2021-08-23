import requests
from colorama import Fore
from os import system

system("cls")
def main():
    try:

        filename = input(Fore.CYAN + """                 
                                           _   _  ____  _   _ ______ _____ _      ______ 
                                     /\   | \ | |/ __ \| \ | |  ____|_   _| |    |  ____|
                                    /  \  |  \| | |  | |  \| | |__    | | | |    | |__   
                                   / /\ \ | . ` | |  | | . ` |  __|   | | | |    |  __|  
                                  / ____ \| |\  | |__| | |\  | |     _| |_| |____| |____ 
                                 /_/    \_\_| \_|\____/|_| \_|_|    |_____|______|______|
                                                                              
                                    Put the file you want to upload at the same
                                    directory of this program and type your file's name.
                                    Ex : filename.rar

                    
                                                    Filename : """)
        files = {
            "file": (filename, "filepath", "rb")
        }

        upload = requests.post("https://api.anonfiles.com/upload", files=files)

        try:

            system("cls") 
            x = upload.json()
            url = x["data"]["file"]["url"]["short"]
            print(Fore.LIGHTRED_EX + "File uploaded : " + url)
            print()
            restart = input(Fore.MAGENTA + """Upload an another file ?
[y/n] : """)
            if restart == "y":
                main()
            else:
                quit()
        except Exception as e:
            print(e)
            # can't get download link.
    
    except Exception as e:
        print(e)
main()
