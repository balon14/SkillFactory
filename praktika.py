from transformers import pipeline

classifier = pipiline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

classifier("Я обожаю инженерию машинного обучения!")
