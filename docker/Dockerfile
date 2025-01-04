FROM python:3.12-slim

# WORKDIR /Users/zhengnaigong/Documents/mnist-fastapi-docker/app
WORKDIR /app

# declare an arg
ARG DISABLE_SSL_FOR_PIP

# COPY requirements.txt .
COPY docker/requirements.txt requirements.txt

# If this arg is set to 1, then disable the SSL check. Mainly for Xin
RUN \
    if [ "${DISABLE_SSL_FOR_PIP}" = "1" ] ; \
        then echo "Disabling SSL checks for pip" ; \
        pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org" && pip config set global.timeout 900 ; \
    fi \ 
    && pip install -r requirements.txt
COPY . .


EXPOSE 12347

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "12347"]
