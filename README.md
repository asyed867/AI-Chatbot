# 🧠 StudyBuddy Chatbot

A student-focused chatbot built with **Python**, **Flask**, and **OpenAI’s API**.  
It provides simple study assistance using both **rule-based intent matching (scikit-learn)** and **AI-generated answers**.  
The project demonstrates **cloud deployment on AWS Elastic Beanstalk** with **automated CI/CD via GitHub Actions**.

---

## 🌐 Live Demo

Access the deployed chatbot here:  
👉 [StudyBuddy Chatbot](http://studybuddy-chatbot-env.eba-phm9sp7b.ca-central-1.elasticbeanstalk.com)

---

## 📘 Overview

**StudyBuddy Chatbot** began as a local Python chatbot and evolved into a deployed web app with automated updates.  
It’s designed to provide quick, conversational help using local intent detection and OpenAI-based responses.

---

## 🧰 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Python (Flask)** | Backend web framework |
| **scikit-learn** | Intent matching and text processing |
| **OpenAI API** | AI-powered responses |
| **Gunicorn** | WSGI server for production deployment |
| **python-dotenv** | Environment variable management |
| **AWS Elastic Beanstalk** | Cloud hosting and deployment |
| **GitHub Actions** | Automated CI/CD pipeline |
| **HTML, CSS, JS** | Front-end chat interface |

---

## 🚀 Deployment Summary

- Hosted on **AWS Elastic Beanstalk** (Python 3.12 platform)  
- Sensitive credentials managed securely with environment variables  
- Automatic deployment pipeline using **GitHub Actions CI/CD**  

---

## 🔐 Environment Variables

| Variable | Description |
|-----------|--------------|
| `OPENAI_API_KEY` | API key for OpenAI access (used by the chatbot) |

> Sensitive credentials are managed securely using environment variables and GitHub Secrets.

---

## 💭 Summary

- Built and deployed a **Flask-based chatbot** integrating scikit-learn and OpenAI  
- Hosted securely on **AWS Elastic Beanstalk**  
- Implemented automated deployment using **GitHub Actions CI/CD**  
- Demonstrates cloud deployment, automation, and full-stack integration skills in a compact project
