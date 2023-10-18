
FROM continuumio/miniconda3:4.10.3
EXPOSE 80


# Accept a build-time variable.
# 'API' will be the default, if not set during the build process.
ARG RUN_MODE=API

# Set an environment variable based on the build-time variable.
ENV RUN_MODE_ENV=${RUN_MODE}

RUN pip install --upgrade pip==22.0.4
#RUN conda create -n geo-env geopandas=0.10.2 -c conda-forge
RUN conda clean --all
#RUN pip install api[all]==0.75.1 hypercorn[trio]==0.13.2 cloudevents==1.2.0 scikit-learn==1.0.2 psutil==5.9.0 graypy==2.1.0 python-dotenv==0.20.0
RUN pip cache purge

# Set a working directory
WORKDIR /app

#COPY ./src .

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge; exit 0

COPY ./src .
COPY ./setup.py .

#ENTRYPOINT ["hypercorn", "api/api:app", "-b", "0.0.0.0:80", "--worker-class", "trio"]

# Conditional ENTRYPOINT based on the build argument
ENTRYPOINT if [ "$RUN_MODE_ENV" = "API" ] ; then hypercorn api.api:app -b 0.0.0.0:80 --worker-class trio; else python main.py; fi