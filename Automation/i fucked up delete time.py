import json
import os

file_list = 'F:\DRG Modding\Project Generator\FSDTemplateU38P7\Content'
json_info = 'F:\DRG Modding\DRGPacker\JSON\AssetTypes.json'

def delete_files(list, root, file):
    for item in list:
        item = item.split('/')[-1]
        if file == item:
            rm_path = os.path.join(root, file)
            if os.path.exists(rm_path):
                os.remove(rm_path)
                print(f'Removed {rm_path}')
            else: print(f'File does not exist: {rm_path}')

def main():
    with open(json_info) as f:
        asset_types = json.load(f)

    for root, _, files in os.walk(file_list):
        for file in files:
            abp_list = asset_types['/Script/Engine.AnimBlueprintGeneratedClass']
            delete_files(abp_list, root, file)

            # skm_list = asset_types['/Script/Engine.SkeletalMesh']
            # delete_files(skm_list, root, file)

            # phys_list = asset_types['/Script/Engine.PhysicsAsset']
            # delete_files(phys_list, root, file)

            # sm_list = asset_types['/Script/Engine.StaticMesh']
            # delete_files(sm_list, root, file)
            
            # anim_list = asset_types['/Script/Engine.AnimSequence'] + asset_types['/Script/Engine.AnimMontage'] + asset_types['/Script/Engine.AnimComposite']
            # delete_files(anim_list, root, file) 

            # sk_list = asset_types['/Script/Engine.Skeleton']
            # delete_files(sk_list, root, file)

if __name__ == '__main__':
    main()