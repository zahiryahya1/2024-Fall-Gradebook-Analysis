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
The data used for this analysis consists of 70 students in Algebra 2. Data was cleaned and reformatted to the following: 
- student ID (fake)
- Gender
- Grade
- Assignment scores

#### Data cleaning and processing were performed using Excel and Python:
1. I used excel to clean the data. This was very time consuming and overall, the data was not "flexable" meaning it only worked for excel and not compatible with other tech tools. I applied a strategy of using a helper rows to perform calculations. It got the job done but again the process seemed messy. 

2. After my initial analysis, I wanted to use power BI to perform further analysis but the data structure was not compatible. I wrote a Python script to normalized the structure into 3 tables:
    - Assignment points Table: Assignment name, unit, category, points possible.
    - Student Data Table: Student ID, age, grade level, and course.
    - Assignemnt Data Table: Student ID, assignment name, score.
  This restructuring allowed for easier extraction of insight and trends via power BI. It also overall made the data easier to analyze. 


## Analysis Insight Deep-Dive

### 1. Group Quiz:
    
![alt text](/assets/images/avg_quiz_vs_test.jpg)

above is a scatter plot where each point respresents a student. 
- Comparing any group quiz and its corresponding unit test scores, you will see that there is no corrolation. I belive this is the case because students may get help or answers from their group members without knowing how to solve the problem. An observation I have noticed amungs kids is many students are looking to just complete the work and are not satisfied with understanding the solution. 

### 2. Missing Assignments:
    
![alt text](/assets/images/missing_assignment_vs_grade.jpg)

above is a scatter plot where each point represents a studnet. 
 - You maay have notice that there is a weak corrolation between the number of missing assignments and overall grade. It makes sense that students who practice will do well. However there are instances of students who complete practice assignments but under perform on the tests. There are 2 reasons that can explain this:
 - First, students can be getting a lot of support from a tutor or friends. This is not necessarily a bad thing, however some students dont know the difference between getting help and getting the steps by step solutions. 
- This leads to the Second reason, students copying unfaithfully. Again getting help or looking at the solutions can be a tool if used correctly but most students dont have the time, patients, or want to study the solution. 

### 3. Retake Analysis:
    
![alt text](/assets/images/retake_data_pie_chart.jpg)

above is a pie chart that looks at all retake scores and organizes scores based on level of improvement. In total, there were 70 retakes with 148 non retakes. 
- As you can see, just under 50% of students who retook scored over 5% better.
A large percent of students did not improve. In order to retake, students must complete test corrections and 1 additional assignment of their choice. These requiremnts discurage non serious students from retake and also helps students learn from their mistakes and study a bit. Unfortinatly, not all students who retake are learning from their mistake. Students lack study, review, and self analysis skills. Unfortinatly there is not much time in the classroom for these, but something teachers should consider.
  
The table below breaks up the retake data by unit and improvement level. 

|  Unit  |  Num of Retake  | No Growth  | Little  Growth | Meaningful Growth  | Large Growth  |
|--------|-----------------|------------|----------------|--------------------|---------------|
|  Unit 1|  13             | 3          | 1              | 4                  | 4             |
|  Unit 2|  20             | 9          | 4              | 6                  | 1             |
|  Unit 3|  37             | 14         | 6              | 8                  | 9             |

- Final grade before and after retake. 

![alt text](/assets/images/without_vs_with_retake_bar.jpg)

Comparing students final grades before and after retakes, you can see that students grades have increased. Some more than others. 

  Average Final Grade Excluding Retakes: 74.22%	
  Average Final Grade Including Retakes: 75.32%

Retakes Improved the class average by 1%

### 4. Finals 
- finals score vs average test score. What is the delta? (did students do better on the final then usual?)
- test + final % score vs final grade.  What is the delta? (did practice assignments hurt grade?)
- practice hurt 5 students in particular where they dropped form a - to a plus.
- practrice helped 10 students go from a - to a plus. 

insert mardown table: practice helped 45 students, hurt 25 students. 

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
