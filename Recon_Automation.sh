#!/bin/bash

domain=$1
threads=$2

python3 ~/PycharmProjects/subdomain_finder.py $domain $threads
python3 ~/PycharmProjects/fast_dirbuster.py http://$domain $threads .php
python3 ~/PycharmProjects/web_crawler.py $domain
python3 ~/PycharmProjects/Web_vulnerability_scanner.py $domain
