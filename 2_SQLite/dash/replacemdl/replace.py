#******************************************************************************
# 1. Columns 
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
grade_columns3 = ['course_id','Last Name','First Name', 'Username',
                  'Student ID','Last Access','Availability',
                  'Final Exam']
grade_columns4 = grade_columns3+['year']

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

# Dictionary of Columns
dupcols = {'acl':['course_name', 'acronym'],
           'reg':['course_id','First Name:','Last Name:','Email Address:'],
           'dem':['course_id','object','by','count'],
           'cml':['course_id','Name','Role', 'Pay', 'Type','Location'],
           'gra':['course_id','Last Name', 'First Name'],
           'svy':['course_id','questions', 'opinion', 'count'],
           'set':['percentage_name','Short_name']}

allcols = {'acl': allCourses_columns, 'reg':registrant_columns, 
            'dem': demog_columns, 'cml': cost_columns, 
            'gra': grade_columns, 'svy': sur_columns, 
            'set': dest_cols}

dfmsg = {'set':'Fraction setting','acl':'All Courses List',
          'cml': 'Cost Model File', 'reg':'Registration File',
          'dem':'Demography Dataframe', 'gra':'Grade File',
          'svy':'Survey File'}

tbls  = {'acl':'course_list', 'reg':'registrants', 
         'dem':'demography', 'cml':'cost_model',
         'gra':'grade_report', 'svy':'surveys'}
#******************************************************************************
# 2. Import Libraries and Packages
#******************************************************************************
from datetime import datetime as dtt
from datetime import date
import pandas as pd
import numpy as np
import os, sys, glob
import sqlite3
from sqlalchemy import create_engine

#******************************************************************************
# 3. Reading Inputs
#******************************************************************************
#******************************************************************************
### Read an Excel file from replace folder
                   # dfall, dfreg, demog, dfcos, dfgra, dfsur1, dfset
#******************************************************************************
def extrat_id(fn, prefix, rpath):    
    idd = fn.replace(rpath, '')
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
def read_dsets(rpath):    
    statusc = []
    filenames, ids =get_filenames(glob.glob(rpath+"*.xlsx"))
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
#filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, statusc = read_dsets()

#******************************************************************************
# 4. Backup read-in datasets in All_Datasets Folder
#******************************************************************************
def write_dsets(df, col, filename, msg, rpath, apath):
    wmsg = []    
    if  isinstance(df, bool)==False:
        if set(col).issubset(set(list(df.columns))):
            dfw = df[col]            
            dfw.to_excel(apath + filename.replace(rpath, ''),index=False)

        else:
            var="Replace (write_dsets()): Error! Columns mismatch in "+msg+"!"
            wmsg.append(var)

    else:
        var = "Replace (write_dsets()): No " + msg + " to write to"+\
               " All_Datasets Folder!"
        wmsg.append(var)
    return wmsg

#call_writer(dfall, dfreg, dfgra, dfcos, dfsur, filenames)

#******************************************************************************
#5. Remove files from Replace folder after reading them in
#******************************************************************************
def remove_inputfiles(rpath):    
    rmsg = []
    try:
        files = glob.glob(rpath+'*.xlsx')
        for f in files:
            os.remove(f)
    except:
        rmsg.append("Replace (remove_inputfiles): No files to remove!")
    return rmsg

#remove_inputfiles()

#******************************************************************************
#6. Process all_courses_list --> dfall
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

#dfall, allf, macl = handle_acl(dfall)

#******************************************************************************
#7. Process grade file --> dfgra
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

#dfgra, ccid2, graf,mgra = gen_grades(dfgra, ids)

#******************************************************************************
#8. Process Registrant file --> dfreg & demog
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

#demog, rev, regf, ccid1, mreg = gen_demography(dfreg, ids)

#******************************************************************************
#9. Process cost Models --> dfcos
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

#dfcos, ccid3, cosf, mcos = gen_costModels(dfcos, ids)

#******************************************************************************
#10. Process Suvey Files --> dfsur1
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

#dfsur1, ccid4, sur1f, mtoot = gen_toot(dfsur, ids)

#******************************************************************************
#11. Add course_abb and date
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

#dfreg,demog,dfcos,dfgra,dfsur1 = \
    #add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1,ids)

#******************************************************************************
# 12. Functions for Updating DB Tables
#******************************************************************************
def updateCourselistTable(course_name, acronym, cost_model):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        gl1 = """Update course_list set course_name = ?, cost_model = ? """
        gl2 = """where acronym = ?"""
        sqlite_update_query = gl1+gl2        
        columnValues = (course_name, cost_model, acronym)
        con.commit()
        msg = "Course_List updated successfully!"       
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Course_List update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg

