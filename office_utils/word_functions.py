from ezodf import opendoc, newdoc, Sheet

values = (
    ('Col1', 'Col2', 'Col3', 'Col4'),
    ('12', '23', '34', '45')
)


def create_sheet(data):
    sheet = Sheet('Sheet1', size=(len(data), len(data[0])))
    fill_table(sheet, data)
    return sheet


def fill_table(sheet, result):
    for i in range(len(result)):
        for j in range(len(result[0])):
            sheet[i, j].set_value(result[i][j])


def create_document(file_name, data, template_path='templates/template1.odt'):
    doc = newdoc(doctype='odt', filename=file_name, template=template_path)

    sheet = create_sheet(data)
    doc.body.append(sheet)
    doc.save()
