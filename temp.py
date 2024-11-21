# import json
# import tkinter as tk
# from text_to_speech import text_to_speech
# from database import save_to_db
# from pdf_generator import generate_pdf
# from styles import (
#     BUTTON_COLOR,
#     LABEL_FONT,
#     TITLE_FONT,
#     ENTRY_WIDTH,
#     BUTTON_WIDTH,
#     BUTTON_PADY,
# )

# # Load form definitions from JSON file
# with open("forms.json") as f:
#     forms = json.load(f)


# def load_form(root, form_name):
#     # Clear the window
#     for widget in root.winfo_children():
#         widget.destroy()

#     fields = forms[form_name]
#     form_data = {}
#     user_name = None  # Variable to store the user's name
#     current_field_index = 0  # To track the current field being filled

#     # Frame for the form fields
#     form_frame = tk.Frame(root)
#     form_frame.pack(pady=20)

#     # Create labels and entry fields for all form fields
#     entries = {}
#     for field in fields:
#         label = tk.Label(form_frame, text=f"{field}:", font=LABEL_FONT)
#         label.pack()
#         entry = tk.Entry(form_frame, width=ENTRY_WIDTH)
#         entry.pack()
#         entries[field] = entry  # Store entry widget to access later

#     # Function to read the current field and prompt the user
#     def prompt_current_field(index):
#         if index < len(fields):
#             field_name = fields[index]
#             text_to_speech(f"What is your {field_name}?")  # Text-to-speech prompt

#             # Focus on the current entry field
#             entries[field_name].focus()

#             # Bind Enter key to handle input for the current field
#             def on_enter(event):
#                 nonlocal user_name
#                 user_input = entries[field_name].get()
#                 if field_name.lower() == "name":
#                     user_name = user_input  # Store the user's name
#                 form_data[field_name] = user_input
#                 save_to_db(form_name, field_name, user_input)

#                 # Move to the next field
#                 prompt_current_field(index + 1)  # Prompt next field

#             entries[field_name].bind(
#                 "<Return>", on_enter
#             )  # Bind Enter key to the function

#             # Call the prompt function for the next field after the current one
#         else:
#             generate_pdf(form_name, form_data, user_name)  # Pass user's name
#             print("Form completed!")
#             reset_to_home(root)  # Return to the main form selection

#     # Start prompting for the first field
#     prompt_current_field(current_field_index)


# def reset_to_home(root):
#     # Clear the window
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Frame for the form selection
#     home_frame = tk.Frame(root)
#     home_frame.pack(pady=20)

#     for form_name in forms.keys():
#         button = tk.Button(
#             home_frame,
#             text=form_name,
#             command=lambda fn=form_name: load_form(root, fn),
#             bg=BUTTON_COLOR,
#             width=BUTTON_WIDTH,
#         )
#         button.pack(pady=BUTTON_PADY)


# import tkinter as tk
# from form_handler import load_form, reset_to_home

# # Tkinter window setup
# root = tk.Tk()
# root.title("Form Selection")

# # Initialize the main form selection
# reset_to_home(root)  # Pass root to reset_to_home

# root.mainloop()


# from pdfrw import PdfReader, PdfWriter, PdfDict
# import pyttsx3


# # Function to read form fields from a PDF
# def read_pdf_form(input_path):
#     pdf = PdfReader(input_path)
#     annotations = pdf.pages[0]["/Annots"]

#     field_data = {}
#     for annotation in annotations:
#         field_name = annotation["/T"][1:-1]  # Strip parentheses

#         # Safely extract the field value, ensuring it's properly decoded
#         field_value = annotation.get(
#             "/V", PdfDict()
#         )  # If no value, return an empty PdfDict

#         # Check if field_value is a valid string and convert it to a readable format
#         if isinstance(field_value, PdfDict):
#             field_value = "(No Value)"
#         elif isinstance(field_value, str):
#             field_value = field_value[1:-1]  # Remove parentheses

#         field_data[field_name] = field_value
#         print(f"Field Name: {field_name}, Field Value: {field_value}")

#     return field_data


# # Function to convert text to speech using pyttsx3
# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()


# # Function to update form fields
# def fill_pdf_form(input_path, output_path, field_updates):
#     pdf = PdfReader(input_path)
#     annotations = pdf.pages[0]["/Annots"]

