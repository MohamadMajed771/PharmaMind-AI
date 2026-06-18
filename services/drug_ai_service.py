import json
import re
import ollama


def _extract_json(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Could not parse AI response as JSON.")


def analyze_drug(drug_name: str) -> dict:
    prompt = f"""
You are PharmaMind AI, an advanced pharmacy education assistant.

Create a detailed pharmacy-student drug monograph for: {drug_name}

Return ONLY valid JSON. No markdown outside JSON.

Use this exact JSON structure:

{{
  "drug_name": "",
  "generic_name": "",
  "brand_names": "",
  "drug_class": "",
  "therapeutic_category": "",
  "quick_summary": "",
  "indications": "",
  "mechanism": "",
  "pharmacokinetics": "",
  "adult_dose": "",
  "pediatric_dose": "",
  "renal_adjustment": "",
  "hepatic_adjustment": "",
  "contraindications": "",
  "warnings": "",
  "common_side_effects": "",
  "serious_side_effects": "",
  "drug_interactions": "",
  "food_interactions": "",
  "pregnancy_lactation": "",
  "monitoring": "",
  "toxicity_overdose": "",
  "counseling": "",
  "clinical_pearls": "",
  "exam_focus": ""
}}

Rules:
- Be detailed and pharmacy-focused.
- Use clear bullet-style text inside each JSON value.
- If exact dosing is uncertain, say verify with official drug references.
- Do not invent information.
- Educational use only.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]
    return _extract_json(content)