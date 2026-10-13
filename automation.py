import os
import shutil

print("================================")
print("   GANESH AUTOMATION ASSISTANT")
print("================================")

while True:
    print("\nChoose an automation task:")
    print("1. Create a folder")
    print("2. Create a text file")
    print("3. Write text to a file")
    print("4. List files in a folder")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        folder_name = input("Enter folder name: ")

        os.makedirs(folder_name, exist_ok=True)

        print("Folder created successfully!")

    elif choice == "2":
        file_name = input("Enter file name (example.txt): ")

        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Created by Ganesh Automation Assistant.")

        print("Text file created successfully!")

    elif choice == "3":
        file_name = input("Enter file name: ")
        text = input("Enter the text to save: ")

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text)

        print("Text saved successfully!")

    elif choice == "4":
        folder_name = input("Enter folder path (press Enter for current folder): ")

        if folder_name == "":
            folder_name = "."

        if os.path.isdir(folder_name):
            print("Files and folders:")

            for item in os.listdir(folder_name):
                print("-", item)

        else:
            print("Folder not found!")

    elif choice == "5":
        print("Goodbye! Automation completed.")
        break

    else:
        print("Invalid choice! Enter 1 to 5.")
        