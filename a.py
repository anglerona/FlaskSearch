# Python Flask Search Server By: Angelina

import json
from flask import Flask
from flask import request

with open('scholarships.json', 'r') as m:
  data= json.load(m)

app = Flask(__name__)

@app.route('/scholarships/')


def show():

  q = request.args.get('q', '')
  results = []

  for i in data:
    if checkString(i,q):
      results.append(i)

  return {
        "query": q,
        "results": results
    }


# recursively checks dictionary to see if the valaue contains the search string
def checkString(dictionary, string):
  for k, v in dictionary.items():
    if isinstance(v, dict):
      if checkString(v, string):
        return True 
    elif v == None:
      continue;
    elif string in str(v):
      return True
  
  return False

# python3 -m flask run -p 8000
# if running through Terminal
if __name__ == '__main__':
  app.run(host='127.0.0.1',port=8000,debug=True)
    
    
