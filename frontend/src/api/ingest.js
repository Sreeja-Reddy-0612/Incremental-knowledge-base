import { apiPost } from "./client";

export function ingestDocument(text) {
  return apiPost("/ingest", { text });
}
