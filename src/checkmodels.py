import google.generativeai as genai

genai.configure(api_key="AIzaSyBUo_-3iX4SHuUfioLh5LJITK0-7sjWjRk")

# Convert generator to list
models = list(genai.list_models())

# Print model names
for model in models:
    print(model.name)
