FROM python:3.9

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /tmp
RUN ["chmod", "+x", "/tmp/entrypoint.sh"]

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
ENTRYPOINT [ "/tmp/entrypoint.sh" ]
