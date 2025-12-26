import { spawn } from "child_process";

// Instead of Express, spawn Streamlit for the KawaiiCode app
const streamlit = spawn("python", [
  "-m", "streamlit", "run",
  "streamlit_app/app.py",
  "--server.port", "5000",
  "--server.address", "0.0.0.0",
  "--server.headless", "true"
], {
  stdio: "inherit",
  env: { ...process.env }
});

streamlit.on("error", (err) => {
  console.error("Failed to start Streamlit:", err);
  process.exit(1);
});

streamlit.on("close", (code) => {
  console.log(`Streamlit exited with code ${code}`);
  process.exit(code || 0);
});

process.on("SIGINT", () => {
  streamlit.kill("SIGINT");
});

process.on("SIGTERM", () => {
  streamlit.kill("SIGTERM");
});
