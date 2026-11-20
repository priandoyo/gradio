---
title: Gradio Hello World
emoji: 👋
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# Gradio Hello World

A simple web application built with **Python and Gradio**, deployed to the public internet using **GitHub, GitHub Actions, and Hugging Face Spaces**.

This project demonstrates how to build a lightweight Python web application and establish an automated CI/CD deployment pipeline without managing your own server.

**Live Application:** https://huggingface.co/spaces/priandoyo/gradio

**Source Code:** https://github.com/priandoyo/gradio

---

## 1. Project Overview

This project explores the integration of three platforms:

| Platform | Purpose |
|---|---|
| GitHub | Source code management |
| GitHub Actions | CI/CD automation |
| Hugging Face Spaces | Application hosting |
| Gradio | Python web application framework |

The objective is to develop a simple Hello World application, store the source code in GitHub, and automatically deploy it to Hugging Face Spaces.

## 2. Technology Stack

- **Python:** Application programming language
- **Gradio:** Python framework for building interactive web interfaces
- **GitHub:** Code repository and version control
- **GitHub Actions:** Automated deployment workflow
- **Hugging Face Spaces:** Cloud application hosting
- **ZeroGPU:** GPU infrastructure for supported applications

## 3. Application Code

### app.py

```python
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
```

### requirements.txt

```text
gradio
spaces
```

The `spaces` library provides Hugging Face-specific functionality.

The `@spaces.GPU` decorator makes the function compatible with Hugging Face ZeroGPU infrastructure.

## 4. Deployment Architecture

The deployment architecture uses GitHub as the source of truth and Hugging Face as the hosting platform.

```text
Developer
    |
    v
GitHub Repository
    |
    | Commit / Push
    v
GitHub Actions
    |
    | Automated deployment
    | Using Hugging Face Access Token
    v
Hugging Face Spaces
    |
    v
Gradio Application
    |
    v
Public Internet
```

### Deployment Workflow

1. Develop the application locally or in a development environment.
2. Push the source code to GitHub.
3. GitHub Actions detects the repository update.
4. GitHub Actions authenticates with Hugging Face using an access token.
5. Application files are synchronized to the Hugging Face Space.
6. Hugging Face builds and starts the Gradio application.
7. The application becomes accessible through its public URL.

## 5. GitHub Actions Configuration

The deployment workflow is stored in:

`.github/workflows/deploy.yml`

GitHub Actions uses a Hugging Face access token to authenticate and deploy the application.

The token must be stored securely in:

**GitHub Repository → Settings → Secrets and variables → Actions**

Create a repository secret named:

`HF_TOKEN`

Never hardcode the access token in Python code or commit it to GitHub.

The workflow automatically deploys updates whenever changes are pushed to the configured branch.

## 6. Hugging Face Hardware: CPU vs GPU

This was the most important lesson during deployment.

Hugging Face Spaces provides different hardware configurations, and hardware availability depends on the account's subscription and usage restrictions.

| Hardware | Typical use | Cost / access |
|---|---|---|
| CPU Basic | Simple Python applications, Gradio demos, dashboards | Free tier, subject to eligibility |
| CPU Upgrade | Applications requiring more CPU resources | Paid |
| ZeroGPU | GPU-based machine learning applications | Free allocation subject to quota |
| Dedicated GPU | Intensive AI and deep learning workloads | Paid |

### Important Lesson: Understand Hardware Restrictions Before Creating a Space

Initially, I selected ZeroGPU when creating the Hugging Face Space.

Later, I discovered that I could not downgrade this existing Space to CPU Basic without a PRO subscription.

Hugging Face explicitly displayed:

"Without a PRO subscription, you can't downgrade this Space to cpu-basic."

This created an unexpected deployment constraint.

**Lessons learned:**

- Choose the hardware configuration before creating a Space.
- Do not assume that switching hardware is always available.
- Free CPU and free GPU have different eligibility and usage restrictions.
- ZeroGPU has a limited daily GPU allocation.
- A simple Hello World application does not technically require GPU computation.
- Avoid selecting GPU hardware unnecessarily when a free CPU option is available.

