# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:24:03 2026

@author: nidum
"""
import datetime
#Used to work with dates and times

def exam_subjects(): #To get subjects and exam dates from user
    subjects={} #Dictionary to store subject name as key and exam date as value
    
    n=int(input("How many subjects: "))
    for i in range(n):
        name=input(f"\nEnter subject {i+1} name: ")
        date1=input("Enter exam date (DD-MM-YYYY): ")
        exam_date=datetime.datetime.strptime(date1, "%d-%m-%Y").date() #Convert str to actual date object
        subjects[name]=exam_date #Store in dictionary
    return subjects

def study_schedule(subjects): #To calculate daily study hours w.r.t urgency
    today=datetime.date.today() #For getting today's date
    schedule={} #Dictionary for storing study schedule
    
    for subject,exam_date in subjects.items():
        days_left=(exam_date-today).days #No. of days to exam
        if days_left<=0:
            print(f"\nEXAM FOR {subject} IS TODAY OR ALREADY OVER!")
            continue #Skipping that subject
        
        # Basic urgency formula:
        # More days left → fewer hours per day
        # Fewer days left → more hours per day
        hours_a_day = round(2 + (30 / days_left), 1)
        
        schedule[subject]=hours_a_day #To store calculated hours
    return schedule

def save_schedule(schedule): #Function to save study plan to text file
    with open("study_schedule.txt", "w") as file:
        file.write("****DAILY STUDY PLAN****\n\n") #For writing heading
        for subject, hours in schedule.items(): #For writing each subject and item required
            file.write(f"{subject}: {hours} hours per day\n")
    print("\n Schedule saved to study_schedule.txt")
    
def main(): #Controls program flow
        print("Study planner\n")
        subjects=exam_subjects() #Get subjects from user
        schedule=study_schedule(subjects) #Generate schedule
        print("\n****YOUR DAILY STUDY PLAN****")
        for subject, hours in schedule.items():
            print(f"{subject}: {hours} hours per day")
            
        save_schedule(schedule) #Save to file
        
if __name__=="__main__": #This makes sure that program runs only when directly executed
    main()
        
        
