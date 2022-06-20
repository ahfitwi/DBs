#******************************************************************************
### 0.1 Columns
#******************************************************************************
# All Course List Columns
allCourses_columns = ['course_name', 'acronym', 'cost_model']
    # Registrants columns: two are missing (Education Level and Country)
registrant_columns1 = ['First Name:','Last Name:','Email Address:','Address 1:',
                          'City:','State:', 'Education Level:', 'Country:',
                          'ZIP Code:', 'Phone:','Company/School:', 'Job Title:',
                          'Department:', 'How did you hear about this course?',
                          'Registration Date', 'Registration Status',
                          'Payment Status','Payment Type','Fee Type',
                          'Promo Code', 'Code Type', 'Discount Percent',
                          'Discount Amount', 'Total Price']
registrant_columns = ['course_id','course_abb','mmyyyy','course_type',
                      'First Name:','Last Name:','Email Address:','Address 1:',
                      'City:','State:', 'Education Level:', 'Country:',
                      'ZIP Code:','Phone:','Company/School:', 'Job Title:',
                      'Department:','How did you hear about this course?',
                      'Registration Date','Registration Status',
                      'Payment Status','Payment Type','Fee Type', 'Promo Code',
                      'Code Type', 'Discount Percent','Discount Amount',
                      'Total Price']
#Grade columns
grade_columns1 =['Last Name', 'First Name', 'Username',
                     'Student ID','Last Access', 'Availability', 'Final Exam']
grade_columns = ['course_id','course_abb','mmyyyy','course_type','Last Name',
                 'First Name', 'Username', 'Student ID','Last Access',
                 'Availability', 'Final Exam', 'Final Grade']

# Cost-model
cost_columns1 = ['Name', 'Role', 'Pay', 'Type', 'Location']
cost_columns = ['course_id','course_abb','mmyyyy','course_type','Name','Role',
                'Pay','Type','Location']
# Survey
sur_columns1 = ['course_id','course_type','questions','opinion','count']
sur_columns = ['course_id','course_abb','mmyyyy','course_type','questions',
               'opinion','scores','count']

# Others
bunbu_columns = ['course_id','course_type','Fee Type']
city_columns = ['course_id','course_type','City:']
state_columns = ['course_id','course_type','State:']
dept_columns = ['course_id','course_type','Department:']
jt_columns = ['course_id','course_type','job_title']
demog_columns = ['course_id', 'course_abb','mmyyyy', 'course_type', 'object',
                 'by', 'count']

profit_columns = ['course_id', 'course_abb', 'mmyyyy', 'course_type', 'Name',
                  'Role', 'Pay', 'Type',
                  'Location','Amount']
psmry_col = ['course_id', 'course_abb','mmyyyy','total_income', 'total_cost',
             'profit', '%profit']
type_col =['Total Income','Total Direct Expense','State Fringeable sum',
           'RF Overhead 25%','State Fringe',
           'Total Invoiced Direct Expenses',
           'Credit Card (Paypal) fees 3','Total Costs', 'Profit']

sort_dict = {'Total Income': 'A',
             'percent': 'B',
             'actual': 'C',
             'Total Direct Expense': 'D',
             'State Fringeable sum': 'E',
             'RF Overhead 25%': 'F',
             'State Fringe': 'G',
             'Total Invoiced Direct Expenses': 'H',
             'Credit Card (Paypal) fees 3': 'I',
             'Total Costs': 'J',
             'Profit': 'K',
             'Profit%': 'L'}
sort_dict2 = {'Total Income': 'A',
             'Total Direct Expense': 'B',
             'State Fringeable sum': 'C',
             'RF Overhead 25%': 'D',
             'State Fringe': 'E',
             'Total Invoiced Direct Expenses': 'F',
             'Credit Card (Paypal) fees 3': 'G',
             'Total Costs': 'H',
             'Profit': 'I'}

