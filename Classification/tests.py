from django.test import TestCase

# Create your tests here.
import json

with open("./scores.json") as fp:
    dictionary = json.load(fp)



