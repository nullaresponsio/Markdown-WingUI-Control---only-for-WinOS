import os

pip_exe = r"C:\Users\bshan\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\pip3.13.exe"
site_packages = os.path.join(os.path.dirname(pip_exe), "Lib", "site-packages")
os.makedirs(site_packages, exist_ok=True)
