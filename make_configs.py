import json

base_config_path = "config.json"
config = None
with open(base_config_path) as f:
    config = json.load(f)
if config is None:
    raise Exception("No config file found")
else:
    is_expert_choice = [True, False]
    samples_choice = [
        "151507",
        "151508",
        "151509",
        "151510",
        "151669",
        "151670",
        "151671",
        "151672",
        "151673",
        "151674",
        "151675",
        "151676"
    ]

    for is_expert in is_expert_choice:
        for sample in samples_choice:
            config['schema'] = "expert" if is_expert else "mclust"
            config['samples'] = [sample]
            config_path_name = f"config_{sample}_{'expert' if is_expert else 'mclust'}.json"
            with open(config_path_name, 'w') as f:
                json.dump(config, f, indent=4)
            print(f"Created config file {config_path_name}")
