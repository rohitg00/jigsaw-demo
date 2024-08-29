# Generate smarter text summaries with JigsawStack AI

This project implements a text summarization web application using [JigsawStack](https://jigsawstack.com/)'s AI capabilities and Flask web framework.

![Text Summarizer UI](https://snipboard.io/OBbThU.jpg)

## Features
- Summarize in any language

- Contextual understanding to maintain key points

- Maintaining sentiments of the original text

- Point form or paragraph format

- Specialized fine tuned LLM engine for summarizing texts

## Prerequisites

- [JigsawStack AI Scrape API key](hhttps://docs.jigsawstack.com/api-reference/ai/summary)


## Setup

1. Install required packages:
   ```
   pip install flask jigsawstack
   ```

2. Set up your JigsawStack API key as an environment variable:
   ```
   export JIGSAWSTACK_API_KEY='your_api_key_here'
   ```

3. Create a Flask application file `test_summary.py` with the provided code.

4. Create an HTML template file `templates/index.html` with the provided code.

## Running the Application

1. Execute the Flask application:
   ```
   python test_summary.py
   ```

2. Access the application at `http://127.0.0.1:5000` or `http://localhost:5000` in your web browser.

## Using the Text Summarizer

1. Enter the text you want to summarize in the provided text area.
2. Click the **"Generate Summary"** button to submit the form.
3. The summary will appear below the input form after processing.

## Technical Details

- The Flask route handles both GET and POST requests.
- On POST, it retrieves the input text, uses JigsawStack's summary function, and renders the result.
- The HTML template uses Jinja2 templating to conditionally display the summary.
- CSS styles are embedded in the HTML for simplicity.
- JavaScript is used to dynamically adjust the textarea height based on content.

## Error Handling

Ensure proper error handling is implemented for API failures or invalid inputs in a production environment.