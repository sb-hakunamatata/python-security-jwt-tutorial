FROM public.ecr.aws/lambda/python:3.8

ADD configuration ./configuration
ADD controllers ./controllers
ADD models ./models
ADD config.ini ./
ADD app.py ./
ADD Pipfile ./

RUN pip install pipenv

# install depedencies in local folder only.
RUN export PIPENV_VENV_IN_PROJECT="enabled"

# create .venv for installing dependencies.
RUN mkdir .venv

RUN pipenv install

# this is mandatory. why ?
RUN cp -a .venv/lib/python3.8/site-packages/. ./

RUN ls -al

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
