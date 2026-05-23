def create_prompt(topic, audience, tone, length):

    prompt = f"""

    You are an expert AI Blog Strategist, SEO Specialist,
    and Content Marketing Expert.

    Your task is to generate:

    1. SEO Optimized Blog Title
    2. Blog Introduction
    3. Structured Blog Outline
    4. Writing Goal
    5. SEO Keywords

    USER INPUT:

    Topic: {topic}

    Target Audience: {audience}

    Writing Tone: {tone}

    Blog Length: {length}

    REQUIREMENTS:

    - Create engaging title
    - Make title SEO optimized
    - Create professional introduction
    - Outline must include:
        • Introduction
        • Main Concepts
        • Examples
        • Challenges
        • Conclusion
    - Content should match audience
    - SEO keywords should be search friendly
    - Return ONLY valid JSON
    - No markdown
    - No explanations

    OUTPUT FORMAT:

    {{
        "blog_title": "",
        "blog_intro": "",
        "outline_sections": [],
        "target_audience": "",
        "writing_goal": "",
        "seo_keywords": []
    }}

    """

    return prompt