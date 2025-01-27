import os
import tkinter as tk
import keyboard
import json

# Load settings
with open("settings.json", 'r') as settings:
    d = json.load(settings)
    main_path = d['path']
    hotkey_combination = d['hotkeys']

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
        project_path = os.path.join(root_folder, project)
        project_path = os.path.normpath(project_path)
        if os.path.exists(fr"{project_path}"):
            os.startfile(fr"{project_path}")

    else:
        root = tk.Tk()
        listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80)
        for folder in project_list:
            listbox.insert(tk.END, folder)
        listbox.pack()

        def choose_folder():
            selected_index = listbox.curselection()
            if selected_index:
                selected_folder = listbox.get(selected_index[0])
                project_path = os.path.join(main_path, selected_folder)
                project_path = os.path.normpath(project_path)
                if os.path.exists(fr"{project_path}"):
                    os.startfile(fr"{project_path}")
                root.destroy()
            else:
                print("Please select a folder from the list.")

        choose_button = tk.Button(root, text="Choose", command=choose_folder)
        choose_button.pack()

        root.mainloop()

def main():
    root = tk.Tk()
    root.geometry('300x200')
    root.title("Project Folder Opener")

    label = tk.Label(root, text="Enter Project Number:")
    label.pack()

    entry = tk.Entry(root, highlightthickness=2, highlightcolor='#A1D7FA')
    entry.pack()

    def open_folder(event=None):
        project_number = entry.get()
        open_project_folder(project_number, main_path)
        root.destroy()

    root.bind('<Return>', open_folder)

    button = tk.Button(root, text="Open Folder", command=open_folder)
    button.pack()
    root.focus_force()
    root.mainloop()

if __name__ == "__main__":
    # Register hotkey to open the main GUI
    keyboard.add_hotkey(hotkey_combination, main)
    
    # Keep the script running
    keyboard.wait()
