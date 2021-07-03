from simpletransformers.classification import MultiLabelClassificationModel
import requests
from utils import constants
from utils import utility

class AICEngine:
     def __init__(self, config):
          self.appID = config[constants.GIT_APP_ENV_NAME]
          self.pemKey = open(config[constants.PEM_KEY_FILE_ENV_NAME], 'rt').read()
          self.model = MultiLabelClassificationModel(constants.ROBERTA, constants.TRAINED_MODEL_PATH, use_cuda=False)

     def predict(self, text):
          feature = text.lower()
          prediction = self.model.predict(feature)
          result = {}
          result[constants.RESULT_LABELS] = prediction[0][0]
          result[constants.RESULT_THRESHOLD] = prediction[1][0].tolist()
          return result

     def assign(self, prediction, installationID, issueURL):
          resp = requests.post(
               constants.GITHUB_ACCESS_TOKEN_LINK.format(installationID),
               headers = utility.fetchTokenHeader(self.appID, self.pemKey)
          )
          token = resp.json()[constants.TOKEN]
          label_url = issueURL + constants.LABEL_LINK_SUFFIX
          predicted_label_names = []

          for i in range(0,len(constants.RESULT_MASK_ORDER)):
               if (prediction[constants.RESULT_LABELS][i] == 1):
                    predicted_label_names.append(constants.RESULT_MASK_ORDER[i])
          resp = requests.post(
               label_url,
               json=predicted_label_names,
               headers=utility.githubPostHeader(token)
          )