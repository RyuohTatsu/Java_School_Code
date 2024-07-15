import boto3
from boto3.dynamodb.conditions import Attr
from courses_data import courses

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Select the DynamoDB table
table = dynamodb.Table('Courses')

def get_course_title(subject, catalog_nbr):
    response = table.scan(
        FilterExpression=Attr('Subject').eq(subject) & Attr('CatalogNbr').eq(catalog_nbr)
    )
    items = response.get('Items', [])
    if items:
        return items[0]['Title']
    return None

def main():
    print("Available courses:")
    for course in courses:
        print(f"Subject: {course['Subject']}, CatalogNbr: {course['CatalogNbr']}")

    while True:
        subject = input("Enter the Subject:\n").upper()
        catalog_nbr = input("Enter the CatalogNbr:\n").upper()

        if not subject or not catalog_nbr:
            print("Both Subject and CatalogNbr are required. Please try again.")
            continue

        title = get_course_title(subject, catalog_nbr)
        if title:
            print(f"The title of {subject} {catalog_nbr} is {title}.")
        else:
            print(f"No course found for {subject} {catalog_nbr}.")

        continue_search = input("Would you like to search for another title? (Y or N)\n").upper()
        if continue_search != 'Y':
            print("Thanks for using the Catalog Search program.")
            break

if __name__ == "__main__":
    main()
