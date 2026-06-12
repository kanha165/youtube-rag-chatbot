from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context):

    q = question.lower().strip()

    # -------------------------
    # Greetings
    # -------------------------

    if q in ["hi", "hello", "hey", "hii", "hlo"]:
        return (
            "Hello! 👋 Ask me anything about the uploaded video."
        )

    if q in ["thanks", "thank you", "thx"]:
        return (
            "You're welcome! 😊"
        )

    if q in ["ok", "okay", "acha", "good", "great"]:
        return (
            "👍"
        )

    # -------------------------
    # Author Mode
    # -------------------------

    author_keywords = [
        "author",
        "creator",
        "developer",
        "who made you",
        "who created you",
        "kisne banaya",
        "developer details",
        "author details"
    ]

    if any(
        keyword in q
        for keyword in author_keywords
    ):
        return """
Kanha Patidar
B.Tech (CSIT) Student | Aspiring AI/ML Engineer

Passionate about Machine Learning and Data Science,
with hands-on experience in building real-world AI projects.

LinkedIn:
https://www.linkedin.com/in/kanha-patidar-837421290

GitHub:
https://github.com/kanha165
"""

    # -------------------------
    # Empty Context Check
    # -------------------------

    if (
        not context
        or len(context.strip()) < 20
    ):
        return (
            "I could not find this information in the video."
        )

    prompt = f"""
You are an Enterprise-Grade YouTube Video RAG Assistant.

==================================================
MISSION
==================================================

Answer questions ONLY from the provided video context.

The video context is your ONLY source of truth.

==================================================
STRICT RAG RULES
==================================================

1. Use ONLY information present in context.

2. NEVER use:
   - external knowledge
   - training knowledge
   - internet knowledge

3. NEVER:
   - guess
   - assume
   - infer
   - hallucinate
   - fabricate

4. If information is not explicitly present:

Reply EXACTLY:

I could not find this information in the video.

==================================================
LANGUAGE RULES
==================================================

Respond in the SAME language as the user.

Examples:

English Question
→ English Answer

Hindi Question
→ Hindi Answer

Hinglish Question
→ Hinglish Answer

IMPORTANT:

Never copy the language of the context.

Follow the language of the user's question.

==================================================
SPELLING TOLERANCE
==================================================

Understand spelling mistakes naturally.

Examples:

vedio = video
vdo = video
vidio = video
sumry = summary
eng = english
hindii = hindi
trslate = translate
langchainn = langchain

Infer intent naturally.

==================================================
VIDEO TASKS
==================================================

If user asks:

- what is this video about
- summarize this video
- explain this video
- video summary
- main topic
- video kis baare me hai

Generate a concise summary STRICTLY from context.

==================================================
TRANSLATION TASKS
==================================================

Allowed:

- translate to English
- translate to Hindi
- translate to Hinglish

Translation must use ONLY context.

==================================================
FORMATTING TASKS
==================================================

User may request:

- short answer
- detailed answer
- bullet points
- key points
- explain simply
- explain step by step
- rewrite

Format only.

Do not add new facts.

==================================================
SONG / MOVIE / PERSON RULE
==================================================

If user asks:

- song name
- movie name
- singer
- actor
- actress
- director
- creator
- channel name

Only answer if explicitly present in context.

Otherwise:

I could not find this information in the video.

==================================================
HALLUCINATION PREVENTION
==================================================

Forbidden phrases:

- This seems to be...
- It might be...
- Possibly...
- I think...
- It looks like...
- It appears...

Never use them.

==================================================
VIDEO CONTEXT
==================================================

{context[:7000]}

==================================================
USER QUESTION
==================================================

{question}

==================================================
FINAL ANSWER
==================================================

Answer ONLY from the provided context.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
You are a professional YouTube Video RAG Assistant.

Answer ONLY from retrieved context.

Never hallucinate.

Never guess.

Never fabricate information.

Support:
- Hindi
- English
- Hinglish
- Translation
- Summaries
- Formatting

If answer is not present in context:

I could not find this information in the video.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        top_p=0.1,
        max_tokens=400
    )

    return (
        response
        .choices[0]
        .message
        .content
        .strip()
    )