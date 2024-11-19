import os

def version():
    version_file = os.path.join("mercurydsa", "__init__.py")
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
            
def mercurydsa_version():
    print(version())