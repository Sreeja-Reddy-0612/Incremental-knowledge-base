export default function Results({ answer }) {
  if (!answer) return null;

  return (
    <div>
      <h4>Answer</h4>
      <div style={{ padding: "10px", border: "1px solid #ccc" }}>
        {answer}
      </div>
    </div>
  );
}
