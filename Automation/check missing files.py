import os

generated_files = 'F:\DRG Modding\Project Generator\FSDTemplateU38P3\Content'
unpacked_files = 'F:\DRG Modding\DRGPacker\_unpacked\FSD\Content'

def main():
    for root, _, files in os.walk(unpacked_files):
        for file in files:
            if not file.endswith('.uasset'): continue
            unpacked_file = os.path.join(root, file)
            generated_file = unpacked_file.replace(unpacked_files, generated_files)
            if not os.path.exists(generated_file):
                print(f'File does not exist: {generated_file}')

if __name__ == '__main__':
    main()