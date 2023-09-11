import lxml.etree
import lxml.builder
import xlrd

# 1-ый STUD
stud_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/stud.xls")
stud_sh = stud_wb.sheet_by_index(0)
stud_tags = [n.replace(" ", "").lower() for n in stud_sh.row_values(0)]

stud_XLS = []
for row in range(1, stud_sh.nrows):
    stud_XLS.append(stud_sh.row_values(row))

# 2-ой APPOI
appoi_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/appoi.xls")
appoi_sh = appoi_wb.sheet_by_index(0)
appoi_tags = [n.replace(" ", "").lower() for n in appoi_sh.row_values(0)]

appoi_XLS = []
for row in range(1, appoi_sh.nrows):
    appoi_XLS.append(appoi_sh.row_values(row))

# 3-ий ADRESS1
addres1_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/addres1.xls")
addres1_sh = addres1_wb.sheet_by_index(0)
addres1_tags = [n.replace(" ", "").lower() for n in addres1_sh.row_values(0)]

addres1_XLS = []
for row in range(1, addres1_sh.nrows):
    addres1_XLS.append(addres1_sh.row_values(row))

# 4-ый ADRESS2
addres2_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/addres2.xls")
addres2_sh = addres2_wb.sheet_by_index(0)
addres2_tags = [n.replace(" ", "").lower() for n in addres2_sh.row_values(0)]

addres2_XLS = []
for row in range(1, addres2_sh.nrows):
    addres2_XLS.append(addres2_sh.row_values(row))

# 5-ый DOC1
doc1_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/doc1.xls")
doc1_sh = doc1_wb.sheet_by_index(0)
doc1_tags = [n.replace(" ", "").lower() for n in doc1_sh.row_values(0)]

doc1_XLS = []
for row in range(1, doc1_sh.nrows):
    doc1_XLS.append(doc1_sh.row_values(row))

# 6-ой DOC2
doc2_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/doc2.xls")
doc2_sh = doc2_wb.sheet_by_index(0)
doc2_tags = [n.replace(" ", "").lower() for n in doc2_sh.row_values(0)]

doc2_XLS = []
for row in range(1, doc2_sh.nrows):
    doc2_XLS.append(doc2_sh.row_values(row))

# 7-ой COMMUN1
commun1_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/commun1.xls")
commun1_sh = commun1_wb.sheet_by_index(0)
commun1_tags = [n.replace(" ", "").lower() for n in commun1_sh.row_values(0)]

commun1_XLS = []
for row in range(1, commun1_sh.nrows):
    commun1_XLS.append(commun1_sh.row_values(row))

# 8-ой COMMUN2
commun2_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/commun2.xls")
commun2_sh = commun2_wb.sheet_by_index(0)
commun2_tags = [n.replace(" ", "").lower() for n in commun2_sh.row_values(0)]

commun2_XLS = []
for row in range(1, commun2_sh.nrows):
    commun2_XLS.append(commun2_sh.row_values(row))

# 9-ый EDU_P
edu_p_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/edu_p.xls")
edu_p_sh = edu_p_wb.sheet_by_index(0)
edu_p_tags = [n.replace(" ", "").lower() for n in edu_p_sh.row_values(0)]

edu_p_XLS = []
for row in range(1, edu_p_sh.nrows):
    edu_p_XLS.append(edu_p_sh.row_values(row))

# 10-ый EDUC
educ_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/educ.xls")
educ_sh = educ_wb.sheet_by_index(0)
educ_tags = [n.replace(" ", "").lower() for n in educ_sh.row_values(0)]

educ_XLS = []
for row in range(1, educ_sh.nrows):
    educ_XLS.append(educ_sh.row_values(row))

# 11-ый PERS1
pers1_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/pers1.xls")
pers1_sh = pers1_wb.sheet_by_index(0)
pers1_tags = [n.replace(" ", "").lower() for n in pers1_sh.row_values(0)]

pers1_XLS = []
for row in range(1, pers1_sh.nrows):
    pers1_XLS.append(pers1_sh.row_values(row))

# 12-ый PERS2
pers2_wb = xlrd.open_workbook(
    "C:/Users/Mosyagin/Desktop/ssStudy/сводка данных по группам/pers2.xls")
pers2_sh = pers2_wb.sheet_by_index(0)
pers2_tags = [n.replace(" ", "").lower() for n in pers2_sh.row_values(0)]

pers2_XLS = []
for row in range(1, pers2_sh.nrows):
    pers2_XLS.append(pers2_sh.row_values(row))


ALL_TAGS = [len(appoi_tags), len(stud_tags), len(addres1_tags),
            len(addres2_tags), len(doc1_tags), len(doc2_tags),
            len(commun1_tags), len(commun2_tags), len(edu_p_tags),
            len(educ_tags), len(pers1_tags), len(pers2_tags),]


def func_creating_students():
    for j in range(36):
        STUDY = {'stud': {}, 'appoi': {}, 'addres1': {}, 'addres2': {}, 'doc1': {}, 'doc2': {}, 'commun1': {},
                 'commun2': {}, 'educ': {}, 'edu_p': {}, 'pers1': {},
                 'pers2': {}, }

        for l in range(30):
            if len(stud_tags) > l and len(stud_XLS) > j:
                STUDY['stud'][str(stud_tags[l])] = str(stud_XLS[j][l])
            if len(appoi_tags) > l and len(appoi_XLS) > j:
                STUDY['appoi'][str(appoi_tags[l])] = str(appoi_XLS[j][l])
            if len(addres1_tags) > l and len(addres1_XLS) > j:
                STUDY['addres1'][str(addres1_tags[l])] = str(addres1_XLS[j][l])
            if len(addres2_tags) > l and len(addres2_XLS) > j:
                STUDY['addres2'][str(addres2_tags[l])] = str(addres2_XLS[j][l])
            if len(doc1_tags) > l and len(doc1_XLS) > j:
                STUDY['doc1'][str(doc1_tags[l])] = str(doc1_XLS[j][l])
            if len(doc2_tags) > l and len(doc2_XLS) > j:
                STUDY['doc2'][str(doc2_tags[l])] = str(doc2_XLS[j][l])
            if len(commun1_tags) > l and len(commun1_XLS) > j:
                STUDY['commun1'][str(commun1_tags[l])] = str(commun1_XLS[j][l])
            if len(commun2_tags) > l and len(commun2_XLS) > j:
                STUDY['commun2'][str(commun2_tags[l])] = str(commun2_XLS[j][l])
            if len(edu_p_tags) > l and len(edu_p_XLS) > j:
                STUDY['edu_p'][str(edu_p_tags[l])] = str(edu_p_XLS[j][l])
            if len(educ_tags) > l and len(educ_XLS) > j:
                STUDY['educ'][str(educ_tags[l])] = str(educ_XLS[j][l])
            if len(pers1_tags) > l and len(pers1_XLS) > j:
                STUDY['pers1'][str(pers1_tags[l])] = str(pers1_XLS[j][l])
            if len(pers2_tags) > l and len(pers2_XLS) > j:
                STUDY['pers2'][str(pers2_tags[l])] = str(pers2_XLS[j][l])

            if max(ALL_TAGS) <= l:
                break
        yield STUDY
    return STUDY


# STUDY = {'stud': {}, 'appoi': {}, 'appoi2': {}, 'addres': {}, 'addres2': {},
#          'addres3': {}, 'doc': {}, 'doc2': {}, 'doc3': {}, 'commun': {},
#          'commun2': {}, 'commun3': {}, 'educ': {}, 'edu_p': {}, 'pers': {},
#          'pers2': {}, 'pers3': {}, }
