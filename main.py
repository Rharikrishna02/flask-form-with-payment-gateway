from flask import Flask,render_template,request,redirect,url_for
import os
from werkzeug.utils import secure_filename
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials

from firebase_admin import credentials, initialize_app, storage
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build

import pandas as pd

app = Flask(__name__)
app.config['FILE_UPLOADS'] = 'static/files'
firebaseConfig = {
  "apiKey": "AIzaSyBNIpa8uqAz-sXfby1dRtfXQiOA_bpfhjE",
  "authDomain": "tidshots.firebaseapp.com",
  "projectId": "tidshots",
  "storageBucket": "tidshots.appspot.com",
  "messagingSenderId": "298901560768",
  "appId": "1:298901560768:web:7e9fb209bab1f21eabfc25",
  "measurementId": "G-V11CJ8WYLT"
};
@app.route("/success",methods=['POST',"GET"]) 
def suc():
    return render_template('success.html')

@app.route("/trans100",methods=['POST',"GET"]) 
def tran100():
    if(request.method=='POST'):
        with open('myfile.txt') as f:
            nn=f.readline()
        data=nn.split("-")
        tid=request.form.get('tid')
        file=request.files['file']
        filename=secure_filename(file.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir,app.config["FILE_UPLOADS"],data[0]+'.png'))
        cred = credentials.Certificate("./static/files/tidshots-firebase-adminsdk-psrzj-1c3853d0d8.json")
        initialize_app(cred, {'storageBucket': 'tidshots.appspot.com'})

        # Put your local file path 
        fileName = "./static/files/"+data[0]+'.png'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

        # Opt : if you want to make public access from the URL
        blob.make_public()

        file_path= blob.public_url
        data={'auid':[data[0]],'filepath':str(file_path),'amount':'100'}
        df=pd.DataFrame(data)
        scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials1 = Credentials.from_service_account_file('./static/files/woven-invention-377716-9c2ae2d0cfbe.json', scopes=scopes)
        gc = gspread.authorize(credentials1)
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        year1='1QTeoBawNK4PYxNiU7RybXUkl12Rnailbfm5-vD8wFcQ'
        gs = gc.open_by_key(year1)
        worksheet1 = gs.worksheet('Sheet1')
    
        records_data = worksheet1.get_all_records()
        if len(records_data)==0:
          res=df
        else:
          df2 = pd.DataFrame.from_dict(records_data)
          res = df2.set_index(['auid'])\
               .combine_first(df.set_index(['auid']))\
               .reset_index()
          
    
        gs.worksheet('Sheet1').clear()

        set_with_dataframe(worksheet=worksheet1, dataframe=res, include_index=False,include_column_header=True, resize=True)
        return render_template('success.html')

    with open('myfile.txt') as f:
        nn=f.readline()
    data=nn.split("-")
    return render_template('transaction100.html',uid=data[0],name=data[1])


@app.route("/trans200",methods=['POST',"GET"]) 
def tran200():
    if(request.method=='POST'):
        with open('myfile.txt') as f:
            nn=f.readline()
        data=nn.split("-")
        tid=request.form.get('tid')
        file=request.files['file']
        filename=secure_filename(file.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir,app.config["FILE_UPLOADS"],data[0]+'.png'))
        cred = credentials.Certificate("./static/files/tidshots-firebase-adminsdk-psrzj-1c3853d0d8.json")
        initialize_app(cred, {'storageBucket': 'tidshots.appspot.com'})

        # Put your local file path 
        fileName = "./static/files/"+data[0]+'.png'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

        # Opt : if you want to make public access from the URL
        blob.make_public()

        file_path= blob.public_url
        data={'auid':[data[0]],'filepath':str(file_path),'amount':'200'}
        df=pd.DataFrame(data)
        scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials1 = Credentials.from_service_account_file('./static/files/woven-invention-377716-9c2ae2d0cfbe.json', scopes=scopes)
        gc = gspread.authorize(credentials1)
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        year1='1QTeoBawNK4PYxNiU7RybXUkl12Rnailbfm5-vD8wFcQ'
        gs = gc.open_by_key(year1)
        worksheet1 = gs.worksheet('Sheet1')
    
        records_data = worksheet1.get_all_records()
        if len(records_data)==0:
          res=df
        else:
          df2 = pd.DataFrame.from_dict(records_data)
          res = df2.set_index(['auid'])\
               .combine_first(df.set_index(['auid']))\
               .reset_index()
          
    
        gs.worksheet('Sheet1').clear()

        set_with_dataframe(worksheet=worksheet1, dataframe=res, include_index=False,include_column_header=True, resize=True)
        return render_template('success.html')

    with open('myfile.txt') as f:
        nn=f.readline()
    data=nn.split("-") 
    return render_template('transaction200.html',uid=data[0],name=data[1])

