# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas


# def generate_pdf(form_name, form_data, user_name):
#     # Create a sanitized filename
#     sanitized_name = user_name.replace(" ", "_")  # Replace spaces with underscores
#     pdf_filename = f"{form_name.replace(' ', '_')}_{sanitized_name}.pdf"

#     c = canvas.Canvas(pdf_filename, pagesize=letter)
#     width, height = letter

#     # Title
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(100, height - 50, f"Form: {form_name}")

#     # Adding fields with specific formatting
#     y_position = height - 100  # Start below the title
#     line_spacing = 20  # Space between lines

#     c.setFont("Helvetica", 12)
#     for field, value in form_data.items():
#         c.drawString(50, y_position, f"{field}: {value}")
#         y_position -= line_spacing  # Move down for the next field

#     c.save()
#     print(f"PDF generated for {form_name} with user name: {user_name}")
