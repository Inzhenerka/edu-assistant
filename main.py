from edu_assistant.config import Config

config = Config.from_yaml_file("config.yml")
print("Full config:", config)
print("LLM model:", config.llm.model)

system_prompt = config.render_system_instructions(role="history_tutor", template="tutor_quick_answer")
print("System prompt:", system_prompt)
