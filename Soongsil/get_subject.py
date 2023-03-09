# %%
from tabula import read_pdf
import pandas as pd
tables=read_pdf("Untitled.pdf")

# %%
subjects=pd.concat(tables)

# %%
subjects.head()

# %%
subjects.columns

# %%
subjects=subjects.drop(columns=["과  목  명",'교과목코드','비고'])
subjects=subjects.fillna("")

# %%
category=[]
current=""
for i in subjects['이수구분'].to_list():
    if i !='':
        current=i
    category.append('전공' if '전공' in current else '교양기타')

# %%
years=[]
semesters=[]
for i in subjects['이수시기'].to_list():
    yaer,semester=i.split()
    years.append(yaer)
    if not semester.isdigit():
        semesters.append(semester+"계절")
    else:
        semesters.append(semester)

# %%
retake=[]
for i in subjects['과목정보'].to_list():
    if 'Re' in i:
        retake.append('Y')
    else:
        retake.append('N')

# %%
subjects['이수구분']=category
subjects['수강연도']=years
subjects['학기']=semesters
subjects['재수강여부']=retake

# %%
majors=[]
for i in subjects['수강연도'].to_list():
    majors.append("소프트웨어학(숭실대-학사-주전공)")

# %%
grades=[]
for i in subjects['등급'].to_list():
    
    if '0' in i:
        grades.append(i[0])
    elif i=='P':
        grades.append('PASS')
    elif i=='F':
        grades.append('FAIL')
    else:
        grades.append(i)

# %%
subjects['전공명']=majors
subjects['등급']=grades

# %%
subjects=subjects.drop(columns=["과목정보",'이수시기','점수'])

# %%
subjects=subjects.rename(columns={'Unnamed: 0':'과목명','이수구분':'과목유형','학점':'취득학점','등급':'성적'})

# %%
subjects=subjects[['전공명','수강연도'	,'학기',	'과목명',	'과목유형',	'취득학점',	'성적',	'재수강여부']]

# %%
subjects.head()

# %%
# NO	전공명	수강연도	학기	과목명	과목유형	취득학점	성적	재수강여부

# %%
subjects

# %%
subjects.to_excel("이수교과목.xlsx")

# %%



