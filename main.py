import stashy
from authentication import *
from pprint import pprint

stash = stashy.connect(msbbURL, token=msbbToken)
pprint(stash.projects.list())