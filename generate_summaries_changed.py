from data_changed import load_data, save_to_json
from models import get_summary

xsum_articles, xsum_keys = load_data("xsum")
cnn_articles, cnn_keys = load_data("cnn")

main_models = ["gpt4","gpt35","claude"]
'''xsum_models_gpt35 = [
    "xsum_2_ft_gpt35",
    "xsum_10_ft_gpt35",
    "xsum_500_ft_gpt35",
    "xsum_always_1_ft_gpt35",
    "xsum_random_ft_gpt35",
    "xsum_readability_ft_gpt35",
    "xsum_length_ft_gpt35",
    "xsum_vowelcount_ft_gpt35",
]
cnn_models_gpt35 = [
    "cnn_2_ft_gpt35",
    "cnn_10_ft_gpt35",
    "cnn_500_ft_gpt35",
    "cnn_always_1_ft_gpt35",
    "cnn_random_ft_gpt35",
    "cnn_readability_ft_gpt35",
    "cnn_length_ft_gpt35",
    "cnn_vowelcount_ft_gpt35",
]

xsum_models_llama = [
    "xsum_2_ft_llama",
    "xsum_10_ft_llama",
    "xsum_500_ft_llama",
    "xsum_always_1_ft_llama",
    "xsum_random_ft_llama",
    "xsum_readability_ft_llama",
    "xsum_length_ft_llama",
    "xsum_vowelcount_ft_llama",
]
cnn_models_llama = [
    "cnn_2_ft_llama",
    "cnn_10_ft_llama",
    "cnn_500_ft_llama",
    "cnn_always_1_ft_llama",
    "cnn_random_ft_llama",
    "cnn_readability_ft_llama",
    "cnn_length_ft_llama",
    "cnn_vowelcount_ft_llama",
]'''

models = (
    main_models
)

print("Starting...")
for model in models:
    results = {}
    for key in xsum_keys:
        results[key] = get_summary(xsum_articles[key], "xsum", model)
        save_to_json(results, f"summaries/xsum/{model}_responses.json")
        #print(f"summaries/xsum/{model}_responses.json")

    results = {}
    for key in cnn_keys:
        results[key] = get_summary(cnn_articles[key], "cnn", model)
        save_to_json(results, f"summaries/cnn/{model}_responses.json")
        #print(f"summaries/cnn/{model}_responses.json")
    print(model, "done!")

print("Done!")
