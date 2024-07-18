from bs4 import BeautifulSoup
import requests
import threading

urls = [
    'https://github.com/Vanraj8169/IELTS_Writing_Website',
    'https://github.com/100xDevs-hkirat/Week-2-Assignments',
    'https://chatgpt.com/c/fe1862c9-2547-4496-8be4-2238b31953c6'
]

def fetch_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_length = len(soup.text)
        print(f"Fetched: {content_length} characters from {url}")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
