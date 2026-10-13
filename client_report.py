from datetime import datetime

print("===== CLIENT REPORT GENERATOR =====")

client_name = input("Enter client name: ")
project_name = input("Enter project name: ")
work_done = input("Describe the work completed: ")
status = input("Project status: ")

report = f"""
CLIENT PROJECT REPORT
=====================
Client Name: {client_name}
Project Name: {project_name}
Work Completed: {work_done}
Project Status: {status}
Report Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}
"""

filename = "client_report.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(report)

print("Report generated successfully!")
print("File saved as:", filename)
