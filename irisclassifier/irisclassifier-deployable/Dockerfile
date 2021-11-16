FROM bentoml/model-server:0.13.1-py38

# the env var $PORT is required by heroku container runtime
ENV PORT 8080
EXPOSE $PORT

RUN apt-get update --fix-missing --allow-releaseinfo-change &&     apt-get install -y nginx &&     apt-get clean

# gevent required by AWS Sagemaker
RUN pip install gevent>=20.9.0

# copy over model files
COPY . /bento
WORKDIR /bento

RUN if [ -f /bento/bentoml-init.sh ]; then bash -c /bento/bentoml-init.sh; fi

ENV PATH="/bento:$PATH"
