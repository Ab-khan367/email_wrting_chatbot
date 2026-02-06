
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
        # self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b")
    def extract_jobs(self, cleaned_text):
        prompt = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            Extract job postings and return JSON with:
            role, experience, skills, description.
            Return ONLY valid JSON.
            """
        )

        chain = prompt | self.llm
        response = chain.invoke({"page_data": cleaned_text})

        try:
        # Clean the response to remove markdown code blocks if present
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:]  # Remove ```json
            if content.startswith("```"):
                content = content[3:]   # Remove ```
            if content.endswith("```"):
                content = content[:-3]  # Remove trailing ```
            content = content.strip()
            
            parser = JsonOutputParser()
            result = parser.parse(content)
            
            print(f"Extracted jobs: {result}")  # Debug logging
        
        except OutputParserException as e:
            print(f"Parsing error: {e}")  # Debug logging
            print(f"Raw response: {response.content}")  # See what LLM returned
            raise OutputParserException("Job parsing failed")

        return result if isinstance(result, list) else [result]

    def write_mail(self, job, links, sender_details, company_details, tone):

    # --- FIX 1: normalize skills ---
        skills = job.get("skills", [])
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(",")]
        elif not isinstance(skills, list):
            skills = []

        # --- FIX 2: default tone ---
        tone = tone or "Professional"

        job_description = f"""
    Role: {job.get('role', '')}
    Experience: {job.get('experience', '')}
    Skills: {', '.join(skills)}
    Description: {job.get('description', '')}
    """

        prompt = PromptTemplate(
            input_variables=[
                "job_description",
                "sender_name",
                "sender_role",
                "company_details",
                "link_list",
                "tone"
            ],
            template="""
    ### JOB DESCRIPTION:
    {job_description}

    You are {sender_name}, {sender_role} at {company_details}.
    Write a cold email matching the job above.
    Include relevant portfolio links: {link_list}
    Write the email in a {tone} tone.
    Do not add a preamble.

    ### EMAIL:
    """
        )

        chain = prompt | self.llm
        response = chain.invoke({
            "job_description": job_description,
            "link_list": ", ".join(links),
            "sender_name": sender_details.get("name", "Muhammad Abdullah"),
            "sender_role": sender_details.get("role", "CEO"),
            "company_details": company_details,
            "tone": tone
        })

        return response.content.strip()
