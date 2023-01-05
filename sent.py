from transformers import pipline

classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
classifier("Я обожаю инженерия машинного обучения!")
