PAYLOAD=$(<payloads/add-woman.sh)

curl -vs -X POST -H "Content-type: application/json" --data "$PAYLOAD" http://localhost:8000/extraordinary_women | python -m json.tool
