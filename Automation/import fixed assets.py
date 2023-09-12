import json
import os

project_output = 'F:\DRG Modding\Project Generator\FSDTemplateU38P7\Content'
json_info = 'F:\DRG Modding\DRGPacker\JSON\AssetTypes.json'
fixed_assets = 'F:\DRG Modding\DRGPacker\JSON\Fixed\Temp'

def main():
    with open(json_info) as f:
        assets = json.load(f)

    for root, _, files in os.walk(fixed_assets):
        for file in files:
            for asset_type in assets:
                for asset in assets[asset_type]:
                    asset_name = asset.split('/')[-1]
                    if file.lower() == asset_name.lower():
                        file_path = os.path.join(root, file)
                        new_asset_path = project_output + asset.replace(asset_name, '')
                        if os.path.exists(new_asset_path):
                            os.system(f'copy "{file_path}" "{new_asset_path}"')
                            print(f'Copied {file_path} to {new_asset_path}')
                        else: print(f'File does not exist: {new_asset_path}')
                        break

if __name__ == '__main__':
    main()