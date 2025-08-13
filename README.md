# text-summarization-tool 
COMPANY: CODETECH IT SOLUTIONS

NAME: NAVEEN.R

INTERN ID:CT08DY717

DOMAIN NAME: ARTIFICIAL INTELLIGENCE

DURATION: 8 WEEKS

MENTOR: NEELA SANTHOSH

DESCRIPTION:

Project Title: AI-Powered Text Summarization Web Application
Project Description
This project is a web-based application that performs automatic text summarization using a pre-trained transformer model. The goal is to allow users to input large text documents or paragraphs and receive a concise summary presented in the form of bullet points. It is especially useful for students, professionals, or researchers who need to quickly digest large pieces of information.

The application is built using the Flask web framework, which provides a lightweight yet powerful way to handle routes, user requests, and rendering HTML templates. At its core, the summarization is performed using the T5 (Text-To-Text Transfer Transformer) model, accessed through Hugging Face’s Transformers pipeline. T5 is a versatile NLP model that can perform a variety of language tasks, including summarization, question-answering, and translation.

The user interface comprises multiple pages, including a home page, an input form where users submit their text, a summary results page, and additional pages such as About and Contact. The design is kept minimal and user-friendly to ensure easy interaction.

The backend takes the user input, validates it, and processes it through the T5 model to generate a meaningful summary. The application also ensures that at least five concise points are displayed to maintain consistency in output. If the summarizer does not generate enough points, fallback mechanisms are implemented to extract sentences from the original text or provide contextually meaningful placeholders.

This modular architecture ensures that the application is easy to maintain and scale. The project demonstrates the practical integration of Natural Language Processing (NLP) into a usable web interface, showcasing how modern AI models can be deployed in real-world scenarios.

Technologies Used
Python:
The primary programming language used to develop the backend of the application. Python is known for its simplicity and strong support for AI and machine learning through libraries like Transformers.

Flask:
A lightweight web framework that powers the backend of the application. Flask handles routing, request processing, and rendering HTML templates.

HTML/CSS (Jinja2 Templating):
Used for building the front-end of the application. Jinja2, Flask's templating engine, is used to dynamically display content such as summarized text and user feedback.

Hugging Face Transformers Library:
A powerful NLP library that provides access to state-of-the-art pre-trained models. The T5 model is accessed through this library using a simple pipeline interface.

T5-small Model:
A version of the T5 transformer model trained for summarization tasks. It provides a balance between performance and computational efficiency.

tools and dependencies:

pip / virtualenv: Used to manage Python packages and create isolated environments for clean project dependencies.

Jupyter / VS Code: Development environments commonly used to prototype and test the Python code.

Postman or Browser: For manually testing HTTP routes and checking application flow.

Git: Version control tool used to manage and track changes in the project


OUTPUT:


<img width="1897" height="931" alt="Image" src="https://github.com/user-attachments/assets/54b10460-3147-4d87-a90a-c60de47fd11f" />
