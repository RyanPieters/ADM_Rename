from tika import parser
import re
import os

directory = r'C:\Users\klein\Documents\My Web Sites\PyProjects\PdfRename_ADM'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdf_Name = filename
        raw_data = parser.from_file(pdf_Name)

        raw_data_trimmed = re.sub('\s+', '', raw_data['content'])

        #print(raw_data_trimmed)

        idHit = raw_data_trimmed.find('eidentificatoconcodiceADM:')
        idEnd = raw_data_trimmed[idHit:].find('Presentata') - 26

        id = raw_data_trimmed[idHit+26:idHit+idEnd+26]

        os.rename(filename, id + '.pdf')


