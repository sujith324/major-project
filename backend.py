from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Your knowledge base copied exactly from your Streamlit code
knowledge_base = {
    "python": {
        "definition": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "example": "for i in range(5):\n    print(i)",
        "tip": "Practice small coding challenges daily to strengthen your logic!"
    },
    "gen ai": {
        "definition": "Generative AI (GenAI) creates new data (text, images, code) based on patterns learned from large datasets.",
        "example": "ChatGPT, DALL·E, and Gemini are examples of GenAI systems.",
        "tip": "Experiment with prompts — your phrasing shapes AI’s output!"
    },
    "llm": {
        "definition": "Large Language Models (LLMs) are advanced AI systems trained on huge datasets to generate and understand text.",
        "example": "GPT-4, Claude, and LLaMA are examples of LLMs.",
        "tip": "Understand transformer architecture — it’s the foundation of LLMs."
    },
    "algorithms": {
        "definition": "An algorithm is a step-by-step process to solve a specific problem.",
        "example": "Merge Sort, Binary Search, Dijkstra’s Algorithm.",
        "tip": "Always check time complexity to choose the best algorithm."
    },
    "sorting": {
        "definition": "Sorting arranges data in a particular order.",
        "example": "Quick Sort uses divide and conquer — fast and efficient.",
        "tip": "Remember: Merge Sort is stable; Quick Sort is faster but not stable."
    },
    "machine learning": {
        "definition": "Machine Learning allows systems to learn from data and make predictions.",
        "example": "Linear Regression for prediction, Decision Trees for classification.",
        "tip": "Start small — understand supervised vs. unsupervised learning first."
    },
    "neural networks": {
        "definition": "Neural Networks are computing systems inspired by the human brain’s neurons.",
        "example": "CNNs are used for images, RNNs for sequences like text or speech.",
        "tip": "Understand how layers and activation functions work together."
    },
    "study": {
        "definition": "Study smart, not hard — consistency beats cramming.",
        "example": "Pomodoro technique: 25 min study + 5 min break.",
        "tip": "Teach what you learn — it doubles understanding!"
    }
}


@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("message", "")

    response = "🤔 I’m not sure about that yet. Try asking about AI, Python, or algorithms."

    for topic, info in knowledge_base.items():
        if topic.lower() in user_text.lower():
            response = (
                f"📘 {topic.capitalize()}\n\n"
                f"📖 Definition: {info['definition']}\n\n"
                f"💡 Example:\n{info['example']}\n\n"
                f"✨ Tip: {info['tip']}"
            )
            break

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
