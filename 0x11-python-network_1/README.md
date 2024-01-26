This repository contains Python scripts that interact with the GitHub API to perform various tasks. Each script focuses on specific functionalities using the requests and sys packages.

Scripts
0-hbtn_status.py
bash
Copy code
./0-hbtn_status.py | cat -e
This script fetches the status of the https://alx-intranet.hbtn.io website using the urllib package.

1-hbtn_header.py
bash
Copy code
./1-hbtn_header.py https://alx-intranet.hbtn.io
This script takes a URL as an argument, sends a request, and displays the value of the X-Request-Id variable from the response header using the urllib package.

2-post_email.py
bash
Copy code
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
This script sends a POST request to the specified URL with an email as a parameter using the urllib package.

3-error_code.py
bash
Copy code
./3-error_code.py http://0.0.0.0:5000
This script sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code.

4-hbtn_status.py
bash
Copy code
./4-hbtn_status.py | cat -e
This script fetches the status of the https://alx-intranet.hbtn.io website using the requests package.

5-hbtn_header.py
bash
Copy code
./5-hbtn_header.py https://alx-intranet.hbtn.io
This script takes a URL as an argument, sends a request, and displays the value of the X-Request-Id variable from the response header using the requests package.

6-post_email.py
bash
Copy code
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
This script sends a POST request to the specified URL with an email as a parameter using the requests package.

7-error_code.py
bash
Copy code
./7-error_code.py http://0.0.0.0:5000
This script sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code using the requests package.

8-json_api.py
bash
Copy code
./8-json_api.py a
This script takes a letter as an argument, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the body of the response using the requests package.

10-my_github.py
bash
Copy code
./10-my_github.py <your_username> <your_personal_access_token>
This script takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's id using the requests package.

100-github_commits.py
bash
Copy code
./100-github_commits.py rails rails
This script lists the 10 most recent commits (from the most recent to oldest) of the "rails" repository by the user "rails" using the GitHub API and the requests package.

Author
Dr. Appiagyei
