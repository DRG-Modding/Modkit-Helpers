import os

IN_PATH = "F:\\DRG Modding\\DRGPacker\\JSON\\Animation Stuff\\#placeholder#\\FSD\\Content"
OUT_PATH = "F:\\DRG Modding\\DRGPacker\\JSON\\Assets\\Game"
#TYPES = ["AnimSeqs", "AnimComps", "AnimMonts", "SKMs", "SMs"]
TYPES = ["Anims", "SKMs", "SMs"]

def main():
    for type in TYPES:
        type_path = IN_PATH.replace("#placeholder#", type)
        for root, _, files in os.walk(type_path):
            for file in files:
                if file.endswith(".fbx"):
                    print(os.path.join(root, file))
                    print(os.path.join(root, file).replace(type_path, OUT_PATH))
                    os.makedirs(os.path.join(root, file).replace(type_path, OUT_PATH).replace(file, ""), exist_ok=True)
                    os.system(f'copy "{os.path.join(root, file)}" "{os.path.join(root, file).replace(type_path, OUT_PATH)}" /Y')

if __name__ == "__main__":
    main()