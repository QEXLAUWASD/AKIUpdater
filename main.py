# only can run on windows
import os
import zipfile
import gdown


gitrepo = "https://github.com/QEXLAUWASD/AKIUpdater.git"


if __name__ == "__main__":
    # from google drive download the client zip file and extract it to the same directory(url https://drive.google.com/file/d/1INa9wAych3lDnQAYX5pkif74KZxP1mvD/view?usp=sharing)
    # check if the file not exists
    if not os.path.exists("client.zip"):
        print("Downloading the client")
        gdown.download("https://drive.google.com/uc?id=1INa9wAych3lDnQAYX5pkif74KZxP1mvD", "client.zip", quiet=False)
        print("Downloaded the client")
        # extract the file
        print("Extracting the client")
        with zipfile.ZipFile("client.zip", 'r') as zip_ref:
            zip_ref.extractall()
        print("Extracted the client")
        # remove the zip file
        os.remove("client.zip")
    else:
        print("The client.zip already exists")
        # check if the folder EscapeFromTarkov_Data exists
        if os.path.exists("EscapeFromTarkov_Data"):
            print("The client already installed")
        else:
            with open("客戶端.zip", "r") as zip_ref:
                zip_ref.extractall()    
            print("The client installed")
    
    # install SP-Tarkov Server from google drive(url https://drive.google.com/file/d/1jJNh9L2dQsI7dy0F3jB0yKUrdU4qvyuo/view?usp=drive_link)
    # check if the file not exists
    if not os.path.exists("Server.zip"):
        print("Downloading the server")
        gdown.download("https://drive.google.com/uc?id=1jJNh9L2dQsI7dy0F3jB0yKUrdU4qvyuo", "Server.zip", quiet=False)
        print("Downloaded the server")
        # extract the file
        print("Extracting the server")
        with zipfile.ZipFile("Server.zip", 'r') as zip_ref:
            zip_ref.extractall()
        print("Extracted the server")
        # remove the zip file
        os.remove("Server.zip")
    else:
        print("The Server.zip already exists")
        # check if the file SPT.Launcher.exe exists
        if os.path.exists("SPT.Launcher.exe"):
            print("The server already installed")
        else:
            with open("Server.zip", "r") as zip_ref:
                zip_ref.extractall()    
            print("The server installed")
    

    # check the version.txt file in the same directory
    with open("version.txt", "r") as f:
        version = f.read()
    # check the version from github
    url = "https://raw.githubusercontent.com/QEXLAUWASD/AKIUpdater/main/version.txt"
    # check if the version is the same
    if version != url:
        # download new version
        print("Downloading new version")
        os.system(f"git clone {gitrepo}")
        print("Downloaded new version")
    else:
        print("You have the latest version")
        exit(0)

