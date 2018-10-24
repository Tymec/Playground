import glob
import os


def main():
    os.chdir("F:/Downloads")
    extensions = ["*.jpg_large", "*.png_large", "*.jpg_orig"]
    file_list = list()

    for extension in extensions:
        file_list = file_list + glob.glob(extension)

    for file in file_list:
        for extension in extensions:
            new_extension = extension.replace('*', '')
            if file.endswith(new_extension):
                new_name = file.replace(new_extension, '') + ".jpg"
                os.rename(file, new_name)

    print("Done!")


if __name__ == __name__:
    main()
