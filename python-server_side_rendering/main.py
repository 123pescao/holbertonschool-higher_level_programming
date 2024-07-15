import os
from task_00_intro import generate_invitations

template_path = 'template.txt'

print("Current Working Directory:", os.getcwd())

if not os.path.exists(template_path):
    print(f"Error: {template_path} not found.")
else:
    # Read the template from a file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
