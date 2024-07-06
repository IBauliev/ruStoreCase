import json
from docx import Document
from docx.shared import RGBColor


def extract_question_answer_pairs(doc_path):
    doc = Document(doc_path)

    # Цвет шрифта
    question_color = RGBColor(79, 129, 189)

    question_answer_pairs = []
    current_question = None
    current_answer = []

    for para in doc.paragraphs:
        # проверка на цвет заголовка
        if any(run.font.color and run.font.color.rgb == question_color for run in para.runs):
            if current_question and current_answer:
                answer_text = "\n".join(current_answer).strip()
                if len(answer_text) <= 2000:
                    question_answer_pairs.append({
                        "request": current_question,
                        "response": answer_text
                    })
                current_answer = []

            current_question = para.text.strip()
        else:
            if para.text.strip():
                current_answer.append(para.text.strip())

    if current_question and current_answer:
        question_answer_pairs.append({
            "request": current_question,
            "response": "\n".join(current_answer).strip()
        })

    return question_answer_pairs


doc_path = 'data/documentation.docx'
text_snippets = extract_question_answer_pairs(doc_path)

if not text_snippets:
    raise ValueError("No question-answer pairs found in the document")


def create_jsonl(filename, data, lines=202):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(min(lines, len(data))):
            item = data[i]
            json_line = json.dumps(
                {"request": [{"role": "user", "text": item["request"]}], "response": item["response"]},
                ensure_ascii=False)
            f.write(json_line + '\n')
        if lines > len(data):
            for i in range(lines - len(data)):
                item = data[i % len(data)]
                json_line = json.dumps(
                    {"request": [{"role": "user", "text": item["request"]}], "response": item["response"]},
                    ensure_ascii=False)
                f.write(json_line + '\n')


create_jsonl('data/output.jsonl', text_snippets, lines=202)
