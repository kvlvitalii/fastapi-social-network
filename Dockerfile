FROM alpine:3.13.5


WORKDIR /app

RUN apk update && \
    apk add --no-cache bash \
    make automake gcc subversion python3-dev \
    musl-dev libffi-dev openssl-dev \
    curl dpkg \
    --no-cache jpeg-dev zlib-dev zlib \
    cairo \
    cairo-dev pango-dev \
    openssl-dev rust tcl-dev tiff-dev tk-dev \
    cargo freetype-dev gdk-pixbuf-dev \
    jpeg-dev lcms2-dev  openjpeg-dev poppler-utils py-cffi && \
    apk add --update py3-pip

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --ignore-installed

COPY . .
