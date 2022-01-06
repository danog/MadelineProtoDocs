#!/bin/bash -e

cd docs
gojekyll clean
gojekyll build
rm -rf ../../_site
cp -a _site ../../
cd ..

git checkout gh-pages
rm -rf *
cp -a ../_site/* .
