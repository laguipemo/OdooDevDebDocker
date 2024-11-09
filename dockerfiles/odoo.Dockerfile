FROM odoo:16.0
USER root
RUN apt update && apt upgrade -y && apt install -y curl python3-pandas nano poppler-utils tesseract-ocr
COPY ./requirements.txt /requirements.txt
RUN python3 -m pip install -r /requirements.txt
RUN rm /requirements.txt