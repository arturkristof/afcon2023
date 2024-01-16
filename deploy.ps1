py ./processing.py
npm run build
git add ./dist -f
git commit -m "Next deploy"
git subtree push --prefix dist origin gh-pages