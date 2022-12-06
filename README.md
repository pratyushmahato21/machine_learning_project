## Start Machine Learning Project

### Software and Account Requirements

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/doc)


Creating conda environment
```
conda create -p venv python==3.7 # (first time only)
```

Activate conda environment
```
conda activate venv/
```
OR
```
conda activate venv
```

Install packages
```
pip install -r requirements.txt
```

To add files to git
```
git add <file_name>
```
OR
```
git add .
```

> Note: to ignore file or folder, write name in .gitignore file

To check git status
```
git status
```

To check all versions maintained by git
```
git log
```

To create version/commit all changes in git
```
git commit -m "message"
```

To send all versions/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

to setup CI/CD pipeline in heroku we need 3 information

1. Heroku email
2. Heroku API key
3. Heroku app name


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: image_name for docker must be in lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running docker container
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

To install required libraries
```
python setup.py install
```