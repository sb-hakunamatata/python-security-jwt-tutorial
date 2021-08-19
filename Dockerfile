FROM public.ecr.aws/lambda/python:3.8 AS builder

RUN pip install pipenv
# create .venv for installing dependencies.
RUN mkdir .venv

ADD Pipfile ./
ADD Pipfile.lock ./

# install depedencies in local folder only.
RUN export PIPENV_VENV_IN_PROJECT="enabled"

RUN pipenv install

# this is mandatory. why ?
RUN cp -a .venv/lib/python3.8/site-packages/. /dependencies

FROM public.ecr.aws/lambda/python:3.8
 #seocond mahcine.
COPY --from=builder /dependencies ./
ADD configuration ./configuration
ADD controllers ./controllers
ADD models ./models
ADD config.ini ./
ADD app.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
