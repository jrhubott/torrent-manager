#!/usr/bin/env sh
docker-compose build
docker run --rm -it jrhubott/torrent-manager --view --host=http://htpc.home.rhusoft.com:9091