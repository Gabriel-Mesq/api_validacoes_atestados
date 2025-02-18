from fastapi import FastAPI
from pydantic import BaseModel
from rapidfuzz import fuzz

app = FastAPI()

class NamePair(BaseModel):
    name1: str
    name2: str

@app.post("/compare")
def compare_names(pair: NamePair):
    # Similaridade usando Levenshtein Distance
    levenshtein_score = fuzz.ratio(pair.name1.lower(), pair.name2.lower())
    
    # Similaridade usando Jaro-Winkler (melhor para nomes)
    jaro_winkler_score = fuzz.WRatio(pair.name1.lower(), pair.name2.lower())
    
    # Média ponderada das similaridades
    final_score = (levenshtein_score * 0.5) + (jaro_winkler_score * 0.5)
    
    return {"similarity": final_score / 100}