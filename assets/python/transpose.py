import csv

#algebra 2 transpose and reformate data

# Define the input and output file paths
input_file = "alg2_raw_data.csv"  # Replace with your input file path
output_file = "alg2_out_data.csv"  # Replace with your desired output file path

# Read the input file and process the data
with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    # Define the new header for the transposed file
    fieldnames = ["ID (fake)", "Subject", "Topic", "Assignment Type", "Assignment", "Raw Score"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    subject = "Algebra 2"
    topic = ""

    # Process each row in the input file
    for row in reader:
        
        student_name = row["ID (fake)"] # or should it be row[0]
        for key, value in row.items():
            
            if key.lower() != "id (fake)" and key.lower() != "gender" and key.lower() != "grade_lvl":  # Skip the "student name" column
                    
                # Determine assignment type (e.g., "Practice" or "Test") and title
                assignment_title = key.lower()
                
                # separate the assignments into 3 different categories
                if "practice" in assignment_title:
                    assignment_type = "Practice"
                elif "test" in assignment_title:
                    assignment_type =  "Test"
                elif "final" in assignment_title:
                    assignment_type = "Final"
                else:
                    assignment_type = "NA"
                    
                # group assignments by unit
                if "1." in assignment_title or "unit 1" in assignment_title:
                    topic = "Unit 1"
                elif "2." in assignment_title or "unit 2" in assignment_title:
                    topic = "Unit 2"
                elif "3." in assignment_title or "unit 3" in assignment_title:
                    topic = "Unit 3"
                elif "final" in assignment_title:
                    topic = "Final"
                else:
                    topic = "NA"
                    
                    
                # Write the new row to the output file
                writer.writerow({
                    "ID (fake)": student_name,
                    "Subject": subject,
                    "Topic": topic,
                    "Assignment Type": assignment_type,
                    "Assignment": assignment_title,
                    "Raw Score": value
                })

print(f"Algebra Data has been transposed and saved to {output_file}.")




#geometry Traspose and reformate data

# Define the input and output file paths
input_file = "geo_raw_data.csv"  # Replace with your input file path
output_file = "geo_out_data.csv"  # Replace with your desired output file path

# Read the input file and process the data
with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    # Define the new header for the transposed file
    fieldnames = ["ID (fake)", "Subject", "Topic", "Assignment Type", "Assignment", "Raw Score"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    subject = "Geometry"
    topic = ""

    # Process each row in the input file
    for row in reader:
        
        student_name = row["ID (fake)"] # or should it be row[0]
        for key, value in row.items():
            
            if key.lower() != "id (fake)" and key.lower() != "gender" and key.lower() != "grade_lvl":  # Skip the "student name" column
                    
                # Determine assignment type (e.g., "Practice" or "Test")
                assignment_title = key.lower()
                
                # separate the assignments into 3 different categories
                if "practice" in assignment_title:
                    assignment_type = "Practice"
                elif "test" in assignment_title:
                    assignment_type =  "Test"
                elif "final" in assignment_title:
                    assignment_type = "Final"
                else:
                    assignment_type = "NA"
                    
                # group assignments by unit
                if "unit 1" in assignment_title or "unit 1" in assignment_title:
                    topic = "Unit 1"
                elif "unit 2" in assignment_title or "unit 2" in assignment_title:
                    topic = "Unit 2"
                elif "unit 3" in assignment_title or "unit 3" in assignment_title:
                    topic = "Unit 3"
                elif "final" in assignment_title:
                    topic = "Final"
                else:
                    topic = "NA"
                    
                    
                # Write the new row to the output file
                writer.writerow({
                    "ID (fake)": student_name,
                    "Subject": subject,
                    "Topic": topic,
                    "Assignment Type": assignment_type,
                    "Assignment": assignment_title,
                    "Raw Score": value
                })

print(f"Geometry Data has been transposed and saved to {output_file}.")