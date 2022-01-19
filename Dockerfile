FROM python:3
WORKDIR /usr/src/app
ENV path_to_directory "/mnt/shared_from_host"
COPY . .
CMD ["manage.py"]
ENTRYPOINT ["python3"] 
