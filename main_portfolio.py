import requests
from send_email import send_email

# Make topics more dynamic
topic = "tesla"

api_key = ""
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&" \
      "from=2023-11-25&sortBy=publishedAt&" \
      "apiKey=" \
      "language=en"

# Make requests
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200 :
    # Get a dictionary with data
    content = response.json()

    # Access the articles title & description for 20 articles
    body = ""
    for article in content["articles"][:20]:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")

        if title:
            body += f"{title}\n"

        if description:
            body += f"{description}\n"

        if url:
            body += f"{url}\n\n"

    subject = "Today's News"
    body = body.encode("utf-8")
    send_email(subject = subject, message=body)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


