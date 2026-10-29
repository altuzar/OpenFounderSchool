# Pi from pi.dev

This is the agent harness at [pi.dev](https://pi.dev/), not another product named Pi. The [configuration documentation](https://pi.dev/docs/latest/configuration) describes AGENTS.md and local prompts in `.pi/prompts/`.

## Adult-managed installation

Follow the [official quickstart](https://pi.dev/docs/latest/quickstart), review the installer, and configure an eligible provider with its own budget. This repository does not run installers or supply keys. Installing Pi does not make its models or tools free.

## Use the curriculum

1. Clone or unzip the repository into a dedicated folder without personal documents accessible to the agent.
2. Open your terminal there and start Pi according to your installation (`pi`).
3. Review loaded project instructions: AGENTS.md asks for COACH.md and the minimum materials.
4. Grant project trust when appropriate after reviewing files. The included prompt is Markdown, not an executable extension.
5. Use `/ofs-session` if the local `.pi/prompts/ofs-session.md` prompt was discovered; otherwise paste prompts/SESSION.md and specify the lesson.
6. Run the shared check and start in simulation. Authorize only the student's private folder for deliverables, keeping the public curriculum as reference.

## Check and exit

Ask the agent to list files it read and the week 1 criterion. Save the checkpoint as text or an authorized file. Close the session when finished. You do not need subagent packages, automation, MCP, or a replacement system prompt.

File instructions are not a sandbox. Configure tool access with the adult and consult provider safety options. This adaptation has not been tested with an actual Pi runtime: paths and packaging were checked, not authentication or model execution.
