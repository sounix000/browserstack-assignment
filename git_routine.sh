# For trivial updates
asciidoctor README.adoc -o docs/index.html
git add --all
git commit -m "Update"
git push origin main