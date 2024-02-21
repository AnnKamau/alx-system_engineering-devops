#!/usr/bin/python3
""" Exports api to csv"""

import csv
import requests
import sys

if __name__ == '__main__':
  user = sys.argv[1]
  url_user = 'https://jsonplaceholder.typicode.com/users/' + user
  res = requests.get(url_user)
  """ANY NAME"""
  user_name = res.json().get('username')
  task = url_user + '/todos'
  res = requests.get(task)
  tasks = res.json()
  
  with open('{}.csv' .format(user), 'w') as csvfile:
    for task in tasks:
      completed = task.get('completed')
      """COMPLETE"""
      title_task = task.get('title')
      """DONE"""
      csvfile.write('"{}","{}","{}","{}"\n'.format(
      user, user_name, completed, title_task))