def updateRegistrantsTable(course_id, course_abb, mmyyyy, course_type,
                            First_Name, Last_Name, Email_Address, Address_1,
                            City, State, Education_Level, Country, ZIP_Code,
                            Phone, Company_School, Job_Title, Department,
                            How_did_you_hear_about_this_course, Registration_Date,
                            Registration_Status, Payment_Status, Payment_Type,
                            Fee_Type, Promo_Code, Code_Type, Discount_Percent,
                            Discount_Amount, Total_Price):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        reg1 = """Update registrants set course_abb= ?, mmyyyy= ?, """
        reg2 = """course_type= ?, First_Name= ?, Last_Name= ?, Email_Address= ?, """ 
        reg3 = """Address_1= ?, City= ?, State= ?, Education_Level= ?, Country= ?, """ 
        reg4 = """ZIP_Code= ?,Phone= ?, Company_School= ?, Job_Title= ?, """ 
        reg5 = """Department= ?, How_did_you_hear_about_this_course= ?, """ 
        reg6 = """Registration_Date= ?,Registration_Status= ?, Payment_Status= ?, """ 
        reg7 = """Payment_Type= ?,Fee_Type= ?, Promo_Code= ?, Code_Type= ?, """ 
        reg8 = """Discount_Percent= ?, Discount_Amount= ?, Total_Price= ? """
        reg9 = """where course_id= ? """
        sqlite_update_query = reg1+reg2+reg3+reg4+reg5+reg6+reg7+reg8+reg9      
        columnValues = (course_abb, mmyyyy, course_type,
                            First_Name, Last_Name, Email_Address, Address_1,
                            City, State, Education_Level, Country, ZIP_Code,
                            Phone, Company_School, Job_Title, Department,
                            How_did_you_hear_about_this_course, Registration_Date,
                            Registration_Status, Payment_Status, Payment_Type,
                            Fee_Type, Promo_Code, Code_Type, Discount_Percent,
                            Discount_Amount, Total_Price, course_id)
        cursor.execute(sqlite_update_query, columnValues)        
        msg = "Registrants_Table was updated successfully!"
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Registrants_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg

def updateGradeTable(course_id,course_abb,mmyyyy,course_type,Last_Name,
                 First_Name,Username, Student_ID,Last_Access,
                 Availability, Final_Exam, Final_Grade):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        gl1 = f"""Update grade_report set course_abb = ?,mmyyyy= ?, """
        gl2 = """course_type = ?, Last_Name = ?, First_Name = ?, """
        gl3 = """Username = ?, Student_ID = ?, Last_Access = ?, """
        gl4 = """Availability = ?, Final_Exam = ?, Final_Grade = ? """
        gl5 = """where course_id = ?"""
        sqlite_update_query = gl1+gl2+gl3+gl4+gl5
        
        columnValues = (course_abb,mmyyyy,course_type,Last_Name,
                 First_Name,Username, Student_ID,Last_Access,
                 Availability, Final_Exam, Final_Grade, course_id)
        cursor.execute(sqlite_update_query, columnValues)        
        msg = "Grade_Table was updated successfully!"
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Grade_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg

def updateCostTable(course_id, course_abb, mmyyyy, course_type,
                    Name, Role, Pay, Type, Location):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        gl1 = f"""Update cost_model set course_abb = ?,mmyyyy= ?, """
        gl2 = """course_type = ?, Name = ?, Role = ?, """
        gl3 = """Pay = ?, Type = ?, Location = ? """        
        gl4 = """where course_id = ?"""
        sqlite_update_query = gl1+gl2+gl3+gl4
        
        columnValues = (course_abb, mmyyyy, course_type,
                        Name, Role, Pay, Type, Location, course_id)
        cursor.execute(sqlite_update_query, columnValues)
        con.commit()
        msg = "Cost_Table was updated successfully!"
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Grade_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg 

def updateDemographyTable(course_id, course_abb, mmyyyy, course_type,
                                                  object, by, count):
    msg = ''
    try: 
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        gl1 = f"""Update demography set course_abb = ?, mmyyyy= ?, """
        gl2 = """course_type = ?, object = ?, by = ?, """
        gl3 = """count = ? where course_id = ? """         
        sqlite_update_query = gl1+gl2+gl3        
        columnValues = (course_abb, mmyyyy, course_type,
                            object, by, count, course_id)
        cursor.execute(sqlite_update_query, columnValues)        
        msg = "Demography_Table was updated successfully!"
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Demography_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg

