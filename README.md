
# Send Text Message and Email

This project reads data columns from the csv file and sends text messages and email using sms-magic API.
Framework used in this Project is FASTAPI and will be deployed using uvicorn.





## Installation
Here are the complete steps to install all the software and packages

1) Install Python latest version from below link
```bash
https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe
```
2) Install Packages - First Navigate to the src folder then enter install requirements command
```bash
cd src
pip install -r requirements.txt
```

    
## Deployment

To deploy this project we will use uvicorn to deploy and make sure to first navigate to src folder.
Run this command below


```bash
  uvicorn main:app --reload
```

