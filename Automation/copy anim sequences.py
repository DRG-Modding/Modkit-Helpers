import json
import os

input_list = 'F:\DRG Modding\Project Generator\FSDTemplateU38P7\Content'
json_info = 'F:\DRG Modding\DRGPacker\JSON\AssetTypes.json'
output_path = 'F:\DRG Modding\DRGPacker\JSON\OutputAnims'

def main():
    with open(json_info) as f:
        asset_types = json.load(f)

    for root, _, files in os.walk(input_list):
        for file in files:
            anim_list = asset_types['/Script/Engine.AnimSequence']
            for item in anim_list:
                item = item.split('/')[-1]
                if file == item:
                    rm_path = os.path.join(root, file)
                    if os.path.exists(rm_path):
                        print(f'Copying {rm_path} to {output_path}')
                        os.system(f'copy "{rm_path}" "{output_path}"')
                    else: print(f'File does not exist: {rm_path}')

if __name__ == '__main__':
    main()