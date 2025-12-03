# School Supply Order Tracking – Logic Challenge

### Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# -----------------------------------------------------------------------------------------------------------------------------

### Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# -----------------------------------------------------------------------------------------------------------------------------

### Student Tasks (No Coding – Logic Only)

# ### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested
name = ["Olivia", "Gali", "Viviana"]
print(name)
item_request = ["Pencils", "Markers", "color pencils"]
print(item_request)
quantity = [2, 4, 6]
print(quantity)
# -----------------------------------------------------------------------------------------------------------------------------

# ## 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
print(name[0])
# - Identify the **last student’s requested item only**
print(item_request[2])
# -----------------------------------------------------------------------------------------------------------------------------

# ## 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.
print(quantity)
# -----------------------------------------------------------------------------------------------------------------------------

# ## 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
if any(quantity) > 5:
    print("Large order detected!")
    # - Otherwise label the order:
    #   “Orders within normal limits.”
else:
   print("Orders within normal limits.")
# -----------------------------------------------------------------------------------------------------------------------------

# ## 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.
print(quantity)

# -----------------------------------------------------------------------------------------------------------------------------


# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

classrooms = ((Classroom_1: 8, 12, 5),  
              (Classroom_2: 7, 3, 9),
              (Classroom_3: 10, 6, 4))

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?
# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**

# -----------------------------------------------------------------------------------------------------------------------------

# ## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# -----------------------------------------------------------------------------------------------------------------------------

# ## Submission Requirements
# - All answers must be written in words and/or tables.
# - No programming code may be used.
# - Show clear reasoning for each response.

# -----------------------------------------------------------------------------------------------------------------------------

# ## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# -----------------------------------------------------------------------------------------------------------------------------

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  
