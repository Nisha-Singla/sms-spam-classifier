# SMS Spam Classifier

A machine learning project that classifies SMS messages as spam or not spam.

## Technologies Used
- Python
- Scikit-learn
- NLTK
- Pandas
- NumPy
- Streamlit

## Model
- TF-IDF vectorizer
- Multinomial Naive Bayes classifier

## Project Structure
```
├── app.py                  # Streamlit app for predictions
├── artifacts/
│   ├── model.pkl           # Trained ML model
│   └── vectorizer.pkl      # TF-IDF vectorizer
├── data/
│   └── spam.csv            # SMS spam dataset
├── sms_spam_detection.ipynb # Jupyter notebook with training steps
├── requirements.txt        # Dependencies
```

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd sms-spam-classifier
   ```
2. **Create a conda or virtual environment**
   ```bash
   # Using conda
   conda create -n spam_env python=3.10
   conda activate spam_env
   # OR using venv
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## Usage
- Enter an SMS message into the Streamlit UI and get a prediction: **Spam** or **Not Spam**.

## Future Improvements
- Try different classifiers
- Improve text preprocessing
- Add deployment options (Docker, cloud, etc.)

## License
MIT
