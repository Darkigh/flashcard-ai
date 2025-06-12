# Flashcard AI

A web application that generates flashcards from uploaded documents using AI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Flashcard AI project is a web-based application designed to streamline the process of creating flashcards from various document types. Users can upload PDF, DOCX, or TXT files, and the application, powered by OpenAI's GPT models, extracts key information to generate question-and-answer flashcards. This tool aims to assist students, educators, and lifelong learners in efficiently summarizing and memorizing content from their study materials.

## Features

- **Document Upload**: Supports uploading PDF, DOCX, and TXT files for flashcard generation.
- **AI-Powered Flashcard Generation**: Utilizes OpenAI's GPT models to extract key facts and generate question-and-answer flashcards.
- **Text Extraction**: Capable of extracting text content from various document formats.
- **Web-Based Interface**: Provides a user-friendly web interface for uploading documents and viewing generated flashcards.
- **CORS Enabled**: The backend is configured with CORS to allow cross-origin requests from the frontend.
- **Secure File Uploads**: Uses `werkzeug.utils.secure_filename` to ensure safe handling of uploaded file names.

## Installation

Instructions on how to install and set up the project.

### Prerequisites

List any prerequisites here (e.g., Python 3.x, pip, Node.js, npm/yarn).

### Backend Installation

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (Note: A `requirements.txt` file is assumed to be present or will need to be created based on `app.py` dependencies like `flask`, `flask-cors`, `openai`, `pdfplumber`, `docx`, `python-dotenv`, `werkzeug`)

### Frontend Installation

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install Node.js dependencies (if any, based on `src/App.js.ts`):
   ```bash
   # Example if using npm
   npm install
   # Example if using yarn
   yarn install
   ```

## Usage

To use the Flashcard AI application, you need to run both the backend and frontend components.

### Running the Backend

Navigate to the `backend` directory and run the Flask application:

```bash
cd backend
python app.py
```

The backend server will typically run on `http://127.0.0.1:5000`.

### Running the Frontend

Open the `index.html` file located in the `frontend` directory in your web browser. You can do this by navigating to the file path directly (e.g., `file:///path/to/flashcardai_project/frontend/index.html`) or by serving it with a simple local web server if you prefer.

Once both the backend and frontend are running, you can upload your documents through the web interface, and the application will generate flashcards for you.

## Project Structure

```
. (root directory)
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── upload.html
│   ├── static/
│   │   └── style.css
│   └── src/
│       └── App.js.ts
└── uploads/
    └── (uploaded documents)
```

## Contributing

We welcome contributions to the Flashcard AI project! To contribute, please follow these steps:

1.  **Fork the repository**: Start by forking the main repository to your GitHub account.
2.  **Clone your fork**: Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/your-username/flashcard-ai.git
    cd flashcard-ai
    ```
3.  **Create a new branch**: Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Make your changes**: Implement your changes and ensure they adhere to the project's coding standards.
5.  **Test your changes**: Run tests to ensure your changes haven't introduced any regressions.
6.  **Commit your changes**: Commit your changes with a clear and concise commit message:
    ```bash
    git commit -m "feat: Add new feature" # or "fix: Resolve bug"
    ```
7.  **Push to your branch**: Push your changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```
8.  **Open a Pull Request**: Go to the original repository on GitHub and open a pull request from your new branch. Provide a detailed description of your changes.

## License

This project is open-source and licensed under the MIT License. You can find the full text of the license in the `LICENSE` file in the root of the repository.


