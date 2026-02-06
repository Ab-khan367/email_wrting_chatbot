
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.document_loaders import WebBaseLoader

from app.backend.chains import Chain
from app.backend.portfolio import Portfolio
from app.backend.utils import clean_text

app = FastAPI()

chain = Chain()
portfolio = Portfolio()
portfolio.load_portfolio()

###
class Sender(BaseModel):
    name: str
    role: str


class URLRequest(BaseModel):
    url: str
    #new lines starts
    sender: Sender
    company_details: str
    tone: str | None = "Professional"
    




@app.post("/generate-emails")
def generate_email(request: URLRequest):
    try:
        
        docs = WebBaseLoader([request.url]).load()
        if not docs:
            raise HTTPException(status_code=400, detail="Failed to load webpage")
        raw_text = docs.pop().page_content
        
        cleaned_text = clean_text(raw_text)

        jobs = chain.extract_jobs(cleaned_text)
        if not jobs:
            return {
                "emails": [],
                "error": "No job postings extracted from the page"
            }
        emails = []
        for job in jobs:
            skills = job.get("skills", [])
            if isinstance(skills, str):
                skills = [s.strip() for s in skills.split(",")]
            elif not isinstance(skills, list):
                skills = []
            links = portfolio.query_links(skills)
        
            email = chain.write_mail(
                job=job,
                links=links,
                sender_details=request.sender.dict(),
                company_details=request.company_details,
                tone=request.tone
                )
            emails.append(email)

        return {"emails": emails}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

