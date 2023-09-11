from lxml import etree
from shubl_lxml import tree, root, appointments, addresses, documents, communications, education, edu_programm, person_links
import spStudy
from spStudy import func_creating_students

page = etree.Element("students")
docs = etree.ElementTree(page)

lst = [root, appointments, addresses, documents,
       communications, education, edu_programm, person_links]


def append_array_stud2(parent_el, data):
    dictionaty_study = spStudy.func_creating_students()
    count = 0

    for diction in dictionaty_study:
        stud = etree.SubElement(parent_el, "student")
        appoi = etree.SubElement(stud, "appointments")
        appoi2 = etree.SubElement(appoi, "appointment")
        addres = etree.SubElement(stud, "addresses")
        addres2 = etree.SubElement(addres, "address")
        addres3 = etree.SubElement(addres, "address")
        doc = etree.SubElement(stud, "documents")
        doc2 = etree.SubElement(doc, "document")
        doc3 = etree.SubElement(doc, "document")
        commun = etree.SubElement(stud, "communications")
        commun2 = etree.SubElement(commun, "communic")
        commun3 = etree.SubElement(commun, "communic")
        educ = etree.SubElement(stud, "education")
        edu_p = etree.SubElement(stud, "edu_programm")
        pers = etree.SubElement(stud, "person_links")
        pers2 = etree.SubElement(pers, "psn_link")
        pers3 = etree.SubElement(pers, "psn_link")
        for k, v in diction.items():
            for k1, v1 in v.items():
                if count == 0:
                    stud.set(k1, v1)
                elif count == 1:
                    appoi2.set(k1, v1)

                elif count == 2:
                    addres2.set(k1, v1)
                elif count == 3:
                    addres3.set(k1, v1)

                elif count == 4:
                    doc2.set(k1, v1)
                elif count == 5:
                    doc3.set(k1, v1)

                elif count == 6:
                    commun2.set(k1, v1)
                elif count == 7:
                    commun3.set(k1, v1)

                elif count == 8:
                    educ.set(k1, v1)
                elif count == 9:
                    edu_p.set(k1, v1)

                elif count == 10:
                    pers2.set(k1, v1)
                elif count == 11:
                    pers3.set(k1, v1)
            count += 1
        count = 0


for i in range(1):
    append_array_stud2(page, lst)

docs.write("file2.xml")

# def append_array_stud(parent_el, data):
#     # parent_el = root
#     # arrayNumber = etree.SubElement(parent_el, "student")
#     # stud = etree.SubElement(parent_el, "student")
#     # appoi = etree.SubElement(stud, "appointments")
#     # appoi2 = etree.SubElement(appoi, "appointment")
#     # addres = etree.SubElement(stud, "addresses")
#     # addres2 = etree.SubElement(addres, "address")
#     # doc = etree.SubElement(stud, "documents")
#     # doc2 = etree.SubElement(doc, "document")
#     # commun = etree.SubElement(stud, "communications")
#     # commun2 = etree.SubElement(commun, "communic")
#     # educ = etree.SubElement(stud, "education")
#     # edu_p = etree.SubElement(educ, "edu_programm")
#     # pers = etree.SubElement(stud, "person_links")
#     # pers2 = etree.SubElement(pers, "psn_link")
#     count = 0
#     stud = etree.SubElement(parent_el, "student")
#     appoi = etree.SubElement(stud, "appointments")
#     appoi2 = etree.SubElement(appoi, "appointment")
#     addres = etree.SubElement(stud, "addresses")
#     addres2 = etree.SubElement(addres, "address")
#     addres3 = etree.SubElement(addres, "address")
#     doc = etree.SubElement(stud, "documents")
#     doc2 = etree.SubElement(doc, "document")
#     doc3 = etree.SubElement(doc, "document")
#     commun = etree.SubElement(stud, "communications")
#     commun2 = etree.SubElement(commun, "communic")
#     commun3 = etree.SubElement(commun, "communic")
#     educ = etree.SubElement(stud, "education")
#     edu_p = etree.SubElement(stud, "edu_programm")
#     pers = etree.SubElement(stud, "person_links")
#     pers2 = etree.SubElement(pers, "psn_link")
#     pers3 = etree.SubElement(pers, "psn_link")
#     q = 0
#     for datas in data:

#         if len(datas.items()) > 1:
#             dictionary = {datas1: datas2 for datas1, datas2 in datas.items()}
#             for ds in dictionary:
#                 if q == 0:
#                     educ.set(ds, dictionary[ds])
#                 else:
#                     edu_p.set(ds, dictionary[ds])
#             q += 1

#         for i in datas:
#             dictionary2 = {i1: i2 for i1, i2 in i.items()}
#             # print(dictionary)
#             for s1 in dictionary2:
#                 if count == 0:
#                     stud.set(s1, dictionary2[s1])
#                 elif count == 1:
#                     appoi2.set(s1, dictionary2[s1])

#                 elif count == 2:
#                     addres2.set(s1, dictionary2[s1])
#                 elif count == 3:
#                     addres3.set(s1, dictionary2[s1])

#                 elif count == 4:
#                     doc2.set(s1, dictionary2[s1])
#                 elif count == 5:
#                     doc3.set(s1, dictionary2[s1])

#                 elif count == 6:
#                     commun2.set(s1, dictionary2[s1])
#                 elif count == 7:
#                     commun3.set(s1, dictionary2[s1])

#                 elif count == 8:
#                     pers2.set(s1, dictionary2[s1])
#                 elif count == 9:
#                     pers3.set(s1, dictionary2[s1])
#             count += 1