# For the survey data analysis
suvy1_cols1 = ['Timestamp',
 "Participant's Name (Optional)",
 'Contribution to learning [Level of skill/knowledge at start of course]',
 'Contribution to learning [Level of skill/knowledge at end of course]',
 'Contribution to learning [Level of skill/knowledge required to'+
               ' complete the course]',
 'Contribution to learning [Contribution of course to your skill/knowledge]',
 'Skill and responsiveness of the instructors [Instructor  an effective'+
               ' lecturer/demonstrator]',
 'Skill and responsiveness of the instructors [Presentations were clear'
               ' and organized]',
 'Skill and responsiveness of the instructors [Instructor stimulated' +
               ' student interest]',
 'Skill and responsiveness of the instructors [Instructor effectively'+
               ' used time during class periods]',
 'Course content [Learning objectives were clear]',
 'Course content [Course content was organized and well planned]',
 'Course content [Course workload was appropriate]',
 'Course content [Course organized to allow all students to participate fully]',
 'Course content [Hands-on activities aided in your learning]',
 'What aspects of this course were most useful or valuable?',
 'How would you improve this course?',
 'Intention to apply your new knowledge',
 'Satisfaction of Registration/Payment Process [Registration process]',
 'Satisfaction of Registration/Payment Process [Payment process]',
 'Overall Course Satisfaction',
 'Your Likelihood to Recommend this course?',
 'Why or Why Not?']

c_new=['1.1 Level of skill/knowledge at start of course',
       '1.2 Level of skill/knowledge at end of course',
       '1.3 Level of skill/knowledge required to complete the course',
       '1.4 Contribution of course to your skill/knowledge',
       '2.1 Instructor  an effective lecturer/demonstrator',
       '2.2 Presentations were clear and organized',
       '2.3 Instructor stimulated student interest',
       '2.4 Instructor effectively used time during class periods',
       '3.1 Learning objectives were clear',
       '3.2 Course content was organized and well planned',
       '3.3 Course workload was appropriate',
       '3.4 Course organized to allow all students to participate fully',
       '3.5 Hands-on activities aided in your learning',
       '7.1 Registration process',
       '7.2 Payment process',
       '8.1 Overall Course Satisfaction',
       '9.1 Your Likelihood to Recommend this Course?',
       'Keys to Survey Questions 1 through 9.']

colcon =['Contribution to learning',
         'Skill and responsiveness of the instructors',
         'Course content',
         'What aspects of this course were most useful or valuable?',
         'How would you improve this course?',
         'Intention to apply your new knowledge',
         'Satisfaction of Registration',
         'Overall Course Satisfaction',
         'Your Likelihood to Recommend this course?',
         'Why or Why Not?'
        ]

colcon1 = ['Contribution To Learning','Skill and Responsiveness',
           'Course Content', 'Most Useful Aspects',
           'How To Improve This Course', 'Apply New Knowledge',
           'Satisfaction Registration','Overall Course Satisfaction',
           'Likelihood to Recommend','Whyor Why Not']


c1_new =['Level of skill/knowledge at start of course',
         'Level of skill/knowledge at end of course',
         'Level of skill/knowledge required to complete the course',
         'Contribution of course to your skill/knowledge']

c2_new = ['Instructor  an effective lecturer/demonstrator',
          'Presentations were clear and organized',
          'Instructor stimulated student interest',
          'Instructor effectively used time during class periods']
c3_new = ['Learning objectives were clear',
          'Course content was organized and well planned',
          'Course workload was appropriate',
          'Course organized to allow all students to participate fully',
          'Hands-on activities aided in your learning']
c4_new = ['What aspects of this course were most useful or valuable?']
c5_new = ['How would you improve this course?']
c6_new = ['Intention to apply your new knowledge']
c7_new = ['Registration process',
          'Payment process']
c8_new = ['Overall Course Satisfaction']
c9_new = ['Your Likelihood to Recommend this course?']

remarks ={'Excellent':[5], 'Very good':[4], 'Satisfactory':[3],
          'Fair':[2],'Limited':[1],'Strongly disagree':[1],
          'Disagree':[2], 'Neutral':[3], 'Agree':[4], 'Strongly agree':[5],
          'Very Dissatisfied':[1], 'Dissatisfied':[2],
          'Neutral':[3], 'Satisfied':[4], 'Very Satisfied':[5]}

keysvy = ['Excellent', 'Very good', 'Satisfactory', 'Fair', 'Limited',
          'Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree',
           'Very Dissatisfied', 'Dissatisfied', 'Neutral','Satisfied',
           'Very Satisfied']

dest_cols = ['percentage_name','Short_name','update_percent']

cklst_col = ['course_id', 'year']

colhdh=['course_id','course_abb','mmyyyy','How did you hear about this course?']
colhdh2=['Courses','Start Date','How did you hear about this course?','count']
colregin=['Courses','Start Date','Month/Year','Enrollees', 'Income','Notes']


#******************************************************************************
# This is A replace module
#******************************************************************************
### Packages and Libraries
#******************************************************************************
from datetime import datetime as dtt
from datetime import date
import pandas as pd
import numpy as np
import os, sys, glob
import sqlite3
from sqlalchemy import create_engine

