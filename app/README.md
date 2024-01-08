# BudgetBuddy Backend

### Setup

1. Create a `local.env` file with secret value like MongoDB URI, API key, etc. inclued create email.env in models, which has email and email app password
   example:
   FROM_EMAIL=doannguyenphuchau@gmail.com
   EMAIL_PASSWORD=ucee mmkg qwxy avyp
1. Create a `local.env` file with secret value like MongoDB URI, API key, etc.
1. `pip install -r requirement-dev.txt`
1. `python app/main.py`
1. Go to http://localhost:8080/api/v1/docs