def updateSurveysTable(course_id, course_abb, mmyyyy, course_type,
                                questions, opinion, scores, count):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()        
        gl1 = f"""Update surveys set course_abb = ?, mmyyyy= ?, """
        gl2 = """course_type = ?, questions = ?,  opinion = ?, """
        gl3 = """scores = ?, count = ? where course_id = ? """         
        sqlite_update_query = gl1+gl2+gl3       
        columnValues = (course_abb, mmyyyy, course_type,
                        questions, opinion, scores, count, course_id)
        cursor.execute(sqlite_update_query, columnValues)  
        msg = "Surveys_Table was updated successfully!"
        con.commit()
        cursor.close()

    except sqlite3.Error as error:
        msg = f"Surveys_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return msg

#******************************************************************************
# 13. Accessory Functions
#******************************************************************************
# Replace spaces with underscore in columns
def replacespace(col):
    return [col.replace(' ', '_') for col in col]

# Preprocess columns of Registration Files
def replacespacer(col):
    tmp = [col.replace(' ', '_') for col in col]
    tmp = [col.strip(':') for col in tmp]
    tmp = [col.strip('?') for col in tmp]
    tmp = [col.replace('/', '_') for col in tmp]
    return tmp

def check_tables(dpath):
    msg = ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tab = cursor.fetchall()
        table_list = []
        for t in list(tab):
            table_list.append(t[0])
        msg = "Tables grabbed successfully!"
    except sqlite3.Error as error:
        msg = f"Grade_Table update failed due to {error}."
    finally:
        if con:
            con.close()
    return table_list, msg

def remove_duplicate(df, col):
    if isinstance(df, bool)==False:
        df.sort_values(col, inplace = True)
        df.drop_duplicates(subset =col,keep = 'first', inplace = True)
    return df

#******************************************************************************
#14. Main for Updating DB Tables
#******************************************************************************
def updatemain(df, flag, dfname): 
    msg = ''
    if isinstance(df, bool)== False:
        tuples = list(df.itertuples(index=False, name=None))
        if flag == 'acl':
            for tup in tuples:            
                course_name, acronym, cost_model = tup
                msg = updateCourselistTable(course_name, acronym, 
                                     cost_model)
            msg = msg
        elif flag == 'reg':
            def replacespacer(col):
                tmp = [col.replace(' ', '_') for col in col]
                tmp = [col.strip(':') for col in tmp]
                tmp = [col.strip('?') for col in tmp]
                tmp = [col.replace('/', '_') for col in tmp]
                return tmp
            df.columns = replacespacer(df.columns)
            tuples = list(df.itertuples(index=False, name=None))            
            for tup in tuples: 
                course_id, course_abb, mmyyyy,\
                course_type, First_Name, Last_Name,\
                Email_Address, Address, City,State, \
                Education_Level, Country, ZIP_Code,\
                Phone, Company_School, Job_Title,\
                Department, How_did_you_hear_about_this_course,\
                Registration_Date, Registration_Status,\
                Payment_Status, Payment_Type, Fee_Type,\
                Promo_Code, Code_Type, Discount_Percent,\
                Discount_Amount, Total_Price = tup
                msg = updateRegistrantsTable(course_id, course_abb, mmyyyy,
                                       course_type, First_Name, Last_Name,
                                       Email_Address, Address, City,State, 
                                       Education_Level, Country, ZIP_Code,
                                       Phone, Company_School, Job_Title,
                                Department, How_did_you_hear_about_this_course,
                                       Registration_Date, Registration_Status,
                                       Payment_Status, Payment_Type, Fee_Type, 
                                       Promo_Code, Code_Type, Discount_Percent,
                                       Discount_Amount, Total_Price)   
            msg = msg
        elif flag == 'dem':
            for tup in tuples:
                course_id, course_abb, mmyyyy, course_type,\
                object, by, count = tup
                msg = updateDemographyTable(course_id, course_abb, 
                                      mmyyyy, course_type,
                                      object, by, count) 
            msg = msg
            
        elif flag == 'gra':
            for tup in tuples:
                course_id,course_abb,mmyyyy,course_type,\
                Last_Name,First_Name,Username,\
                Student_ID,Last_Access, Availability,\
                Final_Exam, Final_Grade = tup
                msg = updateGradeTable(course_id,course_abb,
                                 mmyyyy,course_type,Last_Name,
                                 First_Name,Username, 
                                 Student_ID,Last_Access,
                                 Availability, Final_Exam, 
                                 Final_Grade) 
            msg = msg
            
        elif flag == 'cml':
            for tup in tuples:
                course_id, course_abb, mmyyyy, course_type,\
                    Name, Role, Pay, Type, Location = tup
                msg = updateCostTable(course_id, course_abb, mmyyyy, course_type,
                    Name, Role, Pay, Type, Location)  
            msg = msg
        elif flag == 'svy':
            for tup in tuples:
                course_id, course_abb, mmyyyy, course_type,\
                questions, opinion, scores, count = tup
                msg = updateSurveysTable(course_id, course_abb, mmyyyy, course_type,
                                   questions, opinion, scores, count) 
            msg = msg
        else:
            msg = f"{flag} doesn't match with any of the dataframes!"
    else:
        msg = f"{dfname} is empty!"     
    return msg