#Linux OS
#cpath="/home/alem/Desktop/alemprojects/SummerProject/0_finalJan22_2021/DashProject02June20/"
#path_9 = os.path.join(cpath,"DatasetsAndReprots/Replace/")
#path_5 = os.path.join(cpath,"DatasetsAndReprots/All_Datasets/")

#Windows
cpath="D:\\DashProject02June20\\"
path_9 = os.path.join(cpath,"DatasetsAndReprots\\Replace\\")
path_5 = os.path.join(cpath,"DatasetsAndReprots\\All_Datasets\\")
dbpath = 'D:\\DashProject02June20\\PythonAndSqlite\\py_and_db\\DashProjDB.db'
#******************************************************************************
### Read an Excel file from replace folder
                   # dfall, dfreg,demog,dfcos,dfgra,dfsur1, dfset
#******************************************************************************
def extrat_id(fn, prefix):
    #path_9 = set_path(cpath)
    #idd = re.sub(path_1, '', fn)
    idd = fn.replace(path_9, '')
    idd = idd.replace(prefix,'')
    idd = idd.replace('.xlsx','')
    if 'pu_' in idd:
        return idd.replace('pu_',''), 'public'
    else:
        return idd.replace('pr_',''), 'private'

def get_filenames(filenames):
    fnall= '';
    fnregistrants =''; idreg = '';
    fngrades = ''; idgra = '';
    fncosts = ''; idcos = '';
    fnevals = ''; ideva = '';

    for fn in filenames:
        if 'all_' in fn:
            fnall = fn
        elif 'registrants_' in fn:
            fnregistrants = fn
            idreg = extrat_id(fn, 'registrants_')
        elif 'grades_' in fn:
            fngrades = fn
            idgra = extrat_id(fn, 'grades_')
        elif 'costs_' in fn:
            fncosts = fn
            idcos = extrat_id(fn, 'costs_')
        elif 'eval_' in fn:
            fnevals = fn
            ideva = extrat_id(fn, 'eval_')
    final_names=[fnall, fnregistrants, fngrades, fncosts, fnevals]
    ids = [idreg, idgra, idcos, ideva]
    return final_names, ids

def read_input_files(path):
    try:
        df = pd.read_excel(path)
    except:
        flag = False
        return flag
    else:
        return df

#*************************************
def read_dsets():
    #path_9 = set_path(cpath)
    statusc = []
    filenames, ids =get_filenames(glob.glob(path_9+"*.xlsx"))
    dfall = read_input_files(filenames[0])
    if isinstance(dfall, bool)==False:
        try:
            dfall = dfall[allCourses_columns]
        except:
            statusc.append('All_course_list has columns mismatch problem!')
    dfreg = read_input_files(filenames[1])
    if isinstance(dfreg, bool)==False:
        try:
            dfreg = dfreg[registrant_columns1]
        except:
            statusc.append('Registrants file has columns mismatch problem!')
    dfgra = read_input_files(filenames[2])
    if isinstance(dfgra, bool)==False:
        try:
            dfgra = dfgra[grade_columns1]
        except:
            statusc.append('Grades file has columns mismatch problem!')

    dfcos = read_input_files(filenames[3])
    if isinstance(dfcos, bool)==False:
        try:
            dfcos = dfcos[cost_columns1]
        except:
            statusc.append('Costs file has columns mismatch problem!')
    dfsur = read_input_files(filenames[4])
    if isinstance(dfsur, bool)==False:
        try:
            dfsur.columns = suvy1_cols1
        except:
            statusc.append('Surveys file has columns mismatch problem!')
    return filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, statusc
#%%%
#filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, statusc = read_dsets()
#******************************************************************************
### Write all datasets to
#******************************************************************************
def write_dsets(df, col, filename, msg):
    wmsg = []
    #path_9 = set_path(cpath)
    if  isinstance(df, bool)==False:
        if set(col).issubset(set(list(df.columns))):
            dfw = df[col]
            #dfw.to_excel(path_5+re.sub(path_1, '', filename),index=False)
            dfw.to_excel(path_5+filename.replace(path_9, ''),index=False)

        else:
            var="Replace (write_dsets()): Error! Columns mismatch in "+msg+"!"
            wmsg.append(var)

    else:
        var = "Replace (write_dsets()): No " + msg + " to write to"+\
               " All_Datasets Folder!"
        wmsg.append(var)
    return wmsg
