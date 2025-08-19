This is a simple Python-based simulation of a university registration system that models the registration process for students and teachers across multiple departments, programs, and subjects.

Project Structure:

Student and Teacher classes to create users and manage registrations.

Depart class hierarchy for organizing Engineering and Business departments.

RegistryStudent and RegistryTeacher handle department-level registration logic.

JSON files (data/programs.json, data/subjects.json) store mappings for programs and subjects.

Auto-generates student numbers based on: year of study program ID registration order

Tracks student counts by (program, grade) combination.

Teachers are registered to all departments that offer the subjects they teach.

How It Works:

Students are registered by name, grade, and program. Their department is derived from the program.

Teachers are registered by name, salary, and the subjects they teach. Their department(s) are determined from the subjects.

The system uses dictionaries and default structures to maintain bidirectional relationships between names and IDs for subjects/programs.
