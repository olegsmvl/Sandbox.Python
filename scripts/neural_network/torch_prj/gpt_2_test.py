from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Загрузка предварительно обученной модели и токенизатора
model_name = "gpt2"  # Можно заменить на gpt2-medium, gpt2-large, gpt2-xl для большей мощности
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Текст для начала генерации
prompt_text = "In a distant future, humanity has"

# Кодирование текста в формат, понятный модели
input_ids = tokenizer.encode(prompt_text, return_tensors='pt')

# Генерация текста
# Вы можете настроить параметры генерации, такие как max_length (макс. длина генерируемого текста)
# и num_return_sequences (количество генерируемых последовательностей)
output_sequences = model.generate(
    input_ids=input_ids,
    max_length=100,
    temperature=1.0,  # Температура определяет уровень случайности в генерации
    num_return_sequences=1
)

# Декодирование и вывод результата
generated_sequence = output_sequences[0].tolist()
text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
print(text)