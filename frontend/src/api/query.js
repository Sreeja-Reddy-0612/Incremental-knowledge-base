import { apiPost } from "./client";

export function queryKnowledgeBase(question) {
  return apiPost("/query", { question });
}
