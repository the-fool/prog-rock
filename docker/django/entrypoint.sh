#!/bin/bash
set -e
cmd="$@"

export REDIS_URL=redis://redis:6379

exec $cmd
