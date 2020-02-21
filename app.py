# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:42:03 2020

@author: Hetal
"""

from flask import Flask, escape, request
import json

app = Flask(__name__)

S_Id = 1
C_Id = 1
Students ={}
Classes = {}
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/students', methods =['POST'])
def store_student_details():
    global S_Id
    if request.method =='POST':
        student_name = request.json['name']
        student_id = S_Id
        Students[student_id] ={"id":student_id,"name": student_name}
        S_Id+=1
        return json.dumps(Students[student_id])

@app.route('/students/<int:id>', methods =['GET'])
def get_student_details(id):
    if request.method =='GET':
        if id in Students:
            return json.dumps(Students[id])
        else:
            return "Student not found"
    
@app.route('/classes', methods =['POST'])
def create_class():
    global C_Id
    if request.method =='POST':
        class_name = request.json['name']
        class_id = C_Id
        Classes[class_id] ={"id":class_id,"name": class_name,"students":[]}
        C_Id+=1
        return json.dumps(Classes[class_id])
    
@app.route('/classes/<int:id>', methods =['GET'])
def get_class_details(id):
    if request.method =='GET':
        if id in Classes:
            return json.dumps(Classes[id])
        else:
            return "Class not found"
    
@app.route('/classes/<int:id>', methods =['PATCH'])
def add_student(id):
    if request.method =='PATCH':
        if id in Classes:
            student_id = request.json["student_id"]
            if student_id in Students:
                Classes[id]["students"].append(Students[student_id])
                return json.dumps(Classes[id])
            else:
                return "Student not found"
        else:
            return "Class not found"