@app.route("/trans300",methods=['POST',"GET"]) 
def tran300():
    if(request.method=='POST'):
        with open('myfile.txt') as f:
            nn=f.readline()
        data=nn.split("-")
        tid=request.form.get('tid')
        file=request.files['file']
        filename=secure_filename(file.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir,app.config["FILE_UPLOADS"],data[0]+'.png'))
        cred = credentials.Certificate("./static/files/tidshots-firebase-adminsdk-psrzj-1c3853d0d8.json")
        initialize_app(cred, {'storageBucket': 'tidshots.appspot.com'})

        # Put your local file path 
        fileName = "./static/files/"+data[0]+'.png'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

        # Opt : if you want to make public access from the URL
        blob.make_public()

        file_path= blob.public_url
        data={'auid':[data[0]],'filepath':str(file_path),'amount':'300'}
        df=pd.DataFrame(data)
        scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials1 = Credentials.from_service_account_file('./static/files/woven-invention-377716-9c2ae2d0cfbe.json', scopes=scopes)
        gc = gspread.authorize(credentials1)
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        year1='1QTeoBawNK4PYxNiU7RybXUkl12Rnailbfm5-vD8wFcQ'
        gs = gc.open_by_key(year1)
        worksheet1 = gs.worksheet('Sheet1')
    
        records_data = worksheet1.get_all_records()
        if len(records_data)==0:
          res=df
        else:
          df2 = pd.DataFrame.from_dict(records_data)
          res = df2.set_index(['auid'])\
               .combine_first(df.set_index(['auid']))\
               .reset_index()
          
    
        gs.worksheet('Sheet1').clear()

        set_with_dataframe(worksheet=worksheet1, dataframe=res, include_index=False,include_column_header=True, resize=True)
        return render_template('success.html')
    with open('myfile.txt') as f:
        nn=f.readline()
    data=nn.split("-") 
    return render_template('transaction300.html',uid=data[0],name=data[1])

@app.route("/trans400",methods=['POST',"GET"]) 
def tran400():
    if(request.method=='POST'):
        with open('myfile.txt') as f:
            nn=f.readline()
        data=nn.split("-")
        tid=request.form.get('tid')
        file=request.files['file']
        filename=secure_filename(file.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir,app.config["FILE_UPLOADS"],data[0]+'.png'))
        cred = credentials.Certificate("./static/files/tidshots-firebase-adminsdk-psrzj-1c3853d0d8.json")
        initialize_app(cred, {'storageBucket': 'tidshots.appspot.com'})

        # Put your local file path 
        fileName = "./static/files/"+data[0]+'.png'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

        # Opt : if you want to make public access from the URL
        blob.make_public()

        file_path= blob.public_url
        data={'auid':[data[0]],'filepath':str(file_path),'amount':'400'}
        df=pd.DataFrame(data)
        scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials1 = Credentials.from_service_account_file('./static/files/woven-invention-377716-9c2ae2d0cfbe.json', scopes=scopes)
        gc = gspread.authorize(credentials1)
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        year1='1QTeoBawNK4PYxNiU7RybXUkl12Rnailbfm5-vD8wFcQ'
        gs = gc.open_by_key(year1)
        worksheet1 = gs.worksheet('Sheet1')
    
        records_data = worksheet1.get_all_records()
        if len(records_data)==0:
          res=df
        else:
          df2 = pd.DataFrame.from_dict(records_data)
          res = df2.set_index(['auid'])\
               .combine_first(df.set_index(['auid']))\
               .reset_index()
          
    
        gs.worksheet('Sheet1').clear()

        set_with_dataframe(worksheet=worksheet1, dataframe=res, include_index=False,include_column_header=True, resize=True)
        return render_template('success.html')

    with open('myfile.txt') as f:
        nn=f.readline()
    data=nn.split("-") 
    return render_template('transaction400.html',uid=data[0],name=data[1])


