
# 💊 MedicineIdentifierAI

An AI-assisted web application that analyzes medicine-package images and reports visible product information using Python, Flask, and the Groq API.

## ✨ Features

- Upload medicine-package images in JPG, PNG, and WebP formats.
- Preview the selected image before analysis.
- Extract and describe visible medicine-package details using an AI vision model.
- Present results with readable headings, paragraphs, and bullet points.
- Apply cautious handling of ingredient and strength information.
- Validate uploaded image formats and enforce a 5 MB upload limit.
- Responsive interface for desktop and mobile devices.

## 🛠️ Technologies Used

- Python
- Flask
- Groq API
- HTML and CSS
- JavaScript
- Pillow
- python-dotenv

## 📁 Project Structure

```text
MedicineIdentifierAI/
├── app.py
├── requirements.txt
├── test_api.py
├── .gitignore
└── templates/
    └── index.html
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Renu0222/MedicineIdentifierAI.git
cd MedicineIdentifierAI
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key. Never commit or share your actual `.env` file.

### 5. Run the application

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

## 🔐 Security and Privacy

- API credentials should be stored in a local `.env` file.
- The `.env` file and virtual environment should not be committed to Git.
- Uploaded image data is processed in memory by the Flask application before being sent to the configured AI service. Review the code and provider policies before using sensitive images.

## ⚠️ Medical Safety Disclaimer

This application is an educational prototype, not a medical device or a substitute for professional medical advice.

AI-generated results can be incomplete or incorrect. Image analysis cannot establish medicine authenticity or reliably identify loose tablets from appearance alone. Do not take an unidentified medicine or make treatment decisions based on this application's output. Verify medicine identity and label information with a pharmacist or doctor.

## 👩‍💻 Author

Renuka Biradar

GitHub: [Renu0222](https://github.com/Renu0222)
