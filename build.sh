#!/bin/bash -e

cd docs
go get github.com/danog/gojekyll
gem install rouge
gojekyll clean
gojekyll build
