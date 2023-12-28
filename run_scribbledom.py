import subprocess
import sys
import json
import shutil

config_file_path = sys.argv[1]
is_expert = sys.argv[2].lower() == "expert"

subprocess.run(
    f"Rscript get_genex_data_from_10x_h5.R {config_file_path}", shell=True)

print("========================================")
print("Genex data extracted from 10x h5 file")

config = None
with open(config_file_path) as f:
    config = json.load(f)
if config is None:
    raise Exception("No config file found")
else:
    # move scribbles
    for sample in config["samples"]:
        shutil.copyfile(f"{config['expert_scribble']}/{config['dataset']}/{sample}/manual_scribble.csv",
                        f"{config['preprocessed_data_folder']}/{config['dataset']}/{sample}/manual_scribble.csv")
        shutil.copyfile(f"{config['manual_annotation']}/{config['dataset']}/{sample}/manual_annotations.csv",
                        f"{config['preprocessed_data_folder']}/{config['dataset']}/{sample}/manual_annotations.csv")
    print("========================================")
    print("Scribbles moved to preprocessed data folder")

subprocess.run(
    f"python visium_data_to_matrix_representation_converter.py --params {config_file_path}", shell=True)
print("========================================")
print("Data convertend in matrix representation")
if is_expert:
    subprocess.run(
        f"python scribble_dom.py --params {config_file_path}", shell=True)
else:
    subprocess.run(
        f"python autoscribble_dom.py --params {config_file_path}", shell=True)
print("========================================")
print("Model run complete")
subprocess.run(
    f"python best_model_estimator.py --params {config_file_path}", shell=True)
print("========================================")
print("Best model evaluated with goodness score")
subprocess.run(
    f"python show_results.py --params {config_file_path}", shell=True)
