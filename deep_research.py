import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    # When clicked:
    # 1️⃣ Disable the button (so user can’t click multiple times)
    # 2️⃣ Run the async generator function
    # 3️⃣ Re-enable when finished
    run_event = run_button.click(
        fn=run,
        inputs=query_textbox,
        outputs=report,
        show_progress=True,
        api_name="deep_research",
    )

    # Disable button at start of process
    run_event.then(
        fn=lambda: gr.update(interactive=False),
        inputs=None,
        outputs=run_button,
        queue=False
    )

    # Re-enable after processing completes
    run_event.then(
        fn=lambda: gr.update(interactive=True),
        inputs=None,
        outputs=run_button,
        queue=False
    )

    # Optional: trigger also on Enter key
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
