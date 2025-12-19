import { ingestDocument } from "../api/ingest";
import { useState } from "react";

export default function UploadDocs() {
  const [text, setText] = useState("");
  const [status, setStatus] = useState("");

  async function handleUpload() {
    if (!text.trim()) return;

    setStatus("Uploading...");
    try {
      await ingestDocument(text);
      setStatus("Document ingested successfully.");
      setText("");
    } catch {
      setStatus("Backend not running yet.");
    }
  }

  return (
    <div style={{ marginBottom: "20px" }}>
      <h4>Upload Document</h4>
      <textarea
        rows="5"
        cols="80"
        placeholder="Paste document text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={handleUpload}>Ingest</button>
      <p>{status}</p>
    </div>
  );
}
