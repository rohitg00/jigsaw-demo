from flask import Flask, render_template, request
from jigsawstack import JigsawStack, JigsawStackError
import os
import subprocess

app = Flask(__name__)

API_KEY = os.environ.get('JIGSAWSTACK_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    error_message = ""
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        input_url = request.form.get('input_url', '')
        jigsaw = JigsawStack(api_key=API_KEY)
        
        try:
            if input_url:
                result = jigsaw.web.ai_scrape({
                    "url": input_url,
                    "element_prompts": ["article"],
                })
                text = ""
                for element in result.get('data', []):
                    if 'results' in element and len(element['results']) > 0:
                        text += element['results'][0].get('text', '')

                if text:
                    summary_result = jigsaw.summary({"text": text})
                    summary = summary_result.get('summary', '')
                else:
                    summary = "Failed to scrape content"
            elif input_text:
                result = jigsaw.summary({"text": input_text})
                summary = result.get('summary', '')
        except JigsawStackError as e:
            error_message = f"JigsawStackError: {str(e)}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            
    return render_template('index.html', summary=summary, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True) #for local testing
    # app.run(host='0.0.0.0', port=5000) #for docker