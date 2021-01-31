import stashy
from authentication import *
from pprint import pprint

stash = stashy.connect(msbbURL, token=msbbToken)

# grab AWS project
aws = next((item for item in stash.projects.list() if item['key'] == 'AWS'))
stash.projects[aws].repos.list()

print("done")