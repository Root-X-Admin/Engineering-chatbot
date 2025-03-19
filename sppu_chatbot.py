# SPPU Engineering Branch Chatbot (CLI-based)
# This chatbot allows users to navigate through branches, years, semesters, and subjects.

sppu_data = {
    "1": {"name": "Computer Engineering", "years": {
        "2": {"name": "Second Year", "semesters": {
            "1": {"name": "Sem 1", "subjects": {
                "1": {"name": "Data Structures", "units": ["Arrays & Linked Lists", "Stacks & Queues", "Trees", "Graphs", "Sorting & Searching"]},
                "2": {"name": "Discrete Mathematics", "units": ["Sets & Relations", "Graph Theory", "Combinatorics", "Boolean Algebra", "Recurrence Relations"]}
            }},
            "2": {"name": "Sem 2", "subjects": {
                "1": {"name": "Object Oriented Programming", "units": ["Classes & Objects", "Inheritance", "Polymorphism", "Exception Handling", "File Handling"]},
                "2": {"name": "Computer Networks", "units": ["Network Models", "IP Addressing", "Routing", "Transport Layer", "Network Security"]}
            }}
        }}
    }},
    "2": {"name": "Mechanical Engineering", "years": {
        "2": {"name": "Second Year", "semesters": {
            "1": {"name": "Sem 1", "subjects": {
                "1": {"name": "Thermodynamics", "units": ["Laws of Thermodynamics", "Entropy", "Steam Boilers", "Gas Turbines", "Refrigeration Cycles"]},
                "2": {"name": "Fluid Mechanics", "units": ["Fluid Properties", "Flow Equations", "Hydrostatics", "Turbulence", "Pumps & Turbines"]}
            }},
            "2": {"name": "Sem 2", "subjects": {
                "1": {"name": "Machine Design", "units": ["Material Properties", "Stress Analysis", "Gears & Bearings", "Shaft Design", "Springs & Couplings"]},
                "2": {"name": "Manufacturing Process", "units": ["Casting", "Forming", "Machining", "Welding", "Additive Manufacturing"]}
            }}
        }}
    }}
}

def chatbot():
    print("\n🤖 Welcome to the SPPU Engineering Chatbot!")
    
    # Select Branch
    print("\nSelect your branch:")
    for key, value in sppu_data.items():
        print(f"{key}. {value['name']}")
    
    branch_choice = input("\nEnter the number of your branch: ")
    if branch_choice not in sppu_data:
        print("Invalid branch choice. Exiting.")
        return

    branch = sppu_data[branch_choice]
    
    # Select Year
    print("\nSelect your year:")
    for key, value in branch["years"].items():
        print(f"{key}. {value['name']}")
    
    year_choice = input("\nEnter the number of your year: ")
    if year_choice not in branch["years"]:
        print("Invalid year choice. Exiting.")
        return

    year = branch["years"][year_choice]
    
    # Select Semester
    print("\nSelect your semester:")
    for key, value in year["semesters"].items():
        print(f"{key}. {value['name']}")
    
    sem_choice = input("\nEnter the number of your semester: ")
    if sem_choice not in year["semesters"]:
        print("Invalid semester choice. Exiting.")
        return

    semester = year["semesters"][sem_choice]
    
    # Select Subject
    print("\nSelect your subject:")
    for key, value in semester["subjects"].items():
        print(f"{key}. {value['name']}")
    
    subject_choice = input("\nEnter the number of your subject: ")
    if subject_choice not in semester["subjects"]:
        print("Invalid subject choice. Exiting.")
        return

    subject = semester["subjects"][subject_choice]
    
    # Display Units
    print(f"\n📚 Subject: {subject['name']}")
    print("Units covered in this subject:")
    for i, unit in enumerate(subject["units"], 1):
        print(f"{i}. {unit}")

    print("\n✅ Thank you for using the SPPU Engineering Chatbot!")

if __name__ == "__main__":
    chatbot()
