import gradio as gr

def greet(name):
    return f"Hello, {name}! Welcome to Gradio."

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name", placeholder="Enter your name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Hello World",
    description="My first Gradio application using GitHub."
)

demo.launch()
