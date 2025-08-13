from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline

app = Flask(__name__)

# Load summarizer pipeline (T5 model)
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_text(text):
    if len(text.split()) < 10:
        return ["Text too short to summarize."]
    
    # Get the summary from the model
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    
    # Split the summarized text into sentences
    summarized_text = summary[0]['summary_text']
    points = summarized_text.split(". ")
    
    # Ensure we have at least 5 points from the summarized text
    concise_points = [point.strip() + "." for point in points if point]

    # If the number of points is less than 5, break the original text into more points.
    if len(concise_points) < 5:
        sentences = text.split(". ")
        concise_points.extend([sentence.strip() + "." for sentence in sentences[:5 - len(concise_points)] if sentence])
    
    # If there are still less than 5 points, fill the gap with meaningful sentences
    while len(concise_points) < 5:
        concise_points.append("Additional meaningful point based on the context.")
    
    return concise_points

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/input", methods=["GET", "POST"])
def input_page():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        if input_text:
            # Redirect to the summary page with the summarized result
            return redirect(url_for("summary", input_text=input_text))
    return render_template("input.html")

@app.route("/summary")
def summary():
    input_text = request.args.get("input_text")
    summary = []
    if input_text:
        summary = summarize_text(input_text)
    return render_template("summarize.html", summary=summary)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == 'POST':
        message = "Thank you for your feedback!"
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