#updatemain(df, flag, dfname)
#******************************************************************************
# 11. Replace Tables
#******************************************************************************
"""
cpath="D:\\DashProject02June20\\"
rpath_9 = os.path.join(cpath,"DatasetsAndReprots\\Replace\\")
apath_5 = os.path.join(cpath,"DatasetsAndReprots\\All_Datasets\\")
dbpath = os.path.join(cpath,"PythonAndSqlite\\py_and_db\\DashProjDB.db")
""" allcols, dfmsg, tbls

def replace_tables(rpath, apath, dbpath):
    errors = reptabs = []
    wmsg  = dmsgs = []
 
   
    table_list = check_tables(dpath)
    filenames, ids, dfall, dfreg, dfgra, dfcos,\
         dfsur,statusc = read_dsets(rpath)

 
    wmsg1 = write_dsets(dfall, allcols['acl'], filenames[0], dfmsg['acl'],
                rpath, apath)
    wmsg2 = write_dsets(dfreg, allcols['reg'], filenames[1], dfmsg['reg'],
                rpath, apath)
    wmsg3 = write_dsets(dfgra, allcols['gra'], filenames[2], dfmsg['gra'],
                rpath, apath)    
    wmsg4 = write_dsets(dfcos, allcols['cml'], filenames[3], dfmsg['cml'],
                rpath, apath)      
    wmsg5 = write_dsets(dfsur, allcols['svy'], filenames[3], dfmsg['svy'],
                rpath, apath)

    rmsg = remove_inputfiles(rpath)

    wmsg = wmsg1 + wmsg2 + wmsg3 + wmsg3 + wmsg4+ wmsg5 + rmsg

    dfall, allf, macl = handle_acl(dfall)
    dfgra, ccid2, graf, mgra = gen_grades(dfgra, ids)
    demog, rev, regf, ccid1, mreg = gen_demography(dfreg, ids)
    dfsur1, ccid4, sur1f, mtoot = gen_toot(dfsur, ids)
    dfcos, ccid3, cosf, mcos = gen_costModels(dfcos, ids)
    dfreg,demog,dfcos,dfgra,dfsur1=add_abb_date(
    dfreg,demog,dfcos,dfgra,dfsur1,ids)
    dmsgs = macl + mgra + mreg + mtoot + mcos       

    dfall = remove_duplicate(dfall, dupcols['acl'])
    dfgra = remove_duplicate(dfgra, dupcols['gra'])
    dfreg = remove_duplicate(dfreg, dupcols['reg'])
    dfcos = remove_duplicate(dfcos, dupcols['cml'])
    demog = remove_duplicate(demog, dupcols['dem'])
    dfsur1 = remove_duplicate(dfsur1, dupcols['svy'])

    mrep1 = mrep2 = mrep3 = mrep4 = mrep5 = mrep6 = []
    mrep1 = updatemain(dfall, 'acl',dfmsg['acl'])
    mrep2 = updatemain(dfgra, 'gra',dfmsg['gra'])
    mrep3 = updatemain(dfreg, 'reg',dfmsg['reg'])
    mrep4 = updatemain(dfcos, 'cml',dfmsg['cml'])
    mrep5 = updatemain(demog, 'dem',dfmsg['dem'])
    mrep6 = updatemain(dfsur1, 'svy',dfmsg['svy'])
    mrep = mrep1 + mrep2 + mrep3 + mrep4 + mrep5 + mrep6

    if len(reptabs) == 0:
        reptabs.append('None')
    errors = errors+statusc+wmsg+dmsgs+
    
    return errors, reptabs
#errors11,reptabs = readProcessinputs()
#******************************************************************************
#                                   ~END~
#******************************************************************************
