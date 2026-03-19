# Write a Python program to make a request to a web page, and test the status code, and display the HTML code of the specified web page.
# Sample Output:
# Web page status: <Response [200]>
# HTML code of the above web page:
# <!doctype html>
# <html>
# <head>
# <title>Example Domain</title>
# <meta charset="utf-8" />
# <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
# <meta name="viewport" content="width=device-width, initial-scale=1" />
# </head>
# <body>
# <div>
# <h1>Example Domain</h1>
# <p>This domain is for use in illustrative examples in documents. You may use this
# domain in literature without prior coordination or asking for permission.</p>
# <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>

import requests

url = input()

response = requests.get(url)

print("Web page status:", response)
print("HTML code of the above web page:")
print(response.text)