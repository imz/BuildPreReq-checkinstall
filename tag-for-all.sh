#!/bin/sh -efuC

readonly TAG="$1"; shift

for n in \
    apt-BuildPreReq-basic-checkinstall \
    apt-BuildPreReq-checkinstall \
    apt-BuildPreReq-xxtra-heavy-load-checkinstall \
    apt-BuildPreReq-under-pkdirect-checkinstall \
    rpm-BuildPreReq-checkinstall \

do
    ./tag-for-name.sh "$n" "$TAG" "$@"
done
