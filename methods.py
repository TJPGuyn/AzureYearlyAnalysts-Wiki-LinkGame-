import requests

s = requests.Session()
r = s.get("https://www.bbc.co.uk/news")
print(r.status_code)
html = (r.text)

heads = html.split('split__text">')
clean_heads = []
skipped = False
for h in heads:
  if skipped:
    i = h.index("</h")
    x = h[:i]
    if x not in clean_heads:
      clean_heads.append(x)
  else:
    skipped = True

for c in clean_heads:
  print(c)