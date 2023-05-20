# apiwithpython
api with python using fast api

# create a virtual env
python3 -m venv <name>

# use command pallete to choose the python interpreter ./venv/bin/python

# make sure command prompt also uses the same python interpreter (before running or downloading a lib)
source venv/bin/activate

# install the fastapi using below command. quotes is used to prevent zsh to misunderstand the command as fastapi[\all\]
pip install 'fastapi[api]' 

# use the below command to see what all packakges got installed
pip freeze

# use uvicorn as server and hit the localhost to see the api response. alternatively put /docs in the url to use ui based interaction
uvcorn main:app --reload