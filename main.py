import stashy
from authentication import *
from pprint import pprint

stash = stashy.connect(msbbURL, token=msbbToken)

# grab AWS project
aws = next((item for item in stash.projects.list() if item['key'] == 'AWS'))
aws_repos = stash.projects[aws.get('key')].repos.list()

#i'm only intrested in two repos (for now)



