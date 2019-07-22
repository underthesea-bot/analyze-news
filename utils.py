import json
import requests
import os

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
try:
    os.environ['GITBOT_USERNAME']
    os.environ['GITBOT_PASSWORD']
except:
    print('[ERROR] GITBOT_USERNAME and GITBOT_PASSWORD must be set')
    exit()
USERNAME = os.environ['GITBOT_USERNAME']
PASSWORD = os.environ['GITBOT_PASSWORD']

# The repository to add this issue to
REPO_OWNER = 'undertheseanlp'
REPO_NAME = 'resources'


class Repository:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name


class Github:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_issue(self, repository, title, body=None, assignee=None, milestone=None, labels=None):
        '''Create an issue on github.com using the given parameters.'''
        # Our url to create issues via POST
        url = 'https://api.github.com/repos/%s/%s/issues' % (repository.owner, repository.name)
        # Create an authenticated session to create the issue
        session = requests.Session()
        session.auth = (self.username, self.password)
        # Create our issue
        issue = {'title': title,
                 'body': body,
                 'assignee': assignee,
                 'milestone': milestone,
                 'labels': labels}
        # Add the issue to our repository
        r = session.post(url, json.dumps(issue))
        if r.status_code == 201:
            print('Successfully created Issue "%s"' % title)
        else:
            print('Could not create Issue "%s"' % title)
            print('Response:', r.content)

if __name__ == '__main__':
    repository = Repository(REPO_OWNER, REPO_NAME)
    github = Github(USERNAME, PASSWORD)
    github.create_issue(repository, 'Issue Title 3', 'Body text', assignee=None, labels=['data'])