#%%%
#call_writer(dfall, dfreg, dfgra, dfcos, dfsur, filenames)
#******************************************************************************
### Write all datasets to
#******************************************************************************
def remove_inputfiles():
    #path_9 = set_path(cpath)
    rmsg = []
    try:
        files = glob.glob(path_9+'*.xlsx')
        for f in files:
            os.remove(f)
    except:
        rmsg.append("Replace (remove_inputfiles): No files to remove!")
    return rmsg
#%%%
#remove_inputfiles()
#******************************************************************************
### Process all_courses_list --> dfall
#******************************************************************************
def handle_acl(dfall):
    macl = []
    all_bool1 = str(type(dfall))
    all_bool2 = "<class 'bool'>"
    allf = None
    if all_bool1 != all_bool2:
        try:
            dfall = dfall[allCourses_columns]
            dfall.sort_values(by='course_name', inplace=True)
        except:
            macl.append("Replace acl: Column names of grade file are"+
                         " inconsistent")
            macl.append("Replace acl: Hence, grade file is not added to "
                          +"DB nor report")
            allf = False
            return dfall, allf, macl
        else:
            return dfall, allf, macl
    else:
        return dfall, allf, macl
#%%%%
#dfall, allf, macl = handle_acl(dfall)
#******************************************************************************
### Process grade file --> dfgra
#******************************************************************************
def get_grade(dfgra):
    lstr = set(dfgra["Final Exam"].tolist())
    if 'P' in lstr or 'F' in lstr:
        dfgra["Final Exam"]=dfgra["Final Exam"].apply(lambda x:
                    'Passed' if x == 'P' else('Failed'
                    if x == 'F' else('H' if x=='H' else 'NaN')))
        dfgra["Final Grade"] = dfgra["Final Exam"]
    else:
        dfgra['tmp'] = dfgra['Final Exam'].apply(lambda x:
                                                 1000 if x=='H' else x)
        dfgra['tmp'] = dfgra['tmp'].astype('float')
        cnds2 = [((dfgra["tmp"]>=70) & (dfgra["tmp"]<=100)),
                                        (dfgra["tmp"]<70),
                                     (dfgra["tmp"]==1000),
                                (dfgra["tmp"]==pd.np.nan)]
        vals2 = ['Passed', 'Failed', 'H','NaN']
        dfgra['Final Grade'] = np.select(cnds2,vals2)
        #dfgra = dfgra[['course_id', 'Final Exam','Final Grade']]

        cnds3 = [(dfgra["Final Grade"].isin(['Passed'])),
                    (dfgra["Final Grade"].isin(['Failed'])),
                    (dfgra["Final Grade"].isin(['H'])),
                    (~dfgra["Final Grade"].isin(['Passed','Failed','H']))]

        vals3 = ['Passed', 'Failed', 'H','NaN']
        dfgra['Final Grade'] = np.select(cnds3,vals3)
        del dfgra['tmp']
    return dfgra

def gen_grades(dfgra, ids):
    ccid2 = None
    gra_bool1 = str(type(dfgra))
    gra_bool2 = "<class 'bool'>"
    graf = None
    mgra = []
    if gra_bool1 != gra_bool2:
        try:
            dfgra['course_id'] = ids[1][0]
            ccid2 = ids[1][0]
            dfgra['course_type'] = ids[1][1]
            #dfgra = dfgra[grade_columns]
            dfgra = get_grade(dfgra)    
            dfgra['Student ID'] = dfgra['Student ID'].astype(str)
        except:
            mgra.append("Repalce gra: Column names of grade file are"
                          +" inconsistent")
            mgra.append("Repalce gra: Hence, grade file is not added to"
                          +" DB nor report")
            graf = False
            return dfgra, ccid2, graf, mgra
        else:
            return dfgra, ccid2, graf, mgra
    else:
        return dfgra, ccid2, graf, mgra
#%%%%
#dfgra, ccid2, graf,mgra = gen_grades(dfgra, ids)
#******************************************************************************
### Process Registrant file --> dfreg & demog
#******************************************************************************
def promo_code(dfreg):
    promlst = dfreg['Promo Code'].tolist()
    numlst = []
    for p in promlst:
        numlst.append(any(map(str.isdigit, str(p))))

    if any(numlst) == True:
        dfreg['temp'] = dfreg['Promo Code'].str.extract('(\d+)')
        dfreg["temp"] = pd.to_numeric(dfreg["temp"])
        dfreg["temp"] = dfreg["temp"].apply(lambda x: x if x>=0 else 'x' )
        cnds1 = [(dfreg["temp"]!='x'),(dfreg["temp"]=='x')]
        vals1 = [dfreg["temp"], dfreg['Total Price']]
        dfreg['Total Price'] = np.select(cnds1,vals1)
        dfreg['Total Price'] = pd.to_numeric(dfreg['Total Price'])
        del dfreg['temp']
    return dfreg

