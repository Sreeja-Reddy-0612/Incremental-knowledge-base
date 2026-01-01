import { apiPost } from "./client";

export function updateDocument(doc_id, text) {
  return apiPost("/update", { doc_id, text });
}
