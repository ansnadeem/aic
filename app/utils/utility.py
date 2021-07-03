import jwt
import time


def fetchTokenHeader(app_id, private_key):
    time_since_epoch_in_seconds = int(time.time())
    payload = {
      'iat': time_since_epoch_in_seconds,
      'exp': time_since_epoch_in_seconds + (10 * 60),
      'iss': app_id
    }
    jwt_encoded = jwt.encode(payload, private_key, algorithm='RS256')
    headers = {
          "Authorization": "Bearer {}".format(jwt_encoded),
          "Accept": "application/vnd.github.machine-man-preview+json"
     }
    return headers

def githubPostHeader(token):
    headers = {
        "Authorization": "token {}".format(token),
        "Accept": "application/vnd.github.machine-man-preview+json"
    }
    return headers