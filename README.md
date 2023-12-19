# Currency Converter Flask App

## Overview
This is a simple web application built with Flask for converting currencies. It uses an external API to fetch real-time currency conversion rates.

## Features
- Currency conversion between a variety of currencies.
- Real-time fetching of conversion rates from an external API.
- User-friendly web interface.

## Requirements
- Python 3.10
- Flask
- Requests

## Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/vib795/flask-currency-converter.git
cd currency-converter
```

Then, create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:
```bash
pip install -r requirements.txt
```
## Usage
To run the application, execute:
```bash
flask run
```

Navigate to http://127.0.0.1:5000/ in your web browser to use the application.

## Deployment 
To deploy your Flask application on Vercel and integrate it into your README.md, you can follow these steps:
- **Install Vercel CLI:** First, install the Vercel CLI globally using npm:
    ```bash
    npm install -g vercel
    ```
- **Vercel Account Setup:** Make sure you have a Vercel account. If not, create one at Vercel.
- **Prepare Your Project:** Ensure your Flask project has `requirements.txt` and `vercel.json` files. The `vercel.json` should specify the Python runtime and routing configurations. Example:
    ```json
    {
    "version": 2,
    "builds": [
        {
        "src": "./app.py",
        "use": "@vercel/python"
        }
    ],
    "routes": [
        {
        "src": "/(.*)",
        "dest": "app.py"
        }
    ]
    }
    ```

- **Deploy with Vercel:** Navigate to your project directory and run the vercel command to deploy.

- **Update After Changes:** After making updates to your project, deploy using `vercel --prod` to push your changes to the production environment.

- When deploying your Flask app on Vercel, it's crucial to modify the app's entry point. Specifically, **remove the following lines from your main application file:**
    ```python
    if __name__ == '__main__':
        app.run()
    ```

## Live demo:
https://swiftconvert.vercel.app/

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
MIT License - Feel free to use and modify this code for your personal or educational projects.
