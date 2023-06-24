#!/bin/bash
cd src
celery -A core worker -B -l INFO