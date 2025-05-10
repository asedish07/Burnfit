# GPT QLoRA 예시 코드

# from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
# from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
# from trl import SFTTrainer

# model_name = "meta-llama/Meta-Llama-3-3B"

# # Load tokenizer and model (4-bit)
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     load_in_4bit=True,
#     device_map="auto",
#     quantization_config=BitsAndBytesConfig(load_in_4bit=True),
# )

# # Prepare for QLoRA
# model = prepare_model_for_kbit_training(model)
# lora_config = LoraConfig(
#     r=8,
#     lora_alpha=16,
#     target_modules=["q_proj", "v_proj"],  # Depends on the model arch
#     lora_dropout=0.05,
#     bias="none",
#     task_type="CAUSAL_LM"
# )
# model = get_peft_model(model, lora_config)

# # Fine-tuning
# trainer = SFTTrainer(
#     model=model,
#     train_dataset=your_dataset,
#     args=TrainingArguments(
#         output_dir="./qlora-llama3-3b",
#         per_device_train_batch_size=2,
#         gradient_accumulation_steps=8,
#         num_train_epochs=3,
#         logging_steps=10,
#         save_steps=100,
#         save_total_limit=2,
#         fp16=True
#     ),
#     tokenizer=tokenizer
# )

# trainer.train()