def get_demog(df, cols):
    cols1=[c for c in cols]
    tmp = cols1[2]
    subset = df[cols1]
    cols1[2] = 'object'
    subset.columns = cols1
    subset['by']=tmp
    subset['count']=1
    cols2 = list(subset.columns)
    subset = subset.groupby(cols2[0:4]).sum().reset_index()
    return subset
# Current Course ID
def gen_demography(dfreg, ids):
    mreg = []
    ccid1 = None
    reg_bool1 = str(type(dfreg))
    reg_bool2 = "<class 'bool'>"
    regf = None
    if reg_bool1 != reg_bool2:
        try:
            dfreg = promo_code(dfreg)
            dfreg['course_id'] = ids[0][0]
            ccid1 = ids[0][0]
            dfreg['course_type'] = ids[0][1]
            #Demography-By BU and Non-BU
            buNonBU = get_demog(dfreg, bunbu_columns)
            #Demography-By City bunbu_columns, city_columns, state_columns,
            cityreg = get_demog(dfreg, city_columns)
            #Demography-By State
            statereg = get_demog(dfreg, state_columns)
            #Demography-By Dept
            deptreg = get_demog(dfreg, dept_columns)
            #Demography-By Job-Title
            jt = 'Job Title:'
            jtreg = dfreg[['course_id','course_type',jt]]
            jtreg.columns = jt_columns
            jtreg = get_demog(jtreg, jt_columns)
            #Aggregate all demography datasets
            demog = pd.concat([buNonBU,cityreg,statereg,deptreg,jtreg],
                          ignore_index=True)
            # Revenue
            rev1 = dfreg[['course_id','course_type','Promo Code','Total Price']]
        except:
            mreg.append("Subsection-3.2: Column names of registrants are "
                  +"inconsistent")
            mreg.append("Replace reg: Hence, registrants are not added to"
                  +" DB nor report")
            demog, rev1, regf = False, False, False
            return demog, rev1, regf, ccid1, mreg
        else:
            return demog, rev1, regf, ccid1, mreg
    else:
        demog, rev1 = False, False
        return demog, rev1, regf, ccid1, mreg
#%%%%
#demog, rev, regf, ccid1, mreg = gen_demography(dfreg, ids)
#******************************************************************************
### Process cost Models --> dfcos
#******************************************************************************
# costs_pu/pr_acronym_yyyy_mm.xlsx
# dfcos
# Current Course ID
def gen_costModels(dfcos, ids):
    mcos = []
    ccid3 = None
    cosf = None
    if isinstance(dfcos, bool)==False:
        try:
            dfcos['course_id'] = ids[2][0]
            ccid3 = ids[2][0]
            dfcos['course_type'] = ids[2][1]
            #dfcos = dfcos[cost_columns]
        except:
            mcos.append("Replace cml: Column names of grade file are"
                          + " inconsistent")
            mcos.append("Replace cml: Hence, grade file is not added to"
                          +" DB nor report")
            cosf = False
            return dfcos, ccid3, cosf, mcos
        else:
            return dfcos, ccid3, cosf, mcos
    return dfcos, ccid3, cosf, mcos
#%%%%
#dfcos, ccid3, cosf, mcos = gen_costModels(dfcos, ids)
#******************************************************************************
### Process Suvey Files --> dfsur1
#******************************************************************************
# Current Course ID
def change_col(df):
    pat_col1 = 'Your Likelihood to Recommend this course?'
    pat_col2 = ' (Would you recommend it to a friend or colleague?)'
    pat_col = pat_col1 + pat_col2
    sur_col_all = list(df.columns)
    for i, col in enumerate(sur_col_all):
        if 'Your Likelihood to Recommend this' in col:
            sur_col_all[i] = pat_col
    df.columns = sur_col_all
    return df

def proc(df,c,i):
    q1c1 = df[[c[i],'count']].groupby(c[i]).sum().reset_index()
    q1c1['x']=c[i]
    q1c1 = q1c1[['x',c[i],'count']]
    q1c1.columns = ['questions','opinion','count']
    return q1c1

def ext_col(df, cn):
    cc = [df.columns[i] for i in range(len(df.columns))
          if cn in df.columns[i]]
    return cc

