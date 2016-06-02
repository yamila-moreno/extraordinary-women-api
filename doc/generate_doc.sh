#!/bin/bash
echo "Remember to execute generate-doc with the server started, and the database clean with the initial fixtures"
echo ""

echo "Generating snippets"

rm snippets/*.json.adoc
rm snippets/payloads/*.json.adoc

pushd ../scripts
for f in `ls *.sh`; do
  filename=$(basename "$f")
  extension="${filename##*.}"
  filename="${filename%.*}"
  adoc="../doc/snippets/$filename.json.adoc"
  echo "... $filename"

  echo "[source,json]" > $adoc
  echo "`ls $adoc`"
  echo "----" >> $adoc
  bash $f >> $adoc 2>/dev/null
  echo "----" >> $adoc
done
popd

for f in `ls ../scripts/payloads/*.sh`; do
  filename=$(basename "$f")
  extension="${filename##*.}"
  filename="${filename%.*}"
  adoc="snippets/payloads/$filename.json.adoc"
  echo "[source,json]" > $adoc
  echo "----" >> $adoc
  cat $f >> $adoc
  echo "----" >> $adoc
done

asciidoctor index.adoc

echo "Done!"
