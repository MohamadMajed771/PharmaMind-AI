import ollama


def generate_quiz(drug_name: str) -> str:
    prompt = f"""
You are PharmaMind AI, a pharmacy education assistant.

Generate a pharmacy-student quiz about:

Drug: {drug_name}

Requirements:
- Generate 10 multiple-choice questions.
- Each question must have 4 choices: A, B, C, D.
- Put EACH choice on a separate line.
- After each question, provide:
  - Correct Answer
  - Explanation

Use this exact format:

1. Question text?

A) Choice A

B) Choice B

C) Choice C

D) Choice D

Correct Answer: A

Explanation: Explanation text.

Focus on:
- Mechanism of action
- Indications
- Dosing
- Side effects
- Contraindications
- Drug interactions
- Counseling points
- High-yield exam facts

Use clean Markdown formatting.

End with:
Study Tip: Give one short useful study tip about this drug.
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