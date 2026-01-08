import re

def process_text(text: str) -> dict:
    # إزالة الفراغات
    cleaned = text.strip()

    # تحويل لحروف صغيرة
    cleaned = cleaned.lower()

    # إزالة الرموز
    cleaned = re.sub(r"[^\w\s]", "", cleaned)

    # حساب عدد الكلمات
    words = cleaned.split()
    word_count = len(words)

    return {
        "cleaned_text": cleaned,
        "word_count": word_count
    }
