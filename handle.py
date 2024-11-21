import pdfrw


def read_pdf_fields(pdf_path):
    """Reads the fields from the given PDF form and returns a list of field names."""
    template = pdfrw.PdfReader(pdf_path)
    fields = template.pages[0]["/Annots"]
    field_names = []
    for field in fields:
        field_name = field.get("/T")
        if field_name:
            field_names.append(field_name[1:-1])  # Clean up field name
    return field_names


def fill_pdf_form(template_path, data, output_path):
    """Fills the PDF form fields with the provided data and saves it."""
    template = pdfrw.PdfReader(template_path)
    for page in template.pages:
        for field in page["/Annots"]:
            field_name = field.get("/T")[1:-1]  # Clean up field name
            if field_name in data:
                field.update(pdfrw.PdfDict(V="{}".format(data[field_name])))
    pdfrw.PdfWriter().write(output_path, template)