For a new project, check the available hardware options and account restrictions before creating the Space.

## 7. Important ZeroGPU Configuration

When using ZeroGPU, Hugging Face requires GPU-compatible function configuration.

The following code is important:

```python
import spaces

@spaces.GPU
def greet(name):
    return f"Hello, {name}!"
```

Without the decorator, Hugging Face may report:

`No @spaces.GPU function detected during startup`

This was the second important technical lesson.

**CPU Basic vs ZeroGPU:**

| Configuration | Application code |
|---|---|
| CPU Basic | Ordinary Python and Gradio |
| ZeroGPU | Import `spaces` and decorate GPU-compatible functions using `@spaces.GPU` |

Note that the decorator is intended for functions that need GPU allocation. Using it for a simple greeting function is a workaround to satisfy ZeroGPU's startup requirement, not an efficient use of GPU resources.

Calling the decorated function consumes GPU allocation.

## 8. Troubleshooting and Lessons Learned

During deployment, several problems were encountered.

| Problem | Root cause | Solution |
|---|---|---|
| Missing configuration in README | Missing Hugging Face metadata | Add YAML front matter |
| Configuration error | Gradio SDK not specified | Set `sdk: gradio` |
| Missing application file | Application entry point not configured | Set `app_file: app.py` |
| No `@spaces.GPU` function detected | ZeroGPU requires GPU-decorated function | Import `spaces` and add `@spaces.GPU` |
| Cannot downgrade to CPU Basic | Hugging Face subscription restriction | Keep ZeroGPU or use an eligible CPU hosting option |
| GitHub Actions deployment failed | Initial deployment/authentication configuration issue | Configure access token and workflow correctly |

### Lesson 1: README.md Is More Than Documentation

In Hugging Face Spaces, README.md also contains application configuration.

The YAML metadata at the beginning determines:

- Application title
- SDK framework
- Application entry point
- Display metadata

For Gradio, the important configuration is:

```yaml
---
title: Gradio Hello World
sdk: gradio
app_file: app.py
---
```

### Lesson 2: CI/CD Eliminates Manual Deployment

Once GitHub Actions is configured, changes committed to GitHub can automatically synchronize to Hugging Face.

There is no need to manually upload application files every time.

### Lesson 3: Hosting and Framework Are Different Things

Gradio is an application framework, not a hosting service.

- Gradio builds the application interface.
- Hugging Face Spaces hosts and executes the application.
- GitHub stores the source code.
- GitHub Actions automates deployment.

These are separate components working together.

## 9. Project Structure

```text
gradio/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app.py
├── requirements.txt
└── README.md
```

## 10. Key Takeaways

This small project demonstrates several important software engineering concepts:

1. **Web Application Development:** Building interactive web applications using Python and Gradio.
2. **Version Control:** Managing source code using GitHub.
3. **CI/CD:** Automating deployment through GitHub Actions.
4. **Cloud Hosting:** Publishing applications using Hugging Face Spaces.
5. **Cloud Infrastructure:** Understanding the differences between CPU and GPU hosting.
6. **Configuration Management:** Using README metadata to configure application execution.
7. **Security:** Managing deployment credentials through GitHub Secrets.

---

## 11. Future Experiments

The same deployment architecture can be reused for more advanced applications:

- MiniBank – Banking simulator
- MiniScore – Credit scoring application
- FoodVision – AI-powered computer vision
- MiniFDS – Fraud detection system
- SmartRecruit – Recruitment application

The objective is to establish a reusable development and deployment pattern for Python-based applications.

---

**Project:** Gradio Hello World  
**Author:** Anjar Priandoyo  
**Repository:** https://github.com/priandoyo/gradio  
**Hosting:** Hugging Face Spaces  
**Deployment:** GitHub Actions  
**Status:** Successfully deployed
