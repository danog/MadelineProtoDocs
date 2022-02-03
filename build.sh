#!/bin/bash -e

git checkout master
git fetch origin gh-pages

which gojekyll || {
	mkdir /tmp/bin -p
	wget https://github.com/danog/gojekyll/releases/latest/download/gojekyll-amd64 -O /tmp/bin/gojekyll
	chmod +x /tmp/bin/gojekyll
	export PATH="$PATH:/tmp/bin"
}

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
