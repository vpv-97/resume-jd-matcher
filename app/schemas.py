from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
	resume_text: str = Field(..., min_length=50)
	job_description: str = Field(..., min_length=50)

class MatchResult(BaseModel):
	match_score: int = Field(..., ge=0, le=100)
	matched_skills: list[str]
	missing_skills: list[str]
	suggested_edits: list[str] = Field(..., min_length=2, max_length=3)