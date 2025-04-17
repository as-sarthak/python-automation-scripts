import os

folder_path = 'your_folder_path_here'
prefix = 'img'

for count, filename in enumerate(os.listdir(folder_path)):
    new_name = f"{prefix}_{count + 1}.jpg"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)

print("All files renamed successfully!")