@app.route("/form",methods=['POST',"GET"]) 
def upload_image():
    if(request.method=='POST'):
        name=request.form.get('name')
        cname=request.form.get('college')
        mail=request.form.get('mail')
        mobile=request.form.get('mobile')
        workshop=request.form.get('workshop')
        payment=request.form.get('payment')
        tevent=request.form.getlist('tevent')
        ntevent=request.form.getlist('ntevent')
        ipl=request.form.get('ipl')
        print(tevent)
        print(workshop)
        print(ntevent)
        sum=0
        w=0
        if workshop!=None:
            w+=1
        sum=len(tevent)+len(ntevent)
        if len(tevent)>1:
            sum+=1
        if len(ntevent)>1:
            sum+=1

        print(sum)
        id=''
        id+=name[0:3]
        id+=cname[0:4]
        id+=mobile[-4:]
        id+='00'+str(sum)
        uid=id.upper()
        print(uid)
        print(w)
        file1 = open("myfile.txt","w")
        file1.write(uid+'-'+name)
        file1.close()
        data={'auid':[uid],'Name':[name],'College':[cname],'Workshop':[workshop],'Technical Events':[tevent],'Non Technical Events':[ntevent],'Payment Mode':[payment]}
        df=pd.DataFrame(data)
        scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file('./static/files/woven-invention-377716-9c2ae2d0cfbe.json', scopes=scopes)
        gc = gspread.authorize(credentials)
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        year1='1fpr1V1hRMTMWDRGSQ0FlxH7fvJK3fb3o1cGzg9E1grw'
        gs = gc.open_by_key(year1)
        worksheet1 = gs.worksheet('Sheet1')
    
        records_data = worksheet1.get_all_records()
        if len(records_data)==0:
          res=df
        else:
          df2 = pd.DataFrame.from_dict(records_data)
          res = df2.set_index(['auid'])\
               .combine_first(df.set_index(['auid']))\
               .reset_index()
          
    
        gs.worksheet('Sheet1').clear()

        set_with_dataframe(worksheet=worksheet1, dataframe=res, include_index=False,include_column_header=True, resize=True)
        if payment=='spot':
            return render_template('success.html')
        if payment=='online':
            if sum==1 and w==0:
                return render_template('payment100.html',uid=uid,name=name), {"Refresh": "120; url=/trans100"}
            if sum==0 and w==1:
                return render_template('payment200.html',uid=uid,name=name), {"Refresh": "120; url=/trans200"}
            if sum==1 and w==1:
                return render_template('payment300.html',uid=uid,name=name), {"Refresh": "120; url=/trans300"}
            if sum>1 and w==1:
                return render_template('payment400.html',uid=uid,name=name), {"Refresh": "120; url=/trans400"}
            if sum>1 and w==0:
                return render_template('payment200.html',uid=uid,name=name), {"Refresh": "120; url=/trans200"}
            
        return render_template('success.html')
    return render_template('form.html')

if __name__ == '__main__':
    app.run(port=5000)