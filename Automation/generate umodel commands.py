import os
import subprocess

CONTENT_PATH = "F:\\DRG Modding\\DRGPacker\\_unpacked\\FSD\\Content"
OUTPUT_PATH = "F:\\DRG Modding\\DRGPacker\\JSON\\Animation Stuff\\UModel Export\\Test Missing Anims"
UMODEL_EXE = "F:\\DRG Modding\\DRGTools\\UModel\\umodel.exe"

def main():
    with open("Automation\missing_anims.txt", "r") as f:
        files = f.readlines()
    files = [x.strip() for x in files]
    names = [x.split("\\")[-1].replace('.uasset', '.psa') for x in files]

    for missing_anim in files:
        missing_anim = missing_anim.replace("Content", CONTENT_PATH)
        missing_anim = missing_anim.replace("/", "\\")
        missing_anim = missing_anim.replace(missing_anim.split("\\")[-1], "")
        out_path = missing_anim.replace(CONTENT_PATH, OUTPUT_PATH)

        output = subprocess.Popen([
            UMODEL_EXE,
            f'-path="{missing_anim}"',
            "-game=ue4.27",
            f'-out="{out_path}"',
            "-nooverwrite",
            "-nostat",
            "-novert",
            "-notex",
            "-nomorph",
            "-nolightmap",
            "-export",
            "*.uasset"
        ], shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
        print(output)

        # if the output contains text that says 'WARNING: Import(Skeleton'', then the skeleton is missing
        # get the skeleton path from the output and then rerun the umodel command with the path starting at the skeleton path
        found = False
        while not found:
            if "WARNING: Import(Skeleton" in output:
                skeleton_path = output.split("WARNING: Import(Skeleton'")[1].split("'):")[1].split("was not found")[0].strip().replace('package ', '')
                skeleton_path = skeleton_path.replace("Content", CONTENT_PATH)
                skeleton_path = skeleton_path.replace("/", "\\")
                skeleton_path = skeleton_path.replace(skeleton_path.split("\\")[-1], "")
                skeleton_path = skeleton_path.replace("\\Game", CONTENT_PATH, 1)
                out_path = skeleton_path.replace(CONTENT_PATH, OUTPUT_PATH)
                
                output = subprocess.Popen([
                    UMODEL_EXE,
                    f'-path="{skeleton_path}"',
                    "-game=ue4.27",
                    f'-out="{out_path}"',
                    "-nooverwrite",
                    "-nostat",
                    "-novert",
                    "-notex",
                    "-nomorph",
                    "-nolightmap",
                    "-export",
                    "*.uasset"
                ], shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
                print(output)
            else:
                found = True
                print('found')

        for root, _, all_files in os.walk(out_path):
            for file in all_files:
                if file.startswith("ANIM_") and not file.endswith(".fbx"):
                    if file not in names:
                        print(os.path.join(root, file))
                        os.remove(os.path.join(root, file))

if __name__ == "__main__":
    main()