#!/usr/bin/env bash
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : setup.sh
#   Created Time  : 2019-09-21 15:39
#   Last Modified : 2019-09-21 15:39
#   Describe      :
#
# ====================================================

function __abspath() {
    if [[ "${HOSTNAME}" == *c6* ]]; then
        /usr/bin/readlink -e -v "${BASH_SOURCE[0]}"
    else
        /usr/bin/realpath -L -P -e "$1"
    fi
}
MTSYS="$(dirname $(__abspath $0))"
# echo $MTSYS
# MTSYS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if ! [ -d "${MTSYS}"/bin ] 
then
    mkdir "${MTSYS}"/bin
fi

if [ -e "${MTSYS}"/bin/rm ] 
then
    /bin/rm -rf "${MTSYS}"/bin/rm
fi
ln -s  "${MTSYS}"/core/main.py "${MTSYS}"/bin/rm
export PATH="${MTSYS}/bin":$PATH
