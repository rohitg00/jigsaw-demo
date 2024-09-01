# Generate smarter text summaries with JigsawStack AI

This project implements a text summarization for web application using [JigsawStack](https://jigsawstack.com/)'s AI capabilities and Flask web framework.

![AI Web Summarizer UI](https://i.imghippo.com/files/b0mGX1725177938.png)

## Features
- Summarize in any language

- Contextual understanding to maintain key points

- Maintaining sentiments of the original text

- Point form or paragraph format

- Specialized fine tuned LLM engine for summarizing texts

## Prerequisites

- [JigsawStack AI Summarizer API key](https://docs.jigsawstack.com/api-reference/ai/summary)
- [JigsawStack AI Scrape API key](https://docs.jigsawstack.com/api-reference/ai/scrape)

- Set up your JigsawStack API key as an environment variable:
   ```
   export JIGSAWSTACK_API_KEY='your_api_key_here'
   ```

## Setup

1. Install required packages:
   ```
   pip install flask jigsawstack
   ```
   
3. Clone this repository or download the source code.

4. Ensure you have the `test_summary.py` and `templates/index.html` files in your project directory.

## Running the Application

1. Execute the Flask application:
   ```
   python test_summary.py
   ```

2. Access the application at `http://127.0.0.1:5000` or `http://localhost:5000` in your web browser.

## Quick Start with Docker

1. Pull the Docker image:
   ```
   docker pull rohitghumare/ai-web-summarizer:latest
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 -e JIGSAWSTACK_API_KEY='your_api_key_here' rohitghumare64/ai-web-summarizer:latest
   ```

3. Access the application at `http://127.0.0.1:5000` or `http://localhost:5000` in your web browser.

## Using the AI Web Summarizer

1. Enter the URL in the **"Enter URL here..."** field to summarize a website, web article or blog post.
2. Alternatively, enter your text in the **"Or enter your text here..."** area for direct text summarization.
2. Click the **"Generate Summary"** button to submit the input.
3. The AI-generated summary will appear below the input form.

## Technical Details

- The Flask route handles both GET and POST requests.
- JigsawStack's `ai_scrape` function is used for web article extraction.
- The `summary` function from JigsawStack processes both scraped content and direct text input.
- Jinja2 templating is used for dynamic content rendering in the HTML.
- CSS provides a responsive, modern UI with a space-themed design.
- JavaScript creates a dynamic starry background and adjusts textarea height.

## Error Handling

The application includes error handling for API failures and invalid inputs. Error messages are displayed to the user for a smooth experience.

## Customization

You can easily customize the UI by modifying the CSS in the `index.html` file. Adjust colors, fonts, or layout to match your preferences or branding.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.