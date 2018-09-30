# -*- coding: utf-8 -*-
"""
Created on THU SEP 20

@author: nimit kothari
"""

import os
import json
from flask import Flask,Response,request
#from flask_cors import CORS
import pandas as pd
import pickle


path = os.getcwd()
print(path)
port = 80
app = Flask(__name__)
#CORS(app)

@app.route('/query', methods=['POST'])

def get_status():
    try:
        req_body = request.get_json(force=True)
        df = dfConverter(req_body)
        #df = df.drop(['unId'], axis=1)
        #df = df.drop(['credibility'], axis=1)
        print("dataframe",df)
        #df.to_csv('df.csv', sep=',', encoding='utf-8')
        classifier = pickle.load(open('clf.pkl', 'rb'))
        print("classifier loaded",classifier)
        credibility = classifier.predict(df)
        print(credibility)
        if (credibility >= 1.5):
            msg = {"status":2}
        else :
            msg = {"status":1}
        resp = Response(response=json.dumps(msg), status=200, mimetype="application/json")
        print("response", resp)
        return resp

    except Exception as e:
        print(e)

@app.route('/login', methods=['POST'])
def login():
    try:
        req_body = request.get_json(force=True)
        username = req_body["username"]
        password = req_body["password"]
        if username == 'applicant' and password == 'pass1234':
            msg = {"allow":1}
            return Response(response=json.dumps(msg), status=200, mimetype="application/json")
        else :
            msg = {"allow":0}
            return Response(response=json.dumps(msg), status=200, mimetype="application/json")
    except Exception as e:
        print(e)


