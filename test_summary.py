from flask import Flask, render_template, request
from jigsawstack import JigsawStack

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        jigsaw = JigsawStack()
        result = jigsaw.summary({"text": input_text})
        # Extract the summary directly from the result dictionary
        summary = result.get('summary', '')
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)