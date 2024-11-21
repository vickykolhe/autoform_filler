# Automatic Form Filler Using TTS and STT

# Introduction 

In many places like banks, government offices and public services, majority of the population faces difficulties in filling out complex forms due to language barriers, illiteracy , etc.This research presents the development of an innovative form-filling system to assist users in real time through authentic communication, text-to-speech and support for multiple languages.The system allows users to interact with it through speech and then converting their spoken input into text using a speech-to-text mechanism  and then type it in the field.
This not only provides more accuracy in written form, but also reduces the skill of the user who has difficulty writing the form manually.The project have two primary functionalities: form filling and guidance.

Form Filling:In this mode the user is guided through the form fields by converting the form field into speech by using the text-to-speech mechanism. The user then responds with their input,and these inputs are transcribed into the corresponding form field using the speech-to-text mechanism. The filled form is then saved as a PDF with the user name which was given by the user during the form filling and also all information is stored into the database for the future reference and validation . The system supports multiple languages, including English, Hindi, and Marathi,and allowing users to choose their preferred language for further interaction with the system.
The language selection and form selection interfaces are presented together which makes the system less complex and user friendly.

Guidance System:In this mode the user is guided through the form fields by converting the form field into speech by using the text-to-speech mechanism.Difference is, the guidance system is designed to assist users and provide the information about the field.This mode is designed to help users who want to fill out the form themselves but need help understanding what information is required at each location. Users can choose the direction and receive instructions in their favorite language, making the paper writing process clearer and less tedious.

This dual-system approach offers flexibility,to meet the needs of users who need general assistance in filling out the form or simply needs the guidence about the fields present in the forms.  The system integrates speech recognition and multilingual speech-to-speech, improving accessibility and user experience in critical environments where originality and user preferences are important.


# Methodology

The primary objective of this project is to assist users, particularly in government and banking environments, in filling out forms accurately and efficiently through a speech-enabled system.The system is divided into two functionalities: form filling and guidance, each implemented through specific components and technologies.

1. System Architecture :
The project architecture consists of a combination of front-end and back-end components.The user interface was built using Tkinter, a Python library for creating graphical user interfaces. Back-end functionality, including speech recognition, text-to-speech conversion,and form manipulation, is implemented using a variety of Python libraries,such as:
Google Text-to-Speech (gTTS) for multilingual speech.
Vosk for instant speech to text changes.
PyPDF2 reads, edits, and creates PDF files.
Googletrans supports automatic domain name translation.

The project integrates a database system to store information so that in future the user can automatically fill any form without giving the input for the fields which was stored in the database in past when the user filled the form first time.

2. Form Filling System :
The form-filling mode guide the user through each form field in real-time,The process for this feature follows these steps.
Language and Form Selection: Users first select their preferred language (e.g. English, Hindi, Marathi) from the interface. After selecting a language,the user have to select the form which they want to fill out.
Speech Recognition: For each response type, the system uses text-to-speech to read the written text aloud and prompts the user to respond to the message. Use the Vosk speech recognition engine which is the power full library in the python for speech recognition to capture user responses and transcribe them into text.
Data Entry and Validation:The output is entered into a combined form. At the same time, the system uses information stored in the database  to validate the input and correct minor or inconsistent input if the user is not new to fill the form. If an error is found, the user will be asked to provide the correct information.
Form Submission:Once all fields are filled in, the form will be saved in PDF format with a unique name that includes the user name and format. The PDF is stored in the system for future access or editing.

3. Guidance System:
The guidance system is designed to help users understand the form without filling it out. The system provides voice prompts explaining what information is required for each form. The process includes,
Language and Form Selection:Users first select their preferred language (e.g. English, Hindi, Marathi) from the interface. After selecting a language,the user have to select the form for which they want the guidance.
Field Guidance: The system reads the label of each form out loud and explains exactly what needs to be done in the field.For example, if the field is "Date of Birth", the system will explain: "Please enter your date of birth in the format DD/MM/YYYY."
User Engagement:This type of guidance does not require user input, but provides the necessary information to prepare their responses in advance. This is especially useful for users who want to fill in information before interacting with the form or who are unfamiliar with the application form.

4. Speech and Language Processing:
system revolves around speech-to-text and text-to-speech capabilities,
Text-to-Speech:The gTTS library is used to convert text labels and alerts into speech. This results in the text being read aloud with the words selected by the user.
Speech Recognition:Use the Vosk engine for real-time speech recognition. When users give input by speaking, this is transcribed as text and signed into the response form.
Multilingual Support:This project supports multiple languages ​​using Googletrans to translate domain names and make user-selected words. This supports easy access, especially for non-English speaking users.

5. Data Management
This system has a database system that stores user information, allows data analysis, and records data in real time,
Unique User Identification:Each user is identified by the unique key such as the last four digits of the Aadhaar number.This key is used to store and preserve data securely.
Data Correction and Validation:After returning to the form, the user can retrieve previously saved data using their unique key. The system automatically corrects typos and prompts users to re-enter missing or incorrect information.

6. User Interface Design
user interface is designed to be simple,allowing users with minimal experience to easily navigate the system.The main homepage has two large buttons for users to select a text or navigation. Both types guide users step-by-step through the process they choose. 

7. PDF Management
This project uses PyPDF2 to manage document templates. The system reads the pre-designed PDF and dynamically adds information to the appropriate fields based on user input. The final completed form will be saved with a unique identifier for easy tracking.



# Result 

Home page 
![Screenshot (188)](https://github.com/user-attachments/assets/977157e9-4008-454e-8236-7b94ccf3efa2)

selection page
![Screenshot (189)](https://github.com/user-attachments/assets/79bc44cb-f83d-4ee6-af5e-1322924f79ff)

Form page
![Screenshot 2024-11-21 163911](https://github.com/user-attachments/assets/1f3715c1-f2be-4ff1-bc78-de9fa30f8cb8)

guidance page
![Screenshot 2024-11-21 164014](https://github.com/user-attachments/assets/94c46ba8-f556-4e00-8545-dbace9b0aa27)






