#!/bin/bash -e

wget https://go.dev/dl/go1.17.5.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.17.5.linux-amd64.tar.gz

export PATH=/usr/local/go/bin:$PATH

go version

cd docs
go get github.com/danog/gojekyll
gem install rouge
gojekyll clean
gojekyll build
