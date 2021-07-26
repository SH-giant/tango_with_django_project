from django.test import TestCase
import os

# Create your tests here.


project_base_dir = os.getcwd()
print(project_base_dir)
templates_dir = os.path.join(project_base_dir, '../templates')
print(templates_dir)
rango_templates_dir = os.path.join(templates_dir, '')
print(rango_templates_dir)
