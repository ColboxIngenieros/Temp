from importlib import resources

#file_path, file_name = "math_lib.res", "VariasLineas.txt"

file_path = resources.files("math_lib.res").joinpath("VariasLineas.txt")
with resources.as_file(file_path) as txt_path:
    with open(txt_path) as file:
        print(file.readlines())