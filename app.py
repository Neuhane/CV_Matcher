from analyser import CVAnalyzer
import os

# Lecture des fichiers de texte
cv_text = open("data/cv.txt", encoding="utf-8").read()
job_offer_text = open("data/job_offer.txt", encoding="utf-8").read()

# Charger la clé API depuis le fichier .env
def load_api_key_from_env():
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

# Initialiser l’analyseur
analyzer = CVAnalyzer(api_key=load_api_key_from_env())

# Lancer l’analyse avec une question RH
result = analyzer.answer_job_question(cv_text, job_offer_text, "Comment être le canditat idéal?")
if result:
    print(result)