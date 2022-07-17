#!/bin/sh
mkdir -p /data/{geo,logs,cache}
mkdir -p /data/{geo,logs}
mkdir -p /data/attachments/{media,avatar,cache/metadata_thumbnails}
mkdir -p /data/attachments/media/{images,videos,audios,others}

if [ -f "$DJANGO_LOG_FILE" ]; then
    echo "$DJANGO_LOG_FILE exists."
else 
    touch $DJANGO_LOG_FILE
    echo "$DJANGO_LOG_FILE does not exist. created"
fi

./manage runserver --noreload --no-color 0.0.0.0:8000