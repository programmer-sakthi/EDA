import os
import pandas as pd
import sweetviz as sv

# --- Configuration ---
# Change this to the actual full path of your CSV file
csv_path = r"d:\College\5th sem\Professional Electives\EDA\python\Assignment\Problem 2\DA314_S8_EmployeeAttrition_Data_Practice.csv"

# --- Check if file exists ---
if not os.path.exists(csv_path):
    print(f"❌ File not found: {csv_path}")
    print("👉 Please check the path and try again.")
else:
    # --- Read CSV safely ---
    try:
        df = pd.read_csv(
            csv_path,
            encoding="latin1",
            engine="python",
            on_bad_lines="skip",
        )

        # --- Generate Sweetviz report ---
        report = sv.analyze(df)
        output_path = "SWEETVIZ_REPORT.html"
        report.show_html(output_path)

        print(f"✅ Sweetviz report saved as: {os.path.abspath(output_path)}")

    except Exception as e:
        print("⚠️ Error reading or analyzing the CSV:")
        print(e)
