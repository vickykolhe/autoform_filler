# guidance_system.py

import tkinter as tk
from text_to_speech import text_to_speech
from googletrans import Translator

translator = Translator()  # Initialize the translator


def start_guided_mode(root, forms, selected_form, language):
    """Function to guide the user through the form fields one by one."""

    # Retrieve form fields from the JSON structure
    fields = forms[selected_form]

    # Create a frame for guidance mode
    guidance_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief=tk.GROOVE)
    guidance_frame.pack(pady=20, padx=20, fill=tk.BOTH)

    # Display the form title
    title_label = tk.Label(
        guidance_frame,
        text=f"Guided Mode for {selected_form}",
        font=("Helvetica", 18, "bold"),
        bg="#f7f7f7",
    )
    title_label.pack(pady=10)

    # Instructions for navigating through fields
    instruction_label = tk.Label(
        guidance_frame,
        text="Listen to each field's description and press 'Next' to proceed.",
        font=("Helvetica", 12),
        bg="#f7f7f7",
    )
    instruction_label.pack(pady=5)

    # Field index for guidance navigation
    field_index = 0

    def speak_field_description(index):
        """Function to provide audio guidance for the current field."""
        if index < len(fields):
            field_name = fields[index]

            # Translate field label to the selected language if needed
            translated_field = translator.translate(field_name, dest=language).text

            # Construct the guidance text
            if language == "hi":  # Hindi
                guidance_text = f"यह {translated_field} फ़ील्ड है।"
            elif language == "mr":  # Marathi
                guidance_text = f"हे {translated_field} फील्ड आहे."
            else:  # Default to English
                guidance_text = f"This is the {translated_field} field."

            # Text-to-speech output for guidance
            text_to_speech(guidance_text, language=language)

            # Update the current field label in the UI
            current_field_label.config(text=f"Field: {field_name}")
        else:
            # End of fields; show completion message
            text_to_speech(
                "You have completed the guidance for all fields.", language=language
            )
            current_field_label.config(text="Guidance complete.")

    # Label to show the current field name
    current_field_label = tk.Label(guidance_frame, font=("Helvetica", 14), bg="#f7f7f7")
    current_field_label.pack(pady=20)

    # "Next" button to move to the next field
    def next_field():
        nonlocal field_index
        field_index += 1
        speak_field_description(field_index)

    next_button = tk.Button(
        guidance_frame,
        text="Next",
        command=next_field,
        font=("Helvetica", 14, "bold"),
        bg="#4CAF50",
        fg="white",
        height=2,
        width=15,
        relief=tk.RAISED,
    )
    next_button.pack(pady=10)

    # Start by describing the first field
    speak_field_description(field_index)

    # Back to Home Button
    back_button = tk.Button(
        root,
        text="Back to Home",
        command=lambda: root.destroy(),
        font=("Helvetica", 14, "bold"),
        bg="#f44336",
        fg="white",
        height=2,
        width=15,
        activebackground="#e53935",
        relief=tk.RAISED,
    )
    back_button.pack(pady=20)
