import PyPDF3

pdf_path = 'pdf/Formulario_vacio.pdf'

# Abre el PDF en modo lectura
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    form_fields = pdf_reader.getFields()
    for field_name in form_fields:
        print(f'Campo de formulario: {field_name}')

# Output: Lista de nombres de los campos de formulario
