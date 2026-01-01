import UploadDocs from "../components/UploadDocs";
import AskQuestion from "../components/AskQuestion";
import Results from "../components/Results";
import { useState } from "react";

import ManageDocument from "../components/ManageDocument";

export default function Home() {
  const [answer, setAnswer] = useState(null);
  const [docId, setDocId] = useState(null);

  return (
    <>
      <UploadDocs onDocIngested={setDocId} />

      {docId && (
        <>
          <p style={{ fontSize: "12px" }}>
            Active document ID: {docId}
          </p>

          <ManageDocument
            docId={docId}
            onDeleted={() => setDocId(null)}
          />
        </>
      )}

      <AskQuestion onAnswer={setAnswer} />
      <Results answer={answer} />
    </>
  );
}