def dfConverter(jsonData):
    dictNew = []
    #unId = jsonData['unId']
    duration = jsonData['duration']
    credit_amount = jsonData['credit_amount']
    installment_rate = jsonData['installment_rate']
    present_residence_since = jsonData['present_residence_since']
    age = jsonData['age']
    no_of_existing_credits = jsonData['no_of_existing_credits']
    no_of_people_being_liable = jsonData['no_of_people_being_liable']

    status = jsonData['status']
    if status == 'A11':
        status_1 = 1
    else:
        status_1 = 0

    if status == 'A12' or status == 'A13':
        status_2 = 1
    else:
        status_2 = 0

    if status == 'A14':
        status_3 = 1
    else:
        status_3 = 0

    credit = jsonData['credit']
    if credit == 'A30' or credit == 'A31':
        credit_1 = 1
    else:
        credit_1 = 0

    if credit == 'A32':
        credit_2 = 1
    else:
        credit_2 = 0

    if credit == 'A33' or credit == 'A34':
        credit_3 = 1
    else:
        credit_3 = 0

    purpose = jsonData['purpose']
    if purpose == 'A40':
        purpose_1 = 1
    else:
        purpose_1 = 0

    if purpose == 'A41':
        purpose_2 = 1
    else:
        purpose_2 = 0

    if purpose == 'A42':
        purpose_3 = 1
    else:
        purpose_3 = 0

    if purpose == 'A43':
        purpose_4 = 1
    else:
        purpose_4 = 0

    if purpose == 'A49':
        purpose_6 = 1
    else:
        purpose_6 = 0

    if purpose == 'A44' or purpose == 'A45' or purpose == 'A46' or purpose == 'A47' or purpose == 'A48' or purpose == 'A410':
        purpose_5 = 1
    else:
        purpose_5 = 0

    savings_account_bonds = jsonData['savings_account_bonds']

    if savings_account_bonds == 'A61':
        savings_account_bonds_1 = 1
    else:
        savings_account_bonds_1 = 0

    if savings_account_bonds == 'A62':
        savings_account_bonds_2 = 1
    else:
        savings_account_bonds_2 = 0

    if savings_account_bonds == 'A63' or savings_account_bonds == 'A64':
        savings_account_bonds_3 = 1
    else:
        savings_account_bonds_3 = 0

    if savings_account_bonds == 'A65':
        savings_account_bonds_4 = 1
    else:
        savings_account_bonds_4 = 0

    present_employment_since = jsonData['present_employment_since']

    if present_employment_since == 'A71':
        present_employment_since_A71 = 1
    else:
        present_employment_since_A71 = 0

    if present_employment_since == 'A72':
        present_employment_since_A72 = 1
    else:
        present_employment_since_A72 = 0

    if present_employment_since == 'A73':
        present_employment_since_A73 = 1
    else:
        present_employment_since_A73 = 0

    if present_employment_since == 'A74':
        present_employment_since_A74 = 1
    else:
        present_employment_since_A74 = 0

    if present_employment_since == 'A75':
        present_employment_since_A75 = 1
    else:
        present_employment_since_A75 = 0

    personal_status_sex = jsonData['personal_status_sex']

    if personal_status_sex == 'A91':
        personal_status_sex_A91 = 1
    else:
        personal_status_sex_A91 = 0

    if personal_status_sex == 'A92':
        personal_status_sex_A92 = 1
    else:
        personal_status_sex_A92 = 0

    if personal_status_sex == 'A93':
        personal_status_sex_A93 = 1
    else:
        personal_status_sex_A93 = 0

    if personal_status_sex == 'A94':
        personal_status_sex_A94 = 1
    else:
        personal_status_sex_A94 = 0

    other_debtors_guarantors = jsonData['other_debtors_guarantors']
    if other_debtors_guarantors == 'A101':
        other_debtors_guarantors_1 = 1
    else:
        other_debtors_guarantors_1 = 0

    if other_debtors_guarantors == 'A102' or other_debtors_guarantors == 'A103':
        other_debtors_guarantors_2 = 1
    else:
        other_debtors_guarantors_2 = 0

    property1 = jsonData['property']

    if property1 == 'A121':
        property_A121 = 1
    else:
        property_A121 = 0

    if property1 == 'A122':
        property_A122 = 1
    else:
        property_A122 = 0

    if property1 == 'A123':
        property_A123 = 1
    else:
        property_A123 = 0

    if property1 == 'A124':
        property_A124 = 1
    else:
        property_A124 = 0

    other_installment_plans = jsonData['other_installment_plans']
    if other_installment_plans == 'A141' or other_installment_plans == 'A142':
        other_installment_plans_1 = 1
    else:
        other_installment_plans_1 = 0

    if other_installment_plans == 'A143':
        other_installment_plans_2 = 1
    else:
        other_installment_plans_2 = 0

    housing = jsonData['housing']
    if housing == 'A151' or housing == 'A153':
        housing_1 = 1
    else:
        housing_1 = 0

    if housing == 'A152':
        housing_2 = 1
    else:
        housing_2 = 0

    job = jsonData['job']
    if job == 'A171':
        job_A171 = 1
    else:
        job_A171 = 0
    if job == 'A172':
        job_A172 = 1
    else:
        job_A172 = 0
    if job == 'A173':
        job_A173 = 1
    else:
        job_A173 = 0
    if job == 'A174':
        job_A174 = 1
    else:
        job_A174 = 0

    telephone = jsonData['telephone']

    if telephone == 'A191':
        telephone_A191 = 1
    else:
        telephone_A191 = 0

    if telephone == 'A192':
        telephone_A192 = 1
    else:
        telephone_A192 = 0

    dictNew.append({"duration": int(duration),
                    "credit_amount": int(credit_amount),
                    "installment_rate": int(installment_rate),
                    "present_residence_since": int(present_residence_since),
                    "age": int(age),
                    "no_of_existing_credits": int(no_of_existing_credits),
                    "no_of_people_being_liable": int(no_of_people_being_liable),
                    "status_1": status_1,
                    "status_2": status_2,
                    "status_3": status_3,
                    "credit_1": credit_1,
                    "credit_2": credit_2,
                    "credit_3": credit_3,
                    "purpose_1": purpose_1,
                    "purpose_2": purpose_2,
                    "purpose_3": purpose_3,
                    "purpose_4": purpose_4,
                    "purpose_5": purpose_5,
                    "purpose_6": purpose_6,
                    "savings_account_bonds_1": savings_account_bonds_1,
                    "savings_account_bonds_2": savings_account_bonds_2,
                    "savings_account_bonds_3": savings_account_bonds_3,
                    "savings_account_bonds_4": savings_account_bonds_4,
                    "present_employment_since_A71": present_employment_since_A71,
                    "present_employment_since_A72": present_employment_since_A72,
                    "present_employment_since_A73": present_employment_since_A73,
                    "present_employment_since_A74": present_employment_since_A74,
                    "present_employment_since_A75": present_employment_since_A75,
                    "personal_status_sex_A91": personal_status_sex_A91,
                    "personal_status_sex_A92": personal_status_sex_A92,
                    "personal_status_sex_A93": personal_status_sex_A93,
                    "personal_status_sex_A94": personal_status_sex_A94,
                    "other_debtors_guarantors_1": other_debtors_guarantors_1,
                    "other_debtors_guarantors_2": other_debtors_guarantors_2,
                    "property_A121": property_A121,
                    "property_A122": property_A122,
                    "property_A123": property_A123,
                    "property_A124": property_A124,
                    "other_installment_plans_1": other_installment_plans_1,
                    "other_installment_plans_2": other_installment_plans_2,
                    "housing_1": housing_1,
                    "housing_2": housing_2,
                    "job_A171": job_A171,
                    "job_A172": job_A172,
                    "job_A173": job_A173,
                    "job_A174": job_A174,
                    "telephone_A191": telephone_A191,
                    "telephone_A192": telephone_A192,
                    }
                   )

    dfFinal = pd.DataFrame(dictNew, columns=
    ["duration",
     "credit_amount",
     "installment_rate",
     "present_residence_since",
     "age",
     "no_of_existing_credits",
     "no_of_people_being_liable",
     "status_1",
     "status_2",
     "status_3",
     "credit_1",
     "credit_2",
     "credit_3",
     "purpose_1",
     "purpose_2",
     "purpose_3",
     "purpose_4",
     "purpose_5",
     "purpose_6",
     "savings_account_bonds_1",
     "savings_account_bonds_2",
     "savings_account_bonds_3",
     "savings_account_bonds_4",
     "present_employment_since_A71",
     "present_employment_since_A72",
     "present_employment_since_A73",
     "present_employment_since_A74",
     "present_employment_since_A75",
     "personal_status_sex_A91",
     "personal_status_sex_A92",
     "personal_status_sex_A93",
     "personal_status_sex_A94",
     "other_debtors_guarantors_1",
     "other_debtors_guarantors_2",
     "property_A121",
     "property_A122",
     "property_A123",
     "property_A124",
     "other_installment_plans_1",
     "other_installment_plans_2",
     "housing_1",
     "housing_2",
     "job_A171",
     "job_A172",
     "job_A173",
     "job_A174",
     "telephone_A191",
     "telephone_A192",

     ])

    return dfFinal
if __name__ == '__main__':
    #app.run( port=port, threaded=True,debug=True)
    app.run( port=port, threaded=True)