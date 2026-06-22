import ollama


def generate_quiz(drug_name: str) -> str:
    prompt = f"""
You are PharmaMind AI.

Generate a pharmacy-student quiz about:

Drug: {drug_name}

Requirements:

- Generate 10 multiple-choice questions.
- Each question must have 4 choices (A, B, C, D).
- After each question provide:
    - Correct Answer
    - Explanation

Focus on:
- Mechanism of action
- Indications
- Dosing
- Side effects
- Contraindications
- Drug interactions
- Counseling points
- High-yield exam facts

Format clearly using Markdown.

End with:
"Study Tip: ..."
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]