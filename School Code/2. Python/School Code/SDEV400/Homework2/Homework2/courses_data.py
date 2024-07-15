import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Select the DynamoDB table
table = dynamodb.Table('Courses')

# Sample course data
courses = [
    {'CourseID': '001', 'Subject': 'SDEV', 'CatalogNbr': '300', 'Title': 'Building Secure Python Applications', 'NumCredits': 3},
    {'CourseID': '002', 'Subject': 'SDEV', 'CatalogNbr': '400', 'Title': 'Secure Programming in the Cloud', 'NumCredits': 3},
    {'CourseID': '003', 'Subject': 'CS', 'CatalogNbr': '101', 'Title': 'Introduction to Computer Science', 'NumCredits': 4},
    {'CourseID': '004', 'Subject': 'CS', 'CatalogNbr': '102', 'Title': 'Data Structures and Algorithms', 'NumCredits': 4},
    {'CourseID': '005', 'Subject': 'CS', 'CatalogNbr': '201', 'Title': 'Operating Systems', 'NumCredits': 4},
    {'CourseID': '006', 'Subject': 'CS', 'CatalogNbr': '202', 'Title': 'Computer Networks', 'NumCredits': 4},
    {'CourseID': '007', 'Subject': 'IT', 'CatalogNbr': '301', 'Title': 'Cybersecurity Fundamentals', 'NumCredits': 3},
    {'CourseID': '008', 'Subject': 'IT', 'CatalogNbr': '302', 'Title': 'Database Management Systems', 'NumCredits': 3},
    {'CourseID': '009', 'Subject': 'IT', 'CatalogNbr': '401', 'Title': 'Cloud Computing', 'NumCredits': 3},
    {'CourseID': '010', 'Subject': 'IT', 'CatalogNbr': '402', 'Title': 'IT Project Management', 'NumCredits': 3}
]

# Required attributes
required_attributes = ['CourseID', 'Subject', 'CatalogNbr', 'Title', 'NumCredits']

# Insert course data into the table with validation
for course in courses:
    if all(attr in course for attr in required_attributes):
        table.put_item(Item=course)
        print(f"Inserted course: {course['CourseID']}")
    else:
        print(f"Missing attributes in course: {course['CourseID']}")

print("Courses inserted successfully!")