def gen_toot(dfsur, ids):
    mtoot = []
    sur1f, ccid4 = None, None
    sur_bool1 = str(type(dfsur))
    sur_bool2 = "<class 'bool'>"
    if sur_bool1 != sur_bool2:
        try:
            ev11 = change_col(dfsur)
            c1, c2 = ext_col(ev11, colcon[0]), ext_col(ev11, colcon[1])
            c3 = ext_col(ev11, colcon[2])
            c4, c5 = ext_col(ev11, colcon[3]), ext_col(ev11, colcon[4])
            c6 = ext_col(ev11, colcon[5])
            c7, c8 = ext_col(ev11, colcon[6]), ext_col(ev11, colcon[7])
            c9 = ext_col(ev11, colcon[8])
            dfsur_cols = c1+c2+c3+c4+c5+c6+c7+c8+c9
            ev11 = ev11[dfsur_cols]

            dfc1, dfc2, dfc3, dfc4 = ev11[c1], ev11[c2], ev11[c3], ev11[c4]
            dfc5, dfc6, dfc7, dfc8 = ev11[c5], ev11[c6], ev11[c7], ev11[c8]
            dfc9 = ev11[c9]

            qpt1 = []
            for cl in list(dfc2.columns):
                if 'Instructor were available and helpful' not in cl:
                    qpt1.append(cl)
            dfc2 = dfc2[qpt1]

            dfc1.columns, dfc2.columns, dfc3.columns = c1_new,c2_new,c3_new
            dfc4.columns, dfc5.columns, dfc6.columns = c4_new,c5_new, c6_new
            dfc7.columns, dfc8.columns, dfc9.columns = c7_new,c8_new, c9_new

            dfc1['count'], dfc2['count'], dfc3['count']=1, 1, 1
            dfc4['count'], dfc5['count'], dfc6['count']=1, 1, 1
            dfc7['count'], dfc8['count'], dfc9['count']=1, 1, 1

            q11,q12,q13,q14 = proc(dfc1,c1_new,0),proc(dfc1,c1_new,1),\
                  proc(dfc1,c1_new,2),proc(dfc1,c1_new,3)
            q21,q22,q23,q24 = proc(dfc2,c2_new,0),proc(dfc2,c2_new,1),\
                  proc(dfc2,c2_new,2),proc(dfc2,c2_new,3)
            q31,q32,q33,q34,q35 = proc(dfc3,c3_new,0),proc(dfc3,c3_new,1),\
            proc(dfc3,c3_new,2),proc(dfc3,c3_new,3), proc(dfc3,c3_new,4)

            q4 = proc(dfc4,c4_new,0)
            q5 = proc(dfc5,c5_new,0)
            q6 = proc(dfc6,c6_new,0)

            q71,q72 = proc(dfc7,c7_new,0), proc(dfc7,c7_new,1)
            q81 = proc(dfc8,c8_new,0)
            q91 = proc(dfc9,c9_new,0)

            dfsur1 = pd.concat([q11,q12,q13,q14,q21,q22,q23,q24,q31,q32,q33,
                            q34,q35,q4,q5,q6,q71,q72,q81,q91],ignore_index=True)
            dfsur1['course_id'] = ids[3][0]
            ccid4 = ids[3][0]
            dfsur1['course_type'] = ids[3][1]
            dfsur1 = dfsur1[sur_columns1]
            cndsvy = [
            (dfsur1['opinion'] == keysvy[0]),(dfsur1['opinion'] == keysvy[1]),
            (dfsur1['opinion'] == keysvy[2]),(dfsur1['opinion'] == keysvy[3]),
            (dfsur1['opinion'] == keysvy[4]),(dfsur1['opinion'] == keysvy[5]),
            (dfsur1['opinion'] == keysvy[6]),(dfsur1['opinion'] == keysvy[7]),
            (dfsur1['opinion'] == keysvy[8]),(dfsur1['opinion'] == keysvy[9]),
            (dfsur1['opinion'] == keysvy[10]),(dfsur1['opinion'] == keysvy[11]),
            (dfsur1['opinion'] == keysvy[12]),(dfsur1['opinion'] == keysvy[13]),
            (dfsur1['opinion'] == keysvy[14])]
            valuesvy = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
            dfsur1['scores'] = np.select(cndsvy, valuesvy)
            #dfsur1 = dfsur1[sur_columns]

        except:
            mtoot.append("Repalce svy: Column names of the survey file"
                          +" are inconsistent")
            mtoot.append("Repalce svy: Hence, the survey file is not added"
                          +" to DB nor report")
            sur1f, dfsur1 = False, False
            return dfsur1, ccid4, sur1f, mtoot
        else:
            return dfsur1, ccid4, sur1f, mtoot
    else:
        dfsur1 = False
        return dfsur1, ccid4, sur1f, mtoot
