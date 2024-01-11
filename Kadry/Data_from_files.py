import xml.etree.ElementTree as ET
import os
import datetime

def last_data_kk(l):
    l2 = []
    last_date = ''
    for i in l:
        l2.append(datetime.datetime.strptime(i, '%d.%m.%Y').date())
        last_date = str(max(l2))
    return last_date[8:] + '.' + last_date[5:7] + '.' + last_date[:4]

path = 'F:/my_projects/Kadry/files'
for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as f:
        parser  = ET.XMLParser(encoding='UTF-8')
        tree = ET.parse(f'{path}/{filename}')
        root = tree.getroot()

# ФИО
        for tag in root.findall('CADRE_FIO'):
            if tag.find('ISACTIVE').text == '1':
                f_name = tag.find('SURNAME').text
                i_name = tag.find('NAME57').text
                o_name = tag.find('PATRON').text
            #else:
                #fold_name = tag.find('SURNAME').text



# Квалификационный класс

        dt = []
        max_dt = ''
        for tag in root.findall('CADRE_QUALIFIERCLASS/CLASS_DATE'):
            dt.append(tag.text)
        if len(dt) == 0:
            data_of_cclass = 'Квалификационный класс еще не присвоен'
        else:
            data_of_cclass = last_data_kk(dt)
            class_name = ''
            for tag in root.findall('CADRE_QUALIFIERCLASS'):
                if tag.find('CLASS_DATE').text == data_of_cclass:
                    class_name_code = tag.find('ISN_QUALIFIERCLASS_CL').text
            for tag in root.findall('CADRE_QUALIFIERCLASS_CL'):
                if tag.find('ISN_NODE131').text == class_name_code:
                    class_name = tag.find('CLASSIF_NAME131').text



        print(f'{f_name} {i_name} {o_name}')
        #print(f'({fold_name})')
        print(f'Дата присвоения квалификационного класса: {data_of_cclass}')
        #print(class_name_code)
        print(class_name)
        print()


