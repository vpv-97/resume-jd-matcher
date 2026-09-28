from fastapi import FastAPI, HTTPException
from .schemas import MatchRequest, MatchResult
from .llm import get_match_result


app = FastAPI()

@app.get("/health")
def health():
	return {"status": "ok"}

@app.post("/match", response_model=MatchResult)
def match(request:MatchRequest):
	try:
		return get_match_result(request.resume_text, request.job_description)
	except Exception as e:
		print("ACTUAL ERROR:", repr(e))
		raise HTTPException(status_code=502, detail="Failed to get match result from AI service") from e