#%%%%
#dfsur1, ccid4, sur1f, mtoot = gen_toot(dfsur, ids)
#******************************************************************************
### Process Suvey Files --> dfsur1
#******************************************************************************
# ids = [idreg, idgra, idcos, ideva]
def add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1, ids):
    if isinstance(dfreg, bool)==False:
        dfreg['course_abb'] = ids[0][0].split('_')[0]
        my11=ids[0][0].split('_')
        my12 = my11[1:]
        dfreg['mmyyyy'] = '/'.join(my12[::-1])
        dfreg = dfreg[registrant_columns]
        demog['course_abb'] = ids[0][0].split('_')[0]
        demog['mmyyyy'] = '/'.join(my12[::-1])
        demog = demog[demog_columns]
    if isinstance(dfgra, bool)==False:
        dfgra['course_abb'] = ids[1][0].split('_')[0]
        my31=ids[1][0].split('_')
        my32 = my31[1:]
        dfgra['mmyyyy'] = '/'.join(my32[::-1])
        dfgra = dfgra[grade_columns]
    if isinstance(dfcos, bool)==False:
        dfcos['course_abb'] = ids[2][0].split('_')[0]
        my21=ids[2][0].split('_')
        my22 = my21[1:]
        dfcos['mmyyyy'] = '/'.join(my22[::-1])
        dfcos = dfcos[cost_columns]
    if isinstance(dfsur1, bool)==False:
        dfsur1['course_abb'] = ids[3][0].split('_')[0]
        my41=ids[3][0].split('_')
        my42 = my41[1:]
        dfsur1['mmyyyy'] = '/'.join(my42[::-1])
        dfsur1 = dfsur1[sur_columns]
    return dfreg,demog,dfcos,dfgra,dfsur1
#%%%%
#dfreg,demog,dfcos,dfgra,dfsur1 = \
    #add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1,ids)
#******************************************************************************
### Remove duplicates in Dataframes --> dfreg,demog,dfcos,dfgra,dfsur1
#******************************************************************************
def remove_duplicate(df, col):
    df.sort_values(col, inplace = True)
    df.drop_duplicates(subset =col,keep = 'first', inplace = True)
    return df
#******************************************************************************
### Read existing DB --> dfsur1
#******************************************************************************
def qerrydb():
    table_list = check_tables()
    def topd(df,col):
        dff = pd.DataFrame(df, columns=col)
        return dff

    engine = create_engine('sqlite:///'+dbpath, echo=False)
    #Flags
    aclf = regf = demf =  cmlf = graf = svyf = fsetf =False

    if 'course_list' in table_list:
        acl = topd(engine.execute('Select DISTINCT * from course_list'),
               allCourses_columns)
        aclf = True
    else: acl = False
    if 'registrants' in table_list:
        reg = topd(engine.execute('Select DISTINCT * from registrants'),
                    registrant_columns)
        regf = True
    else: reg = False
    if 'demography' in table_list:
        dem = topd(engine.execute('Select DISTINCT * from demography'),
                   demog_columns)
        demf = True
    else: dem = False
    if 'cost_model' in table_list:
        cml = topd(engine.execute('Select DISTINCT * from cost_model'),
                  cost_columns)
        cmlf = True
    else: cml = False
    if 'grade_report' in table_list:
        gra = topd(engine.execute('Select DISTINCT * from grade_report'),
               grade_columns)
        graf = True
    else: gra = False
    if 'surveys' in table_list:
        svy = topd(engine.execute('Select DISTINCT * from surveys'),
                    sur_columns)
        svyf = True
    else: svy = False
    lflags = [aclf, regf, demf,  cmlf, graf, svyf]
    return acl, reg, dem, cml, gra, svy, lflags
