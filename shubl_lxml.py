from lxml import etree as ET

root = ET.Element('students')
student = ET.SubElement(root, 'student', tab_nmb="000001", fio="Иванов Иван Иванович", born_date="01.01.2000", born_addr="г. Москва", sex="М", gr="РФ", app_date="01.09.2021", language="Английский язык",
                        lname="Иванов", fname="Иван", mname="Иванович", lname_lt="Ivanov", fname_lt="Ivan", mname_lt="Ivanovich", abit_info="Общий конкурс", invalid_group="", soc_status_name="", localiz="", ext_stud_id="123456")
appointments = ET.SubElement(student, 'appointments')
# main.text = 'Thanks for contributing an answer to Stack Overflow!'
appointment = ET.SubElement(appointments, 'appointment', order_nmb="21001", order_date="18.08.2021", order_text="Зачисление студентов", order_prim="Зачислить на первый курс",
                            appoint_date="01.09.2021", dismiss_date="", fin="Бюджет", order_rpd="30001", decanat="Фкультет ВШУ", gnumber="2103001", course="1")

# level2 = ET.SubElement(second, 'Token', word=u"low")
addresses = ET.SubElement(student, 'addresses')
address = ET.SubElement(addresses, 'address', obj_type=u"3", full_addr=u"С.Казьминское Кочубеевского р-на Ставропольского края", country=u"",
                        zip=u"", region=u"", area=u"", city=u"", place=u"", street=u"", house=u"", corpus=u"", flat=u"", dreg_beg=u"", dreg_end=u"")
address2 = ET.SubElement(addresses, 'address', obj_type=u"4", full_addr=u"С.Казьминское Кочубеевского р-на Ставропольского края", country=u"",
                         zip=u"", region=u"", area=u"", city=u"", place=u"", street=u"", house=u"", corpus=u"", flat=u"", dreg_beg=u"", dreg_end=u"")

documents = ET.SubElement(student, 'documents')
document = ET.SubElement(documents, 'document', sys_code="502", kind="21", doc_name="Паспорт РФ", doc_series="0101", doc_number="123456",
                         given_date="01.01.2019", given_by="ГУ МВД России по г. Москве", given_podr="770-012", to_date="", doc_osn="1")
document2 = ET.SubElement(documents, 'document', sys_code="501", kind="102", doc_name="СНИЛС", doc_series="",
                          doc_number="000-000-000 00", given_date="", given_by="", given_podr="", to_date="", doc_osn="")

communications = ET.SubElement(student, 'communications')
communic = ET.SubElement(communications, 'communic',
                         comm_type="тел.сот.", communic="+7 911-123-45-67")
communic2 = ET.SubElement(communications, 'communic',
                          comm_type="e-mail", communic="name@mailhost.com")

education = ET.SubElement(student, 'education', edu_level="Среднее (полное) общее", edu_form="", doc_type="104", doc_ser="", doc_nmb="000123456", doc_date="01.07.2021",
                          org_name="МБОУ СОШ №30 г. Химки Московской области", org_type="СОШ", org_country="Россия", org_region="Московская область", org_city="Химки г")

edu_programm = ET.SubElement(student, 'edu_programm', ext_id="", year_ent="2021", edu_level="бакалавр", edu_form="0", faculty_code="14",
                             faculty_name="Институт сокращенных программ", spec_code="38.03.01", spec_name="Экономика", specz="Учёт, анализ и аудит")

person_links = ET.SubElement(student, 'person_links')
psn_link = ET.SubElement(person_links, 'psn_link', link_type="мать", fio="Иванова Татьяна Ивановна", born_date="01.01.1975", address="РОССИЯ, Московская обл, Мытищи г, Ленина ул, 160 д, 15 кв", doc_name="Паспорт РФ", doc_ser="0101",
                         doc_nmb="654987", given_date="01.01.2018", given_by="ГУ МВД по г.Москве", given_podr="770-012", inn="12345678911", snils="000-000-000 00", phone="+7 911 123-12-23", work_plase="ПАО Сбербанк", work_post="директор отделения")
psn_link2 = ET.SubElement(person_links, 'psn_link', link_type="отец", fio="Иванов Иван Иванович", born_date="01.01.1976", address="РОССИЯ, Московская обл, Мытищи г, Ленина ул, 160 д, 15 кв", doc_name="Паспорт РФ", doc_ser="0101",
                          doc_nmb="654978", given_date="01.01.2018", given_by="ГУ МВД по г.Москве", given_podr="770-012", inn="12345678922", snils="000-000-000 00", phone="+7 911 123-12-32", work_plase="ПАО Сбербанк", work_post="начальник трнспортного цеха")


tree = ET.ElementTree(root)
tree.write('output.xml', pretty_print=True,
           xml_declaration=True,   encoding="utf-8")
