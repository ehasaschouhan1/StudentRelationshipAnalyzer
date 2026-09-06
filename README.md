# Student Relationship Analyzer

A Windows-based DML mini project that analyzes mathematical relations between students using concepts from Discrete Mathematics and Logic.

## 📌 Project Overview

Student Relationship Analyzer is a desktop application developed using Python and Tkinter.

The application represents students as elements of a set and relationships between students as ordered pairs. It analyzes the entered relation using important mathematical properties of relations.

The project also uses SQLite database storage so that student and relation data can be saved permanently.

## 🎯 Objectives

* Represent students as elements of a set.
* Represent relationships using ordered pairs.
* Store student and relation data using SQLite.
* Analyze mathematical properties of relations.
* Display the relation in matrix form.
* Provide a simple and user-friendly Windows GUI.
* Package the Python application as a standalone Windows `.exe` software.

## 🧠 DML Concepts Used

The project demonstrates the following concepts:

### 1. Relation

A relation is represented as a set of ordered pairs.

Example:

```text
R = {(A,B), (B,C), (C,A)}
```

### 2. Reflexive Relation

A relation is reflexive if every element is related to itself.

Example:

```text
(A,A), (B,B), (C,C)
```

### 3. Symmetric Relation

A relation is symmetric if:

```text
(A,B) ∈ R  ⇒  (B,A) ∈ R
```

### 4. Antisymmetric Relation

A relation is antisymmetric if:

```text
(A,B) ∈ R and (B,A) ∈ R  ⇒  A = B
```

### 5. Transitive Relation

A relation is transitive if:

```text
(A,B) ∈ R and (B,C) ∈ R  ⇒  (A,C) ∈ R
```

### 6. Equivalence Relation

A relation is an equivalence relation when it is:

* Reflexive
* Symmetric
* Transitive

### 7. Partial Order Relation

A relation is a partial order when it is:

* Reflexive
* Antisymmetric
* Transitive

## 🖥️ Features

* Dashboard with student and relation statistics
* Add new students
* View all students
* Delete students
* Add relationships between students
* View all relationships
* Delete relationships
* Analyze relation properties
* Check Reflexivity
* Check Symmetry
* Check Antisymmetry
* Check Transitivity
* Check Equivalence Relation
* Check Partial Order Relation
* Generate relation matrix
* Persistent SQLite database storage
* Standalone Windows `.exe`

## 🛠️ Technologies Used

* Python
* Tkinter
* SQLite
* PyInstaller
* Git
* GitHub

## 📂 Project Structure

```text
StudentRelationshipAnalyzer/
│
├── main.py
├── database.py
├── README.md
│
└── dist/
    └── StudentRelationshipAnalyzer.exe
```

## ⚙️ How to Run

### Run from Python Source Code

Make sure Python is installed.

Open the project folder in VS Code and run:

```bash
python main.py
```

### Run the Windows Software

Navigate to:

```text
dist/StudentRelationshipAnalyzer.exe
```

Double-click the `.exe` file to launch the application.

## 💾 Database

The project uses SQLite for permanent data storage.

### Students Table

Stores:

* Student ID
* Student Name
* Roll Number

### Relations Table

Stores:

* Relation ID
* First Student
* Second Student

This allows student and relation data to remain available after closing and reopening the application.

## 🔢 Relation Matrix

The application represents a relation using a matrix.

For students:

```text
A, B, C
```

If:

```text
(A,B) ∈ R
```

the corresponding matrix position contains `1`.

Otherwise, it contains `0`.

Example:

```text
    A B C
A   1 1 0
B   0 1 1
C   0 0 1
```

## 🔍 Relation Analysis

The application automatically checks whether the entered relation satisfies:

* Reflexive
* Symmetric
* Antisymmetric
* Transitive
* Equivalence Relation
* Partial Order Relation

The application also provides details about missing or violating ordered pairs where applicable.

## 🏗️ Application Development

The application was developed using Python and Tkinter for the graphical user interface.

SQLite was integrated for database management and persistent data storage.

PyInstaller was used to package the Python application into a standalone Windows executable.

## 🚀 Future Improvements

Possible future enhancements include:

* Graphical visualization of relationships
* Graph representation of students
* Search and filtering
* Export analysis results
* PDF report generation
* Improved UI themes
* Multiple relation types
* User authentication

## 📄 Project Type

**Discrete Mathematics and Logic Mini Project**

**Project:** Student Relationship Analyzer using RELATION

## 📜 License

This project is created for educational and academic purposes.
