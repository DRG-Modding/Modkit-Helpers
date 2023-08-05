import json
import os

files_to_copy = 'F:\DRG Modding\Project Generator\FSDTemplateU37P8-all\Content'
destination = 'F:\DRG Modding\Project Generator\FSDTemplateU38P3\Content'
json_info = 'F:\DRG Modding\DRGPacker\JSON\AssetTypes.json'
additive_paths = 'F:\DRG Modding\DRGPacker\JSON\Automation\Additives.txt'
new_anims = 'F:\\DRG Modding\\DRGPacker\\JSON\\Automation\\NewAnims.txt'

def main():
    with open(json_info) as f:
        asset_types = json.load(f)

    with open(additive_paths) as f:
        additives = f.readlines()

    anim_list = asset_types['/Script/Engine.AnimSequence']
    for additive in additives:
        additive = additive.strip() + '.uasset'
        if additive in anim_list: anim_list.remove(additive)

    existing_anims = []
    for root, _, files in os.walk(files_to_copy):
        for file in files:
            if not file.endswith('.uasset'): continue
            for item in anim_list:
                if file == item.split('/')[-1]:
                    existing_anims.append(item)
                    copy_path = os.path.join(root, file)
                    if os.path.exists(copy_path):
                        dir = destination + item.replace(item.split('/')[-1], '')
                        if not os.path.exists(dir): 
                            os.makedirs(dir)
                            print(f'Created directory: {dir}')
                        os.system(f'copy "{copy_path}" "{destination + item}"')
                        print(f'Copied {copy_path} to {destination + item}')
                    else: 
                        print(f'File does not exist: {copy_path}')

    # compare existing anims to anim list
    # any that are in anim list but not in existing anims are new anims, write to file
    # with open(new_anims, 'w') as f:
    #     for anim in anim_list:
    #         if anim not in existing_anims:
    #             f.write(anim + '\n')

if __name__ == '__main__':
    main()