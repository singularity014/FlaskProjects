import urllib.request
from flask import Flask


fname = r"C:\Users\User\Documents\UipathDocs\GE\SurveyForm.html"
HtmlFile = open(fname, 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)