#!/usr/bin/env bash
set -e

echo "Running Production Server"
exec celery -A demo worker -l info

