import { apiPost } from "./client";

export function deleteDocument(doc_id) {
  return apiPost("/delete", { doc_id });
}
