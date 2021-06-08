FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /working-dir
COPY requirements/common.txt /working-dir/requirements/common.txt
COPY requirements/dev.txt /working-dir/requirements/requirements.txt
RUN pip install -r requirements/requirements.txt
COPY . /working-dir/
EXPOSE 8000 5432
#RUN DATABASE_URL='' python manage.py runserver
#ENV UWSGI_WSGI_FILE=eshipping/wsgi.py
RUN python manage.py migrate
#CMD python manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]