#!/usr/bin/env bash
script_dir=`dirname $0`
cd $script_dir
sudo pip install virtualenv
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
