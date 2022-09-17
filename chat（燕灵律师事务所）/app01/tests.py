from django.test import TestCase

# Create your tests here.
import re

a = 'http://127.0.0.1:8000/index/?tel=13770855741'

print(re.findall('\w+', a))