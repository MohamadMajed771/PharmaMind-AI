import ollama


def compare_drugs(drug1: str, drug2: str) -> str:
    prompt = f"""
You are PharmaMind AI, a pharmacy education assistant.

Compare these two drugs for pharmacy students:

Drug 1: {drug1}
Drug 2: {drug2}

Create a clear comparison using Markdown tables.

Include:

1. Quick summary
2. Drug class
3. Mechanism of action
4. Main indications
5. Adult dosing
6. Important side effects
7. Serious warnings
8. Contraindications
9. Drug interactions
10. Pregnancy and lactation
11. Patient counseling
12. Pharmacist clinical pearls
13. Exam-focused differences
14. Which drug is preferred in common situations

Rules:
- Be organized.
- Use tables where possible.
- If dosing is uncertain, say verify with official references.
- End with: Educational use only. Always verify with official drug references.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]