import { useState } from "react";
import { updateDocument } from "../api/update";
import { deleteDocument } from "../api/delete";


export default function ManageDocument({ onDeleted }) {
  const [docId, setDocId] = useState("");
  const [text, setText] = useState("");
  const [status, setStatus] = useState("");

  async function handleUpdate() {
    if (!docId || !text) return;
    setStatus("Updating...");
    await updateDocument(docId, text);
    setStatus("Document updated.");
  }

  async function handleDelete() {
    if (!docId) return;
    setStatus("Deleting...");
    await deleteDocument(docId);
    setStatus("Document deleted.");
    onDeleted?.();
  }

  return (
    <div>
      <h4>Manage Document</h4>

      <input
        placeholder="Enter doc_id"
        value={docId}
        onChange={(e) => setDocId(e.target.value)}
        size="50"
      />

      <br /><br />

      <textarea
        rows="4"
        cols="80"
        placeholder="Updated document text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br />
      <button onClick={handleUpdate}>Update</button>
      <button onClick={handleDelete}>Delete</button>

      <p>{status}</p>
    </div>
  );
}
