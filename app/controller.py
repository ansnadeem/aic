from flask import request
from flask import Flask
from flask import render_template
from engine import AICEngine
from dotenv import dotenv_values
from dotenv import load_dotenv
from utils import constants

aicEngine = None

def initalize():
     global aicEngine
     global app

     load_dotenv()
     config = dotenv_values(constants.DOT_ENV_PATH)
     aicEngine =  AICEngine(config)
     app = Flask(__name__, template_folder=constants.TEMPLATES_FOLDER)

initalize()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/githublistener', methods = ['POST'])
def listenAPI():
     global aicEngine          
     response = {}
     response[constants.RESPONSE_RESULT] = None
     response[constants.RESPONSE_STATUS] = constants.HTTP_OK
     data = request.get_json(True)
     if (data[constants.GITHUB_ACTION] == constants.OPEN_STATUS):
          issueText = data[constants.ISSUE][constants.TITLE] + " " + data[constants.ISSUE][constants.BODY]
          predicted_labels = aicEngine.predict(issueText)

          issue_url = data[constants.ISSUE][constants.URL]
          installation_id = data[constants.INSTALLATION][constants.ID]
          aicEngine.assign(predicted_labels, installation_id, issue_url)

          response[constants.RESPONSE_RESULT] = predicted_labels
     return response