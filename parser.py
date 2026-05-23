from pydantic import BaseModel
from typing import List, Dict


class BlogOutput(BaseModel):

    blog_title: str

    blog_intro: str

    outline_sections: List[Dict]

    target_audience: str

    writing_goal: str

    seo_keywords: List[str]