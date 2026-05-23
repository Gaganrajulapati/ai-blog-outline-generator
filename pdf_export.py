from fpdf import FPDF


def generate_pdf(data):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_left_margin(10)

    pdf.set_right_margin(10)

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", size=14)

    # MAIN TITLE
    pdf.cell(
        200,
        10,
        txt="AI Blog Outline Generator",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    # BLOG TITLE
    pdf.set_font("Arial", 'B', 12)

    pdf.cell(
        200,
        10,
        txt="Blog Title:",
        ln=True
    )

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        190,
        10,
        data["blog_title"]
    )

    pdf.ln(5)

    # BLOG INTRODUCTION
    if "blog_intro" in data:

        pdf.set_font("Arial", 'B', 12)

        pdf.cell(
            200,
            10,
            txt="Blog Introduction:",
            ln=True
        )

        pdf.set_font("Arial", size=12)

        pdf.multi_cell(
            0,
            10,
            data["blog_intro"]
        )

        pdf.ln(5)

    # OUTLINE SECTIONS
    pdf.set_font("Arial", 'B', 12)

    pdf.cell(
        200,
        10,
        txt="Outline Sections:",
        ln=True
    )

    pdf.set_font("Arial", size=12)

    for section in data["outline_sections"]:

        # IF SECTION IS DICTIONARY
        if isinstance(section, dict):

            title = section.get(
                "title",
                "Untitled Section"
            )

            description = section.get(
                "description",
                "No description available."
            )

            pdf.multi_cell(
                190,
                10,
                f"- {title}"
            )

            pdf.multi_cell(
                190,
                10,
                f"   {description}"
            )

            pdf.ln(2)

        # IF SECTION IS STRING
        else:

            pdf.multi_cell(
                190,
                10,
                f"- {section}"
            )

    pdf.ln(5)

    # TARGET AUDIENCE
    pdf.set_font("Arial", 'B', 12)

    pdf.cell(
        200,
        10,
        txt="Target Audience:",
        ln=True
    )

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        0,
        10,
        data["target_audience"]
    )

    pdf.ln(5)

    # WRITING GOAL
    pdf.set_font("Arial", 'B', 12)

    pdf.cell(
        200,
        10,
        txt="Writing Goal:",
        ln=True
    )

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        0,
        10,
        data["writing_goal"]
    )

    pdf.ln(5)

    # SEO KEYWORDS
    pdf.set_font("Arial", 'B', 12)

    pdf.cell(
        200,
        10,
        txt="SEO Keywords:",
        ln=True
    )

    pdf.set_font("Arial", size=12)

    keywords = ", ".join(data["seo_keywords"])

    pdf.multi_cell(
        0,
        10,
        keywords
    )

    # SAVE PDF
    pdf.output("blog_outline.pdf")