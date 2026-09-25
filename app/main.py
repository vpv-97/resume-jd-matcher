from fastapi import FastAPI
from .schemas import MatchRequest, MatchResult


app = FastAPI()

@app.get("/health")
def health():
	return {"status": "ok"}

@app.post("/match", response_model=MatchResult)
def match(request:MatchRequest):
	return MatchResult(
		match_score=50,
        matched_skills=["example"],
        missing_skills=["example"],
        suggested_edits=["example one", "example two"],
	)