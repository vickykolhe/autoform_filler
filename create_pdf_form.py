# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.colors import black, white


# def create_pdf_form(pdf_path):
#     # Create a PDF canvas
#     c = canvas.Canvas(pdf_path, pagesize=letter)
#     width, height = letter

#     # Title
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(100, height - 50, "Sample Form")

#     # Add fields
#     fields = ["Name", "Email", "Phone Number"]

#     y_position = height - 100  # Starting position for the fields
#     for field in fields:
#         c.drawString(100, y_position, f"{field}:")
#         c.acroForm.textfield(
#             name=field,  # Ensure this is a string
#             tooltip=field,
#             x=200,
#             y=y_position - 10,
#             width=300,
#             height=20,
#             borderStyle="inset",
#             forceBorder=True,
#             textColor=black,  # Black color
#             # fillColor=white,  # White color
#         )
#         print(f"Created field: {field}")  # Debug print
#         y_position -= 40  # Move down for the next field

#     # Save the PDF
#     c.save()
#     print(f"PDF form created: {pdf_path}")


# # Create the PDF form
# create_pdf_form("Form 2.pdf")
# -------------------------------------------------------------------------------

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from reportlab.lib.colors import black


# def create_pdf_form(pdf_path):
#     # Register a font that supports Hindi
#     pdfmetrics.registerFont(
#         TTFont("Devanagari", "NotoSansDevanagari-Regular.ttf")
#     )  # Use the path to your Hindi font

#     # Create a PDF canvas
#     c = canvas.Canvas(pdf_path, pagesize=letter)
#     width, height = letter

#     # Title
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(100, height - 50, "Sample Form")

#     # Add fields with Hindi labels
#     fields = ["नाम", "ईमेल"]

#     c.setFont("Devanagari", 12)  # Use Hindi font for field labels
#     y_position = height - 100  # Starting position for the fields
#     for field in fields:
#         c.drawString(100, y_position, f"{field}:")
#         c.acroForm.textfield(
#             name=field,
#             tooltip=field,
#             x=200,
#             y=y_position - 10,
#             width=300,
#             height=20,
#             borderStyle="inset",
#             forceBorder=True,
#             textColor=black,
#         )
#         y_position -= 40  # Move down for the next field

#     # Save the PDF
#     c.save()
#     print(f"PDF form created: {pdf_path}")


# # Create the PDF form
# create_pdf_form("Form 4.pdf")


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black


def create_government_office_form(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Title of the form
    c.setFont("Helvetica-Bold", 18)
    c.drawString(130, height - 50, "Government Office Application Form")

    # Personal Details Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 100, "Personal Details")

    fields = {
        "Full Name": (50, height - 130, "text", 350, 20),
        "Father's Name": (50, height - 170, "text", 350, 20),
        "Date of Birth (DD/MM/YYYY)": (50, height - 210, "text", 200, 20),
        "Gender": (50, height - 250, "checkbox", None, None),
    }

    c.setFont("Helvetica", 12)
    for field, (x_pos, y_pos, field_type, field_width, field_height) in fields.items():
        c.drawString(x_pos, y_pos, f"{field}:")
        if field_type == "text":
            c.acroForm.textfield(
                name=field,
                tooltip=field,
                x=x_pos + 180,
                y=y_pos - 10,
                width=field_width,
                height=field_height,
                borderStyle="inset",
                forceBorder=True,
                textColor=black,
            )
        elif field_type == "checkbox":
            c.drawString(x_pos + 180, y_pos, "Male")
            c.acroForm.checkbox(
                name="Male", x=x_pos + 240, y=y_pos - 10, buttonStyle="check"
            )

            c.drawString(x_pos + 300, y_pos, "Female")
            c.acroForm.checkbox(
                name="Female", x=x_pos + 360, y=y_pos - 10, buttonStyle="check"
            )

    # Address Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 290, "Address Details")

    address_fields = {
        "House No.": (50, height - 320, "text", 150, 20),
        "Street/Locality": (50, height - 360, "text", 350, 20),
        "City": (50, height - 400, "text", 200, 20),
        "State": (50, height - 440, "text", 200, 20),
        "Postal Code": (50, height - 480, "text", 100, 20),
    }

    c.setFont("Helvetica", 12)
    for field, (
        x_pos,
        y_pos,
        field_type,
        field_width,
        field_height,
    ) in address_fields.items():
        c.drawString(x_pos, y_pos, f"{field}:")
        c.acroForm.textfield(
            name=field,
            tooltip=field,
            x=x_pos + 180,
            y=y_pos - 10,
            width=field_width,
            height=field_height,
            borderStyle="inset",
            forceBorder=True,
            textColor=black,
        )

    # Declaration Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 520, "Declaration")
    c.setFont("Helvetica", 12)
    c.drawString(
        50,
        height - 550,
        "I hereby declare that the information provided is true and correct to the best of my knowledge.",
    )
    c.drawString(
        50,
        height - 580,
        "Signature: ____________________________  Date: _______________",
    )

    # Save the PDF
    c.save()
    print(f"Government Office Application Form created: {pdf_path}")


# Create the Government Office form
create_government_office_form("Form 5.pdf")
