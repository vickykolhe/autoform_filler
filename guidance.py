import tkinter as tk
from text_to_speech import text_to_speech
from handler import read_pdf_fields
from googletrans import Translator
from PIL import Image, ImageTk  # For image handling

# Language mapping to Google TTS codes
language_mapping = {"english": "en", "hindi": "hi", "marathi": "mr"}
translator = Translator()

# Global variable for selected language
selected_language = None

# Field-to-Image Mapping
field_image_mapping = {
    "Name": r"images\adharcard.png",
    "Email": r"images\email.png",
    "Phone Number": r"images\phonenumber.png",
}


def load_guidance_form(root, form_name, language):
    """Load the form and provide field descriptions."""
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Load the form fields from the PDF
    pdf_path = f"{form_name}.pdf"  # Assuming the form is a PDF
    fields = read_pdf_fields(pdf_path)

    # Create a frame for the guidance
    guidance_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    guidance_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Display instructions
    instructions_label = tk.Label(
        guidance_frame,
        text="Guidance - Field Descriptions",
        font=("Helvetica", 20, "bold"),
        bg="#f7f7f7",
    )
    instructions_label.pack(pady=20)

    # Function to describe the current field
    def describe_field(index):
        from main import main_home_page

        if index < len(fields):
            field_name = fields[index]

            # Translate field name to the selected language if needed
            translated_field = translator.translate(field_name, dest=language).text

            # Construct the description message
            if language == "hi":  # Hindi
                prompt_text = f"आपका {translated_field} क्या है?"  # Example in Hindi
            elif language == "mr":  # Marathi
                prompt_text = f"तुमचा {translated_field} काय आहे?"  # Example in Marathi
            else:  # Default to English
                prompt_text = f"What is your {translated_field}?"  # Example in English

            # Use text-to-speech for the description
            text_to_speech(prompt_text, language=language)

            # Display the field description on the UI
            description_label.config(text=prompt_text)

            if field_name in field_image_mapping:
                image_path = field_image_mapping[field_name]
                img = Image.open(image_path)
                img = img.resize(
                    (300, 200), Image.Resampling.LANCZOS
                )  # Resize for better display
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                image_label.image = photo
            else:
                image_label.config(image=None)

            # Update button commands to repeat or proceed
            next_button.config(command=lambda: describe_field(index + 1))
            repeat_button.config(command=lambda: describe_field(index))

        else:
            # Show completion message
            completed_label = tk.Label(
                guidance_frame,
                text="Guidance Completed. Please go back to Home.",
                font=("Helvetica", 18, "bold"),
                bg="#FFEB3B",
            )
            completed_label.pack(pady=20)

            # Add a 'Go Back' button
            go_back_button = tk.Button(
                guidance_frame,
                text="Go Back",
                command=lambda: main_home_page(root),  # No need to pass root here
                font=("Helvetica", 16, "bold"),
                bg="#f44336",
                fg="white",
                activebackground="#f1351e",
                relief=tk.RAISED,
                bd=4,
            )
            go_back_button.pack(pady=20)

    # Initialize description label and buttons
    description_label = tk.Label(
        guidance_frame, text="", font=("Helvetica", 16), bg="#f7f7f7"
    )
    description_label.pack(pady=10)

    image_label = tk.Label(guidance_frame, bg="#f7f7f7")  # Label to display images
    image_label.pack(pady=10)

    # Next Field Button
    next_button = tk.Button(
        guidance_frame,
        text="Next Field",
        command=lambda: describe_field(1),  # Start from the second field
        font=("Helvetica", 14, "bold"),
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        relief=tk.RAISED,
        bd=4,
    )
    next_button.pack(pady=10)

    # Repeat Field Button
    repeat_button = tk.Button(
        guidance_frame,
        text="Repeat",
        command=lambda: describe_field(0),  # Repeat the first field
        font=("Helvetica", 14, "bold"),
        bg="#FF9800",
        fg="white",
        activebackground="#ff8c1a",
        relief=tk.RAISED,
        bd=4,
    )
    repeat_button.pack(pady=10)

    # Start the guidance for the first field
    describe_field(0)


def show_guidance_language_selection(root, forms):
    """Display language selection screen for guidance."""
    global selected_language
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for language selection
    selection_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    selection_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Language selection label
    lang_label = tk.Label(
        selection_frame,
        text="Select a Language for Guidance:",
        font=("Helvetica", 20, "bold"),
        bg="#f7f7f7",
    )
    lang_label.pack(pady=20)

    # Create buttons for language selection
    languages = ["English", "Hindi", "Marathi"]
    for lang in languages:
        button = tk.Button(
            selection_frame,
            text=lang,
            command=lambda ln=lang.lower(): select_language_for_guidance(
                ln, root, forms
            ),
            font=("Helvetica", 16, "bold"),
            height=2,
            width=15,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            relief=tk.RAISED,
            bd=4,
        )
        button.pack(pady=10)


def select_language_for_guidance(language, root, forms):
    """Handle language selection for guidance and show form selection."""
    global selected_language
    selected_language = language_mapping[language]
    show_guidance_form_selection(root, forms)


def show_guidance_form_selection(root, forms):
    """Display form selection after language is chosen."""
    # Clear the window for form selection
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for form selection
    selection_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    selection_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Form selection label
    form_label = tk.Label(
        selection_frame,
        text="Select a Form for Guidance:",
        font=("Helvetica", 20, "bold"),
        bg="#f7f7f7",
    )
    form_label.pack(pady=20)

    # Create buttons for form selection
    for form_name in forms.keys():
        button = tk.Button(
            selection_frame,
            text=form_name,
            command=lambda fn=form_name: load_guidance_form(
                root, fn, selected_language
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