#%%%
#acl, reg, dem, cml, gra, svy, lflags = qerrydb()
#******************************************************************************
### Replace rows if they exist in DB Tables -->
#******************************************************************************
def replacetab(df, tbl, tab_name):
    flag, mrep = False, []
    if isinstance(tbl, bool)==False:
        if tab_name == 'course_list':
            rpl = df['acronym'].tolist()
            tbl = tbl[~tbl['acronym'].isin(rpl)]
            tbl = tbl.append(df)
            flag = True
        else:
            rpl = df['course_id'].tolist()
            tbl = tbl[~tbl['course_id'].isin(rpl)]
            tbl = tbl.append(df)
            flag = True
    else:
        try:
            tbl = df[list(df.columns)]
            flag = True
        except:
            flag = False
    def append_tab(df, engine, tab_name):
        df.to_sql(tab_name, engine, if_exists='replace',index=False)

    if flag == True:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()
        engine = create_engine('sqlite:///'+dbpath, echo=False)
        append_tab(tbl, engine, tab_name)
        mrep.append(f"The attempt to replace {tab_name} was successful!")
    else:
        mrep.append(f"The attempt to replace {tab_name} was unsuccessful!")
    return mrep

#******************************************************************************
### Main1
#******************************************************************************
#errors11 = []
#reptabs = []
def check_tables():
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tab = cursor.fetchall()
    table_list = []
    for t in list(tab):
        table_list.append(t[0])
    return table_list

def readProcessinputs():
    errors = []
    reptabs = []
    #errors11 = reptabs = []
    table_list = check_tables()
    filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur,statusc = read_dsets()
    #print('ids=',ids)
    wmsg1 = write_dsets(dfall, allCourses_columns, filenames[0],
                            "All Courses List File")
    wmsg2 = write_dsets(dfreg, registrant_columns1, filenames[1],
                                "Registrants File")
    wmsg3 = write_dsets(dfgra, grade_columns1, filenames[2],
                                "Grades File")
    wmsg4 = write_dsets(dfcos, cost_columns1, filenames[3],
            "Cost List File")
    wmsg5 = write_dsets(dfsur, suvy1_cols1, filenames[4], "Survey File")
    rmsg = remove_inputfiles()
    wmsg = wmsg1 + wmsg2 + wmsg3 + wmsg3 + wmsg4+ wmsg5 + rmsg

    dfall, allf, macl = handle_acl(dfall)
    dfgra, ccid2, graf, mgra = gen_grades(dfgra, ids)
    demog, rev, regf, ccid1, mreg = gen_demography(dfreg, ids)
    dfsur1, ccid4, sur1f, mtoot = gen_toot(dfsur, ids)
    dfcos, ccid3, cosf, mcos = gen_costModels(dfcos, ids)
    dfreg,demog,dfcos,dfgra,dfsur1=add_abb_date(
    dfreg,demog,dfcos,dfgra,dfsur1,ids)
    dmsgs = macl + mgra + mreg + mtoot + mcos


    acl, reg, dem, cml, gra, svy,lflags =  qerrydb()
    mrep1 = mrep2 = mrep3 = mrep4 = mrep5 = mrep6 = []
    if isinstance(dfall, bool)==False:
        dfall = remove_duplicate(dfall, ['course_name', 'acronym'])
        mrep1 = replacetab(dfall, acl, 'course_list')
        reptabs.append('course_list')
    if isinstance(dfreg, bool)==False:
        dfreg = remove_duplicate(dfreg, ['course_id','First Name:',
                     'Last Name:','Email Address:'])
        mrep2 = replacetab(dfreg, reg, 'registrants')
        reptabs.append('registrants')
    if isinstance(demog, bool)==False:
        demog = remove_duplicate(demog, ['course_id','object','by','count'])
        mrep3 =replacetab(demog, dem, 'demography')
        reptabs.append('demography')
    if isinstance(dfcos, bool)==False:
        dfcos = remove_duplicate(dfcos, ['course_id','Name','Role',
                                 'Pay', 'Type', 'Location'])
        mrep4 = replacetab(dfcos, cml, 'cost_model')
        reptabs.append('cost_model')
    if isinstance(dfgra, bool)==False:
        dfgra = remove_duplicate(dfgra, ['course_id','Last Name','First Name'])
        mrep5 = replacetab(dfgra, gra, 'grade_report')
        reptabs.append('grade_report')
    if isinstance(dfsur1, bool)==False:
        dfsur1 = remove_duplicate(dfsur1, ['course_id','questions', 'opinion',
                                      'count'])
        mrep6 = replacetab(dfsur1, svy, 'surveys')
        reptabs.append('surveys')
    mrep = mrep1 + mrep2 + mrep3 + mrep4 + mrep5 + mrep6
    if len(reptabs) == 0:
        reptabs.append('None')
    errors = errors+statusc+wmsg+dmsgs+mrep
    return errors, reptabs
#%%%
#errors11,reptabs = readProcessinputs()
#******************************************************************************
#                                   ~END~
#******************************************************************************
