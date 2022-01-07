#!/bin/bash -e

git checkout master
git fetch origin gh-pages

cd docs
gojekyll clean
gojekyll build
rm -rf ../../_site
cp -a _site ../../
cd ..

git checkout gh-pages
rm -rf *
cp -a ../_site/* .
git add -A
git commit -am 'Update'
git push origin gh-pages
