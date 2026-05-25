import requests
from bs4 import BeautifulSoup

def scan_website(url):

    vulnerabilities = []

    try:

        # ADD HTTPS IF USER DOESN'T ENTER IT

        if not url.startswith("http://") and not url.startswith("https://"):

            url = "https://" + url

        # SEND REQUEST

        response = requests.get(url, timeout=10)

        # CHECK STATUS

        if response.status_code == 200:

            vulnerabilities.append(
                f"Website reachable - Status Code: {response.status_code}"
            )

        # CHECK SECURITY HEADERS

        headers = response.headers

        security_headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-XSS-Protection"
        ]

        for header in security_headers:

            if header not in headers:

                vulnerabilities.append(
                    f"Missing Security Header: {header}"
                )

        # FIND FORMS

        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        vulnerabilities.append(
            f"Total Forms Found: {len(forms)}"
        )

        # FIND INPUT FIELDS

        inputs = soup.find_all("input")

        vulnerabilities.append(
            f"Input Fields Found: {len(inputs)}"
        )

        return {
            "target": url,
            "results": vulnerabilities
        }

    except requests.exceptions.ConnectionError:

        return {
            "error": "Unable to connect to website."
        }

    except requests.exceptions.Timeout:

        return {
            "error": "Request timed out."
        }

    except Exception as e:

        return {
            "error": str(e)
        }