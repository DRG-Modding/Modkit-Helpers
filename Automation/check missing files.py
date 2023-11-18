import os

generated_files = 'F:\DRG Modding\Project Generator\FSDTemplateU38P10-all\Content'
unpacked_files = 'F:\DRG Modding\DRGPacker\_unpacked\FSD\Content'
serialized_files = 'F:\DRG Modding\DRGPacker\JSON\Assets\Game'

def main():
    file_list = []
    for root, _, files in os.walk(generated_files):
        for file in files:
            if not file.endswith('.uasset'): continue
            if os.path.exists(os.path.join(root, file.replace('.uasset', '.uexp'))): continue
            file_list.append(file.replace('.uasset', ''))

    with open('Automation\missing_files_serialized.txt', 'w') as f:
        for root, _, files in os.walk(serialized_files):
            for file in files:
                if not file.endswith('.json'): continue
                if file.replace('.json', '') not in file_list:
                    print(f'File does not exist in project: {os.path.join(root, file.replace(".json", ".uasset"))}')
                    f.write(f'{os.path.join(root, file.replace(".json", ".uasset"))}\n')

if __name__ == '__main__':
    main()