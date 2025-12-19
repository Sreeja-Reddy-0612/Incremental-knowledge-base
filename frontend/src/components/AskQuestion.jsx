import { queryKnowledgeBase } from "../api/query";
import { useState } from "react";

export default function AskQuestion({ onAnswer }) {
  const [question, setQuestion] = useState("");

  async function handleAsk() {
    if (!question.trim()) return;

    try {
      const response = await queryKnowledgeBase(question);
      onAnswer(response.answer);
    } catch {
      onAnswer("Backend not running yet.");
    }
  }

  return (
    <div style={{ marginBottom: "20px" }}>
      <h4>Ask a Question</h4>
      <input
        type="text"
        size="80"
        value={question}
        placeholder="Ask something..."
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={handleAsk}>Ask</button>
    </div>
  );
}
