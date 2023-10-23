
FROM continuumio/miniconda3:4.10.3
EXPOSE 80

RUN pip install --upgrade pip==22.0.4
RUN conda clean --all
RUN pip cache purge

# Set a working directory
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge; exit 0

COPY ./src .
#COPY .env .

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
