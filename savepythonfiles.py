import os
import shutil

def main():
    extensions = [".py"]

    downloads_folder = os.path.expanduser("C:/Users/sande/Downloads") #expands user directory path using os.path.expanduser()
    documents_folder = os.path.expanduser("C:/Users/sande/OneDrive/Documents")
    python_folder= os.path.expanduser("C:/Users/sande/OneDrive/Documents/Python Projects")

    downloads = os.listdir(downloads_folder) #lists what is in the folder
    documents = os.listdir(documents_folder)

    for download in downloads:
        _, extension = os.path.splitext(download) #breaks the file into two parts.  The base for _, and the extension in extension. splitext breaks it into two parts
        if extension in extensions:
            source_path = os.path.join(downloads_folder, download) #Joins the downloads folder path to the download file to create a full path
            destination_path = os.path.join(python_folder, download) #Joins the python folder path to the download file to set a destination path
            shutil.move(source_path, destination_path) #moves file from source path to destination path
            print(f"Moved {download} to {python_folder}")
        else:
            print(f"{download} is not an image file, nothing to move.")
    for document in documents:
        _, extension = os.path.splitext(document)
        if extension in extensions:
            source_path = os.path.join(documents_folder, document)
            destination_path = os.path.join(python_folder, document)
            shutil.move(source_path, destination_path)
            print(f"Moved {document} to {python_folder}")
        else:
            print(f"{document} is not a python file, nothing to move")

if __name__ == "__main__":
    main()