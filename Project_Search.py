import os
import tkinter as tk
from tkinter import simpledialog

main_path = '/Users/seth/Documents'

def list_projects(project_number, root_path):
    folder_list = os.listdir(root_path)
    results = [i for i in folder_list if project_number.lower() in i.lower()]
    return results

def open_project_folder(project_number, root_folder):
    project_list = list_projects(project_number, root_folder)

    if not project_list:
        root = tk.Tk()
        root.title("No Matching Folders")
        
        message_label = tk.Label(root, text="No matching folders found.")
        message_label.pack()
        
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack()
        
        root.mainloop()
        root.destroy()
        return

    elif len(project_list) == 1:
        project = project_list[0]

    else:
        
        folder_list_string = '\n'.join(project_list)
        message = f"Multiple folders found for project number {project_number}:\n\n{folder_list_string}\n\nEnter the project folder name you want to open:"
        project = tk.simpledialog.askstring("Choose a Folder", message)

        if project not in project_list:
            print('Invalid Folder Name Selected')
            return
        
    project_path = os.path.join(root_folder, project)
    if os.path.exists(project_path):
        os.system(f'open "{project_path}"')

def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Project Folder Opener")

    label = tk.Label(root, text="Enter Project Number:")
    label.pack()

    entry = tk.Entry(root, highlightthickness=2, highlightcolor='#A1D7FA')
    entry.pack()

    def open_folder():
        project_number = entry.get()
        open_project_folder(project_number, main_path)
        root.destroy()


    button = tk.Button(root, text="Open Folder", command=open_folder)
    button.pack()

    # Listen for the keyboard shortcut (e.g., Ctrl+Alt+P)
   # keyboard.add_hotkey('ctrl+alt+p', open_folder)

    root.mainloop()

if __name__ == "__main__":
    main()