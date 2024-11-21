import tkinter as tk
from handler import load_form
from guidance import show_guidance_language_selection
from tkinter import simpledialog
import json

# Load form definitions from JSON file (if applicable)
with open("forms.json") as f:
    forms = json.load(f)

# Language mapping to Google TTS codes
language_mapping = {"english": "en", "hindi": "hi", "marathi": "mr"}

# Global variable to hold the selected language
selected_language = None


def select_language(language, root):
    """Function to handle language selection."""
    global selected_language
    selected_language = language_mapping[language]  # Set the selected language
    display_selection_screen(root)  # Display the selection screen


def display_selection_screen(root):
    """Function to display language and form selection on the same screen."""
    # Clear the window for selection
    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame for the selection
    selection_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    selection_frame.pack(pady=20, padx=20, fill=tk.BOTH)

    # Create a label for instructions
    instructions_label = tk.Label(
        selection_frame,
        text="Select Language and Form:",
        font=("Helvetica", 20, "bold"),
        bg="#f7f7f7",
    )
    instructions_label.pack(pady=10)

    # Create a frame for language selection
    lang_frame = tk.Frame(selection_frame, bg="#f7f7f7")
    lang_frame.pack(pady=20)

    # Create language selection buttons
    languages = ["English", "Hindi", "Marathi"]
    for lang in languages:
        button = tk.Button(
            lang_frame,
            text=lang,
            command=lambda ln=lang.lower(): select_language(ln, root),
            font=("Helvetica", 16, "bold"),
            height=2,
            width=10,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            relief=tk.RAISED,
            bd=4,
        )
        button.pack(side=tk.LEFT, padx=10)  # Added padding between buttons

    # Create a frame for form selection with border and padding
    form_frame = tk.Frame(selection_frame, bg="#f7f7f7")
    form_frame.pack(pady=20)

    # Create buttons for form selection
    for form_name in forms.keys():
        button = tk.Button(
            form_frame,
            text=form_name,
            command=lambda fn=form_name: (
                load_form(root, fn, forms, selected_language)
                if selected_language
                else None
            ),
            font=("Helvetica", 16, "bold"),
            height=2,
            width=25,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            relief=tk.RAISED,
            bd=4,
        )
        button.pack(pady=10)


def open_guidance(root):
    show_guidance_language_selection(root, forms)


def main_home_page(root):
    """Function to display the main home page with two buttons."""
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Title of the main page
    title_label = tk.Label(
        root,
        text="Welcome to the Form System",
        font=("Helvetica", 24, "bold"),
        bg="#4A90E2",
        fg="white",
    )
    title_label.pack(pady=20, fill=tk.X)

    home_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    home_frame.pack(pady=30, padx=30, fill=tk.BOTH)

    # Create buttons for Guidance and Form Filling
    guidance_button = tk.Button(
        home_frame,
        text="Guidance",
        command=lambda: open_guidance(root),
        font=("Helvetica", 16, "bold"),
        height=2,
        width=25,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        relief=tk.RAISED,
        bd=4,
    )
    guidance_button.pack(pady=20)

    form_filling_button = tk.Button(
        home_frame,
        text="Form Filling",
        command=lambda: display_selection_screen(
            root
        ),  # Update to show selection screen
        font=("Helvetica", 16, "bold"),
        height=2,
        width=25,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        relief=tk.RAISED,
        bd=4,
    )
    form_filling_button.pack(pady=20)


def main():
    global root
    root = tk.Tk()
    root.title("Main Home Page")

    # Set the background color of the root window
    root.configure(bg="#E0E0E0")

    # Set the window size
    root.geometry("800x600")

    # Show the main home page with Guidance and Form Filling buttons
    main_home_page(root)

    root.mainloop()


if __name__ == "__main__":
    main()
