#!/bin/sh -efuC

readonly NAME="$1"; shift
readonly TAG="$1"; shift

git tag "$NAME/$TAG" -s -m "$NAME/$TAG

X-gear-specsubst: name=$NAME" \
    "$@"
