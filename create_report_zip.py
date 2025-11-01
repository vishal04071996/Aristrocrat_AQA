import zipfile
import os
from datetime import datetime

def zip_test_results():
    # timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"AQA_Test_Report_{timestamp}.zip"

    # folders and files to include
    paths_to_include = [
        "report.html",
        "reports",
        "screenshot",
        "documentation.docx"  # or documentation.pdf
    ]

    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for path in paths_to_include:
            if os.path.exists(path):
                if os.path.isfile(path):
                    zipf.write(path)
                else:
                    for foldername, subfolders, filenames in os.walk(path):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            arcname = os.path.relpath(file_path, os.path.dirname(path))
                            zipf.write(file_path, arcname)
    print(f"✅ ZIP file created successfully: {output_filename}")

if __name__ == "__main__":
    zip_test_results()
