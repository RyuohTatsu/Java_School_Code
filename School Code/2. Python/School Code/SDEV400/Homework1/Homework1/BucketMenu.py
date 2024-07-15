# Amazon S3 examples - Boto3 1.34.131 documentation. (n.d.). https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
# Note: Code snippets were used from the source above.
# @author Brian Walters
# AWS Code snippets used
# Written 26 June 2024
# SDEV 400 7980 Secure Programming in the Cloud (2245) - Spring 2024
# Profesor Matthew Taylor

import boto3
import random
import datetime
import logging  # Import the logging module
import os
from botocore.exceptions import ClientError
from create_bucket import create_bucket
from copy_object import copy_object
from delete_bucket import delete_bucket
from delete_object import delete_object
from put_object import put_object
from bucket_exists import bucket_exists
from BucketList import buckets
from upload_file import upload_file

def get_buckets():
    """Retrieves a list of S3 buckets for the user."""
    s3 = boto3.client('s3')
    try:
        response = s3.list_buckets()
        return response.get('Buckets', [])  # Return empty list if no buckets found
    except ClientError as e:
        logging.error(f"Error listing S3 buckets: {e}")
        return []  # Return empty list on error
    
def generate_random_suffix():
  """Generates a random 6-digit suffix for the bucket name."""
  return random.randint(100000, 999999)

def get_bucket_name():
  """Prompts user for first and last name, generates a random suffix, and returns the bucket name."""
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  suffix = generate_random_suffix()
  bucket_name = f"{first_name}{last_name}-{suffix}"
  return bucket_name

def get_user_input(prompt):
    """Gets user input for various options."""
    return input(prompt)

def main():
    s3 = boto3.client('s3')  # Create an S3 client
    buckets = get_buckets()  # Retrieve the list of buckets

    while True:
        print("\nS3 Menu:")
        print("a. Create Bucket")
        print("b. Put Object")
        print("c. Delete Object")
        print("d. Delete Bucket")
        print("e. Copy Object")
        print("f. Download Object")
        print("g. Exit")
        choice = get_user_input("Enter your choice (a-g): ").lower()

        if choice == 'a':
            # Get bucket name with user input and random suffix
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            suffix = generate_random_suffix()
            my_bucket_name = f"{first_name}{last_name}-{suffix}"

            try:
                create_bucket(my_bucket_name)
                print(f"Bucket '{my_bucket_name}' created successfully.")
            except ClientError as e:
                print(f"Error creating bucket: {e}")  # Handle specific errors if needed

        if choice == 'b':
            # Display S3 buckets before prompting for upload
            if buckets:
                print("\nYour S3 buckets:")
                for bucket in buckets:
                    print(bucket['Name'])
            else:
                print("You don't have any S3 buckets yet.")

            # Prompt user for the bucket name
            bucket_name = get_user_input("Enter the bucket name to upload to: ")

            # Check if the bucket exists
            if bucket_exists(bucket_name):
                # Prompt user for the file path
                filename = get_user_input("Enter the file path to upload: ")

                # Check if the file exists before upload (optional)
                if os.path.exists(filename):
                    # Upload the file using upload_file function
                    success = upload_file(filename, bucket_name)
                    if success:
                        print(f"File '{filename}' uploaded to bucket '{bucket_name}'.")
                    else:
                        print("Error uploading file. Check logs for details.")
                else:
                    print(f"Error: File '{filename}' does not exist.")
            else:
                print(f"The bucket '{bucket_name}' does not exist or you don't have permission to access it.")

        elif choice == 'c':
            # Display S3 buckets before prompting for upload
            if buckets:
                print("\nYour S3 buckets:")
                for bucket in buckets:
                    print(bucket['Name'])
            else:
                print("You don't have any S3 buckets yet.")
            # Prompt user for the object key within the bucket
            bucket_name = get_user_input("Enter bucket name: ")
            object_key = get_user_input("Enter object name to delete: ")
            # Confirmation for deletion
            confirmation = get_user_input(f"Are you sure you want to delete {object_key} from {bucket_name}? (y/N): ").lower()
            if confirmation == 'y':
                # Call delete_object function
                success = delete_object(bucket_name, object_key)
                if success:
                    print(f"Object {object_key} deleted from {bucket_name}")
                else:
                    print("Error deleting object.")
            else:
                print("Object deletion cancelled.")
        
        elif choice == 'd':
            # Display S3 buckets before prompting for upload
            if buckets:
                print("\nYour S3 buckets:")
                for bucket in buckets:
                    print(bucket['Name'])
            else:
                print("You don't have any S3 buckets yet.")
            # Prompt user for confirmation before deleting the bucket
            bucket_name = get_user_input("Enter bucket name to delete: ")
            confirmation = get_user_input(f"Are you sure you want to delete bucket {bucket_name}? (y/N): ").lower()
            if confirmation == 'y':
                # Ensure bucket is empty before deletion (check object count)
                try:
                    object_paginator = s3.get_paginator('list_objects_v2')
                    pages = object_paginator.paginate(Bucket=bucket_name)
                    object_count = 0
                    for page in pages:
                        object_count += len(page.get('Contents', []))
                    if object_count == 0:
                        # Call delete_bucket function
                        success = delete_bucket(bucket_name)
                        if success:
                            print(f"Bucket {bucket_name} deleted.")
                        else:
                            print("Error deleting bucket.")
                    else:
                        print(f"Bucket {bucket_name} is not empty. Please delete objects first.")
                except ClientError as e:
                    print(f"Error checking object count: {e}")
            else:
                print("Bucket deletion cancelled.")
        
        elif choice == 'e':
            # Display S3 buckets before prompting for upload
            if buckets:
                print("\nYour S3 buckets:")
                for bucket in buckets:
                    print(bucket['Name'])
            else:
                print("You don't have any S3 buckets yet.")
            # Prompt user for source and destination details
            src_bucket_name = get_user_input("Enter source bucket name: ")
            src_object_name = get_user_input("Enter source object name: ")
            dest_bucket_name = get_user_input("Enter destination bucket name: ")
            dest_object_name = get_user_input("Enter destination object name (optional, press Enter to use source key): ")
            if not dest_object_name:
                dest_object_name = src_object_name
            # Call copy_object function
            success = copy_object(src_bucket_name, src_object_name, dest_bucket_name, dest_object_name)
            if success:
                print(f"Object copied from {src_bucket_name}/{src_object_name} to {dest_bucket_name}/{dest_object_name}")
            else:
                print("Error copying object.")
        
        elif choice == 'f':
            # Display S3 buckets before prompting for upload
            if buckets:
                print("\nYour S3 buckets:")
                for bucket in buckets:
                    print(bucket['Name'])
            else:
                print("You don't have any S3 buckets yet.")
            # Prompt user for object key and download location
            bucket_name = get_user_input("Enter bucket name: ")
            object_key = get_user_input("Enter object name: ")
            local_filename = get_user_input("Enter local filename to save the downloaded object: ")
            # Download the object
            try:
                s3.download_file(Bucket=bucket_name, Key=object_key, LocalFilename=local_filename)
                print(f"Object downloaded to: {local_filename}")
            except ClientError as e:
                print(f"Error downloading object: {e}")
        
        elif choice == 'g':
            print(f"Exiting program. Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == '__main__':
    main()