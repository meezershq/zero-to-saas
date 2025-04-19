import sys, requests
from bs4 import BeautifulSoup

url = sys.argv[1]
html = requests.get(url, timeout=10).text

soup = BeautifulSoup(html, "html.parser")

# remove scripts, styles, and other non-content tags
for tag in soup(["script", "style", "noscript"]):
    tag.decompose()

# get visible text
clean_text = soup.get_text(separator="\n", strip=True)

# save to file
filename = url.split("/")[-1] or "output"
with open(f"{filename}.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print(f"Saved {filename}.txt")
