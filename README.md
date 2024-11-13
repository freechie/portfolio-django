# 🌐 John R. Molina - Software Engineering Portfolio

Welcome to my portfolio website! This site showcases my skills, projects, and experience as a software engineer, with a focus on full-stack development, data analysis, and systems programming. It serves as a hub for my professional online presence and a platform to highlight my recent work and technical expertise.

## 🔗 Live Demo
Check out the live website here: [johndev.io](https://www.johndev.io)

## 📝 Table of Contents
- [About Me](#about-me)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact](#contact)

## 👨‍💻 About Me

I am a software engineer specializing in data management and analysis, full-stack development, and systems programming. My expertise spans Python, C/C++, Java, Javascript, SQL, React, AWS, and Docker where I excel in building data-driven applications, optimizing complex datasets, and developing scalable applications. In my freelance work, I have contributed to training Large Language Models (LLMs) using Reinforcement Learning from Human Feedback (RLHF), enhancing model accuracy and performance.

Additionally, I authored a Jupyter Notebook on global economic impact analysis, providing insights into how significant global events affect financial markets and key economic sectors. This research utilized data from sources such as Bloomberg Intelligence and Stockholm International Peace Research Institute(SIPRI), analyzing trends across industries, such as defense, healthcare, and energy to assess market resilience during major events. I am driven by solving complex challenges through efficient data engineering, automation, and secure, scalable software solutions.

## ✨ Features
- Fully responsive design using Tailwind CSS.
- Projects showcase with detailed descriptions and links to GitHub repositories.
- REST API backend powered by Django Rest Framework.
- Relational database using SQLite3 for content management.
- Security features including CAPTCHA and HTTPS.
- Fast and dynamic UI with React frontend.

## 🛠️ Technologies Used

- **Languages**: Python, JavaScript, SQL, Bash, C/C++, HTML/CSS
- **Frontend**: React, Tailwind CSS, Bootstrap
- **Backend**: Django, Django Rest Framework, Node.js
- **Database**: SQLite3
- **DevOps**: GitHub Actions, Gunicorn, DigitalOcean Ubuntu Server Droplet
- **Developer Tools**: Git, NeoVim, VS Code
- **Security**: Hashing, CAPTCHA, HTTPS, Rate Limiting

## 🚀 Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rich-txt-editor/portfolio.git
   cd portfolio
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Update the `.env` file with your configuration.

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📂 Project Structure

```
portfolio/
├── backend/
│   ├── manage.py
│   └── myproject/
├── frontend/
│   ├── public/
│   └── src/
├── venv/
├── .env
├── requirements.txt
├── README.md
```

- `backend/`: Django backend files.
- `frontend/`: React frontend files.
- `.env`: Environment variables.
- `requirements.txt`: Python dependencies.

## 📦 Deployment

For deployment, the frontend can be hosted on Vercel or Netlify, and the backend can be deployed on AWS EC2, Heroku, or DigitalOcean.

## 📬 Contact

Feel free to connect with me for collaboration or inquiries:

- **Email**: [johnrichardmolina@gmail.com](mailto:johnrichardmolina@gmail.com)
- **LinkedIn**: [linkedin.com/in/jrmolin90](https://linkedin.com/in/jrmolin90)
- **GitHub**: [github.com/rich-txt-editor](https://github.com/rich-txt-editor)
- **Website**: [johndev.io](https://www.johndev.io)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
