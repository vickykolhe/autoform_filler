import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame
from text_to_speech import text_to_speech
from handle import read_pdf_fields, fill_pdf_form
from database import save_to_db, get_user_data
from googletrans import Translator
from tkinter import simpledialog
import speech_recognition as sr

from tkinter import PhotoImage
from PIL import Image, ImageTk

# from guidance import show_guidance_language_selection

LABEL_FONT = ("Helvetica", 12)
ENTRY_WIDTH = 30
translator = Translator()  # Initialize the translator

# Language mapping to Google TTS codes
language_mapping = {"english": "en", "hindi": "hi", "marathi": "mr"}
selected_language = None  # To store the selected language


def guided_form_filling(root, form_name, forms, language):
    for widget in root.winfo_children():
        widget.destroy()

    fields = read_pdf_fields(f"{form_name}.pdf")
    form_data = {}

    def prompt_field(index):
        if index < len(fields):
            field = fields[index]
            translated_field = translator.translate(field, dest=language).text
            prompt_text = (
                f"Please enter your {translated_field}."
                if language == "en"
                else f"कृपया अपना {translated_field} दर्ज करें।"
            )

            text_to_speech(prompt_text, language=language)

            entry = tk.Entry(root, width=ENTRY_WIDTH)
            entry.pack(pady=10)

            def save_entry():
                form_data[field] = entry.get()
                entry.destroy()
                prompt_field(index + 1)

            entry.bind("<Return>", lambda _: save_entry())
        else:
            tk.Label(root, text="Guided form complete.", font=LABEL_FONT).pack()

    prompt_field(0)


# Voice input function
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(
            source, duration=1
        )  # Adjust for ambient noise
        print("Please speak now...")
        audio = recognizer.listen(
            source, timeout=5
        )  # Timeout if no speech is detected within 5 seconds
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""


def submit_form(
    user_id, form_name, form_data, user_name, pdf_path, root, forms, language
):
    from main import main_home_page

    # Generate the filled PDF
    output_pdf_path = f"{form_name}_{user_name}.pdf"  # Unique name
    fill_pdf_form(pdf_path, form_data, output_pdf_path)
    print(f"Filled PDF saved as {output_pdf_path}!")

    # Save form data to the database
    for field_name, field_value in form_data.items():
        save_to_db(user_id, form_name, field_name, field_value)

    # reset_to_home(root, forms)
    main_home_page(root)


