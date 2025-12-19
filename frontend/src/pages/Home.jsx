import UploadDocs from "../components/UploadDocs";
import AskQuestion from "../components/AskQuestion";
import Results from "../components/Results";
import { useState } from "react";

export default function Home() {
  const [answer, setAnswer] = useState(null);

  return (
    <>
      <UploadDocs />
      <AskQuestion onAnswer={setAnswer} />
      <Results answer={answer} />
    </>
  );
}
