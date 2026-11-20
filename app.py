import gradio as gr
import spaces

@spaces.GPU
def greet(name):
    return f"Hello, {name}! Welcome to Gradio on Hugging Face."

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Hello World",
    description="My first Gradio application!"
)

demo.launch()
