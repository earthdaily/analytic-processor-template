
FROM continuumio/miniconda3:4.10.3
EXPOSE 80

RUN pip install --upgrade pip==22.0.4
#RUN conda create -n geo-env geopandas=0.10.2 -c conda-forge
RUN conda clean --all
#RUN pip install api[all]==0.75.1 hypercorn[trio]==0.13.2 cloudevents==1.2.0 scikit-learn==1.0.2 psutil==5.9.0 graypy==2.1.0 python-dotenv==0.20.0
RUN pip cache purge

COPY ./src .

ENTRYPOINT ["hypercorn", "cloudevents_endpoint:app", "-b", "0.0.0.0:80", "--worker-class", "trio"]
#COPY ./requirements-conda.txt .
#RUN conda install -c conda-forge --file requirements-conda.txt
#RUN conda clean --all

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge; exit 0

COPY ./src .
COPY ./setup.py .
