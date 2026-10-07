import sys, base64
from google import genai
client = genai.Client()
r = client.interactions.create(model="gemini-3.1-flash-image", input=sys.argv[1])
open(sys.argv[2], "wb").write(base64.b64decode(r.output_image.data))