#     for annotation in annotations:
#         field_name = annotation["/T"][1:-1]
#         if field_name in field_updates:
#             annotation.update(
#                 PdfDict(V=f"({field_updates[field_name]})")  # Update the value
#             )

#     PdfWriter(output_path, trailer=pdf).write()


# # Example of using the functions
# pdf_path = "output_form_with_fields.pdf"  # The PDF generated earlier

# # Read fields and convert their content to speech
# fields = read_pdf_form(pdf_path)
# for field_name, field_value in fields.items():
#     text_to_speech(f"The field {field_name} has value {field_value}")

# # Fill the "Name" field with new content and save as a new PDF
# fill_pdf_form(pdf_path, "filled_output_form.pdf", {"Name": "John Doe"})

# # Read the updated form fields
# print("Updated PDF form:")
# updated_fields = read_pdf_form("filled_output_form.pdf")


import tkinter as tk
from handler import load_form
import json

# Load form definitions from JSON file (if applicable)
with open("forms.json") as f:
    forms = json.load(f)

# Language mapping to Google TTS codes
language_mapping = {"english": "en", "hindi": "hi", "marathi": "mr"}

# Global variable to hold the selected language
selected_language = None


def select_language(language):
    """Function to handle language selection."""
    global selected_language
    selected_language = language_mapping[language]  # Set the selected language
    show_form_selection()  # Show forms with the selected language


def show_form_selection():
    """Function to display form selection after language is chosen."""
    # Clear the window for form selection
    for widget in root.winfo_children():
        widget.destroy()

    # Title for form selection
    title_label = tk.Label(
        root,
        text="Select a Form",
        font=("Helvetica", 20, "bold"),
        bg="#4A90E2",
        fg="white",
    )
    title_label.pack(pady=20, fill=tk.X)

    # Create a frame for form selection with border and padding
    form_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    form_frame.pack(pady=20, padx=20, fill=tk.BOTH)

    # Create buttons for form selection with modern styling
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
            bg="#4CAF50",  # Green background
            fg="white",  # White text
            activebackground="#45a049",  # Hover effect
            relief=tk.RAISED,
            bd=4,
        )
        button.pack(pady=10)

    # Back button
    back_button = tk.Button(
        root,
        text="Back to Home",
        command=main_home_page,
        font=("Helvetica", 14, "bold"),
        bg="#f44336",
        fg="white",
        height=2,
        width=15,
        activebackground="#e53935",
        relief=tk.RAISED,
    )
    back_button.pack(pady=20)


def open_form_filling():
    """Function to navigate to the form-filling process."""
    show_form_selection()


def open_guidance():
    """Function for guidance section, currently empty."""
    # Clear the window and display a guidance message
    for widget in root.winfo_children():
        widget.destroy()

    # Display "Under Construction" message for now
    guidance_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    guidance_frame.pack(pady=20, padx=20, fill=tk.BOTH)

    guidance_label = tk.Label(
        guidance_frame,
        text="Guidance is under construction.",
        font=("Helvetica", 18, "bold"),
        bg="#FFEB3B",
    )
    guidance_label.pack(pady=30)

    # Back button to go to home
    back_button = tk.Button(
        root,
        text="Back to Home",
        command=main_home_page,
        font=("Helvetica", 14, "bold"),
        bg="#f44336",
        fg="white",
        height=2,
        width=15,
        activebackground="#e53935",
        relief=tk.RAISED,
    )
    back_button.pack(pady=20)


def main_home_page():
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

    # Create a frame for the main menu buttons with padding
    home_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    home_frame.pack(pady=30, padx=30, fill=tk.BOTH)

    # Guidance button with enhanced style
    guidance_button = tk.Button(
        home_frame,
        text="Guidance",
        command=open_guidance,
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

    # Form Filling button with enhanced style
    form_filling_button = tk.Button(
        home_frame,
        text="Form Filling",
        command=open_form_filling,
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
    root.title("Advanced Form System")

    # Set the background color of the root window
    root.configure(bg="#E0E0E0")

    # Set the window size
    root.geometry("800x600")

    # Show the main home page
    main_home_page()

    root.mainloop()


if __name__ == "__main__":
    main()
