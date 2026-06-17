"""

GITHUB SESSION COOKIES

GitHub code search requires an authenticated session. Copy this file to
`cookies.py` (same directory) and fill in the cookies from a logged-in
GitHub session in your browser (DevTools -> Application -> Cookies).

`cookies.py` is git-ignored on purpose — never commit your real session
cookies.

"""


GITHUB_COOKIES = [
    {"name": "user_session", "value": "<your user_session cookie>"},
    {"name": "_gh_sess", "value": "<your _gh_sess cookie>"},
]
