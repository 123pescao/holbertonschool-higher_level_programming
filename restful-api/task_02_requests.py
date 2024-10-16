#!/usr/bin/python3
"""Script fetches posts from JSONPlaceholder API"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    posts = []
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    #If response successful, process data and parse JSON into python
    if response.status_code == 200:
        posts = response.json()
    #Loop through posts and print each post
    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    posts = []
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    #If request successful, parse JSON in python
    if response.status_code == 200:
        posts = response.json()

    #Open csv file in write mode
    with open('posts.csv', mode='w', newline='') as j:
    #Create a writer object and write header rows
        writer = csv.DictWriter(j, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
    #write each post as a row
        for post in posts:
            writer.writerow({'id': post['id'],
                        'title': post['title'],
                        'body': post['body']})

    print("Posts have been saved to posts.csv")
