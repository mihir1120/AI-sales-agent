const foundationItems = ["FastAPI", "LangGraph", "PostgreSQL", "Alembic"];

export default function Home() {
  return (
    <main>
      <section className="shell" aria-labelledby="page-title">
        <div className="eyebrow">V1 Foundation</div>
        <h1 id="page-title">Sales AI Agent</h1>
        <p>
          A small, runnable starting point for researching, qualifying, and
          preparing sales outreach with human approval in the loop.
        </p>
        <ul className="status" aria-label="Foundation components">
          {foundationItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
