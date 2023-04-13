###!/usr/bin/env python3
#creating reading from CSV

import csv

def create_csv_file():
    ### my records will be array of disconary 
    records = [
        
        {"id": '1', "firstname": 'dhinakaran', "lastname": 'guna', "age": '34'},
        {"id": '2', "firstname": 'dhina', "lastname": 'guna', "age": '33' },
        {"id": '3', "firstname": 'karan', "lastname": 'guna', "age": '35' },
        {"id": '4', "firstname": 'dk', "lastname": 'guna', "age": '36' },
        {"id": '5', "firstname": 'krupa', "lastname": 'guna', "age": '37' },
    ]
    
    csv_writer = csv.writer(open(records.csv, 'w'), delimiter=',')
    
    csv_writer.writerow(['id', 'firstname', 'lastname', 'age'])
    
    for i in records:
        csv_writer.writerow([i['id'], i['firstname'], i['lastname'],i['age']])

if __name__ == "__main__ ":
    
    create_csv_file()
    
    
    
    
    
    