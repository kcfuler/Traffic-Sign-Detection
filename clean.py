import os
import glob

# 删除根目录下的PNG文件
png_files = glob.glob('*.png')
for file in png_files:
    try:
        os.remove(file)
        print(f"Deleted: {file}")
    except:
        print(f"Failed to delete: {file}")

# 删除output目录下的所有文件
if os.path.exists('output'):
    files = os.listdir('output')
    for file in files:
        try:
            os.remove(os.path.join('output', file))
            print(f"Deleted: output/{file}")
        except:
            print(f"Failed to delete: output/{file}")
