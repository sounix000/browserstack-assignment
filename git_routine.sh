# Run this script for trivial updates

# Build documentation
cp -r images/ docs/
asciidoctor README.adoc -o docs/index.html
asciidoctor docs/doc-analysis.adoc -o docs/doc-analysis.html

# Push to remote Git repository
git add --all
git commit -m "Update"
git push origin main