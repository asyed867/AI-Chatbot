# 🧠 StudyBuddy Chatbot

A student-focused chatbot built with **Python**, **Flask**, and **OpenAI’s API**.  
It provides simple study assistance using local intent-based responses and AI-generated answers.  
The project demonstrates **cloud deployment on AWS Elastic Beanstalk** and **automated CI/CD using GitHub Actions**.

---

## 🌐 Live Demo

Access the deployed chatbot here:  
👉 [StudyBuddy Chatbot](http://studybuddy-chatbot-env.eba-phm9sp7b.ca-central-1.elasticbeanstalk.com)

---

## 📘 Overview

**StudyBuddy Chatbot** began as a local Python chatbot and evolved into a deployed web app with automated updates.  
It’s designed to provide quick, conversational help using both local logic and OpenAI responses.

---

## 🧰 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Python (Flask)** | Backend web framework |
| **OpenAI API** | AI-powered responses |
| **AWS Elastic Beanstalk** | Cloud hosting and deployment |
| **GitHub Actions** | Continuous integration and delivery |
| **HTML, CSS, JS** | Front-end chat interface |

---

## 🚀 Deployment Summary

- Hosted on **AWS Elastic Beanstalk** (Python 3.12 platform)  
- Sensitive credentials managed securely with environment variables  
- **GitHub Actions** automates deployment — each push to `main` redeploys the app automatically  

---

## 🔐 Environment Variables

| Variable | Description |
|-----------|--------------|
| `OPENAI_API_KEY` | API key for OpenAI access (used by the chatbot) |

> Sensitive credentials are managed securely using environment variables and GitHub Secrets.

---

## 🔄 Continuous Deployment (CI/CD)

Each commit to the `main` branch triggers the **GitHub Actions workflow** (`deploy.yml`) to:

1. Package the project  
2. Upload it to AWS S3  
3. Create a new Elastic Beanstalk version  
4. Redeploy automatically to the live environment  

This ensures the chatbot stays continuously up to date.

---

## 💭 Summary

- Built and deployed a **Flask-based chatbot** integrated with OpenAI  
- Hosted securely on **AWS Elastic Beanstalk**  
- Automated deployment using **GitHub Actions**  
- Demonstrates cloud deployment, CI/CD, and full-stack integration skills in a compact project
