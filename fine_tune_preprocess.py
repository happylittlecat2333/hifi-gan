import argparse
import os

def main(args, split=500):
    dataset = args.dataset
    path = args.path
    save_dir = os.path.join("dataset", dataset)
    print(save_dir)
    os.makedirs(save_dir, exist_ok=True)
    file_name = []
    for file in os.listdir(os.path.join(path, dataset, "wav")):
        if file.endswith(".wav"):
            file_name.append(file.split(".wav")[0])

    with open(os.path.join(save_dir, "training.txt"), "w") as f:
        for name in file_name[split:]:
            f.write(name + "\n")

    with open(os.path.join(save_dir, "validation.txt"), "w") as f:
        for name in file_name[:split]:
            f.write(name + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()
    main(args)

"""

python fine_tune_preprocess.py --dataset LJSpeech_v3 --path /home/xjl/Audio/Library/Models/MyFastSpeech2/preprocessed_data/

"""