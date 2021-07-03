# GitHub App Source

  If you are looking forward to replicate a server for the app, the following are a few instructions that need to be followed.
  
  - The '.env' file in this directory is a sample file and requires actual GitHub application ID and path to PEM key in the file
  - The model directory is uploaded as a sample and must contain the pre-trained model that is going to be used for prediction tasks
  
  
  After following the above instructions, the Flask app can be run by executing the 'controller.py' file. 
  The app runs as an API endpoint that listens to requests from github at '<hostname>/githublistener' by default.
  
