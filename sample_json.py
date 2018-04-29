import json

data = {
    "title":"JSONサンプル",
    "date":"2018.04.29",
    "items":[
        {
            "title": "タイトル1",
            "contents":"内容1"
        },
        {
            "title":"タイトル2",
            "contents":"内容2"
        }
    ]
}

save_path = "sample.json"
with open(save_path, "w") as outfile:
    json.dump(data, outfile, ensure_ascii=False)

json_str = json.dumps(data)
print(json_str)
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