def load_form(root, form_name, forms, language):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Prompt user for their identifier (last four digits of Aadhaar)
    # Translate the prompt for the Aadhaar number
    if language == "hi":  # Hindi
        aadhaar_prompt = "कृपया अपने आधार कार्ड के अंतिम चार अंक दर्ज करें।"
    elif language == "mr":  # Marathi
        aadhaar_prompt = "कृपया आपल्या आधार कार्डचे शेवटचे चार अंक प्रविष्ट करा."
    else:  # Default to English
        aadhaar_prompt = "Please enter the last four digits of your Aadhaar card."

    # Play the Aadhaar prompt using text-to-speech
    text_to_speech(aadhaar_prompt, language=language)

    # Prompt user for their identifier (last four digits of Aadhaar)
    user_id = simpledialog.askstring("Input", aadhaar_prompt)

    # Load the fields from the PDF form
    pdf_path = f"{form_name}.pdf"  # Assuming PDF names are form1.pdf and form2.pdf
    fields = read_pdf_fields(pdf_path)
    form_data = {}
    user_name = None  # Variable to store the user's name

    # Retrieve user data from the database
    existing_data = get_user_data(user_id, form_name)

    # Create a canvas for scrolling
    canvas = Canvas(root, bg="#f7f7f7")
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    # Configure the scrollable frame
    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a window in the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a frame for the form fields, centered in the canvas
    form_frame = Frame(scrollable_frame, bg="#f7f7f7")
    form_frame.pack(pady=20)

    # Create labels and entry fields for all form fields
    entries = {}
    for index, field in enumerate(fields):
        label = tk.Label(form_frame, text=f"{field}:", font=LABEL_FONT, bg="#f7f7f7")
        label.grid(row=index, column=0, sticky=tk.W, pady=5, padx=5)

        entry = tk.Entry(form_frame, width=ENTRY_WIDTH)
        entry.grid(row=index, column=1, pady=5, padx=5)

        # Pre-fill entry with existing data if available
        if field in existing_data:
            entry.insert(0, existing_data[field])

        entries[field] = entry  # Store entry widget to access later

    def display_form_image(form_name):
        try:
            # Assuming the images are stored as form1.jpg, form2.jpg, etc.
            image_path = f"images/{form_name}.png"  # Replace with actual image paths
            img = Image.open(image_path)
            img = img.resize((500, 600), Image.Resampling.LANCZOS)  # Resize as needed
            photo = ImageTk.PhotoImage(img)

            image_label = tk.Label(root, image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack(side="right", padx=50)  # Display the image on the right
        except Exception as e:
            print(f"Error loading image: {e}")

    display_form_image(form_name)

    # Function to read the current field and prompt the user
    def prompt_current_field(index):
        if index < len(fields):
            field_name = fields[index]

            # Translate field label to the selected language if needed
            translated_field = translator.translate(
                field_name, dest=language
            ).text  # Translate the field name

            # Construct the full prompt text
            if language == "hi":  # Hindi
                prompt_text = (
                    f"आपका {translated_field} क्या है?"  # Construct the Hindi prompt
                )
            elif language == "mr":  # Marathi
                prompt_text = (
                    f"तुमचा {translated_field} काय आहे?"  # Construct the Marathi prompt
                )
            else:  # Default to English
                prompt_text = f"What is your {translated_field}?"  # Prompt in English

            # Prompt user with translated text
            text_to_speech(prompt_text, language=language)  # Text-to-speech prompt

            # Focus on the current entry field
            entries[field_name].focus()
            input_frame = tk.Frame(form_frame, bg="#f7f7f7")
            input_frame.grid(row=index, column=2, pady=5, padx=5)

            # Function to handle voice input
            def handle_voice_input():
                voice_input = get_voice_input()
                entries[field_name].delete(0, tk.END)
                entries[field_name].insert(0, voice_input)
                form_data[field_name] = voice_input
                save_to_db(user_id, form_name, field_name, voice_input)
                input_frame.destroy()  # Remove input buttons
                prompt_current_field(index + 1)

            def handle_text_input():
                def on_enter(event):
                    user_input = entries[field_name].get()
                    form_data[field_name] = user_input
                    save_to_db(user_id, form_name, field_name, user_input)
                    input_frame.destroy()  # Remove input buttons
                    prompt_current_field(index + 1)

                entries[field_name].bind("<Return>", on_enter)

            voice_button = tk.Button(
                input_frame,
                text="Voice (V)",
                command=handle_voice_input,
                bg="#4CAF50",
                fg="white",
                font=("Helvetica", 10, "bold"),
                width=10,
            )
            voice_button.pack(side=tk.LEFT, padx=5)

            text_button = tk.Button(
                input_frame,
                text="Type (T)",
                command=handle_text_input,
                bg="#2196F3",
                fg="white",
                font=("Helvetica", 10, "bold"),
                width=10,
            )
            text_button.pack(side=tk.LEFT, padx=5)

            # print("Press 'T' to type or 'V' for voice input.")

            def on_key_press(event):
                if event.char.lower() == "v":
                    handle_voice_input()
                elif event.char.lower() == "t":
                    handle_text_input()

            root.bind("<KeyPress>", on_key_press)

        else:

            user_name = entries.get("Name", tk.Entry()).get() or "Unknown"
            # Add a submit button when all fields are filled
            submit_button = tk.Button(
                form_frame,
                text="Submit",
                command=lambda: submit_form(
                    user_id,
                    form_name,
                    {
                        field: entries[field].get() for field in fields
                    },  # Collect current data
                    user_name,
                    pdf_path,
                    root,
                    forms,
                    language,
                ),
                bg="#4CAF50",
                fg="white",
                font=("Helvetica", 16, "bold"),
                height=2,
                width=15,
            )
            submit_button.grid(row=len(fields), columnspan=2, pady=20)

    # Start prompting for the first field
    prompt_current_field(0)
