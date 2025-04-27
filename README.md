# Project Report

##### Tools: Excel, Python, Power BI

##### Type: Data Cleaning, Data Analysis

## Table of Contents
1. [Home](#Project-Report)
2. [Background](#Background)
3. [Executive Summary](#Executive-Summary)
4. [Data Source](#Data-Source)
5. [Analysis](#Analysis-Insight-Deep-Dive)
6. [Recommendations](#Recommendations)
7. [Clarifying Questions, Assumptions, and Caveats](#Clarifying-Questions,-Assumptions,-and-Caveats)

## Background

This project analyzes student performance data to uncover trends in grading outcomes and evaluate the impact of specific math department policies. The main driving questions are:
- Is there a corrolation between group quiz and test score?
- Are retakes useful for improving student achievement?
- Is there a correlation between assignments turned in and test grades?
While home environment and parental involvement are known major factors in academic success, this analysis focuses on assessing whether internal department policies, like group quizzes and retakes, have a measurable effect on test performance.


## Executive Summary
This analysis reveals the following: 
1. Assignment completion rates and test scores show a weak negative corrolation (having missing assignments does not neccicarily mean a student will do poorly).
2. Participation in group quizzes shows no corrolation (many students do well on group quiz and not on the test and vice versa).
3. Retakes had a positive impact for many students, but the magnitude of improvement varied. Many students do not take advantage of retakes but of those who do, nearly 50% improve their scores by over 5%. 
The data structure was refined mid-project, which significantly improved the quality and clarity of the analysis.

## Data Source
Thee data used for this analysis consists of 70 students in Algebra 2. Data was cleaned and reformatted to the following: 
- student ID (fake)
- Gender
- Grade
- Assignment scores

#### Data cleaning and processing were performed using Excel and Python:
1. I used excel to clean the data. This was extreamly time consuming and overall, the data was not not "flexable" meaning I couldnt easily use different technologies. I used helper rows for calculations. It got the job done...
2. Next I wanted to use power BI but the current data structure was not compatible. With Python, I normalized the structure into 3 tables.
    - Assignment points Table: Assignment name, unit, category, points possible.
    - Student Data Table: Student ID, age, grade level, and course.
    - Assignemnt Data Table: Student ID, assignment name, score.
  This restructuring allowed for easier extraction of insight and trends. 


## Analysis Insight Deep-Dive

### 1

### 2



## Recommendations

Based on the exploratory analysis, the following preliminary recommendations can be made:
- 

## Clarifying Questions, Assumptions, and Caveats

### Assumptions:
- Assignment types and categorizations were accurately labeled after restructuring.
- Students put forth sincere effort on retakes and group quizzes.
- The dataset is complete and captures all assignments, tests, and retakes for the grading period.

### Questions for Stakeholders:
- 

### Missing Information:
- 


---
This report serves as an initial exploration of student performance data. Future analysis will include a Dashboard for quick and easy visual insights. with the hopes of the dashboard being realtime and aid teacher decision making. 
