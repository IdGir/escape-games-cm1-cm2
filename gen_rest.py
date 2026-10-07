import sys, os, base64, requests
r = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent",
    headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"], "Content-Type": "application/json"},
    json={"contents": [{"parts": [{"text": sys.argv[1]}]}]},
)
print(r.status_code)
j = r.json()
for p in j.get("candidates", [{}])[0].get("content", {}).get("parts", []):
    d = p.get("inlineData") or p.get("inline_data")
    if d:
        open(sys.argv[2], "wb").write(base64.b64decode(d["data"]))
        print("OK ->", sys.argv[2])
        break
else:
    print(j)
