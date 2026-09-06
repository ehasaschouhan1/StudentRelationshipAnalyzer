import tkinter as tk
from tkinter import ttk, messagebox
from database import Database


class StudentRelationshipAnalyzer:

    def __init__(self, root):
        self.root = root

        self.root.title("Student Relationship Analyzer")
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        # Database
        self.db = Database()

        self.create_styles()
        self.create_header()
        self.create_dashboard()

        self.update_counts()

    # =========================================================
    # STYLING
    # =========================================================

    def create_styles(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#1f2937",
            height=90
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Student Relationship Analyzer",
            font=("Segoe UI", 23, "bold"),
            bg="#1f2937",
            fg="white"
        ).pack(pady=(14, 2))

        tk.Label(
            header,
            text="DML Mini Project • Analysis of Relations",
            font=("Segoe UI", 10),
            bg="#1f2937",
            fg="#d1d5db"
        ).pack()

    # =========================================================
    # DASHBOARD
    # =========================================================

    def create_dashboard(self):

        main = tk.Frame(
            self.root,
            bg="#f3f4f6"
        )

        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="Dashboard",
            font=("Segoe UI", 21, "bold"),
            bg="#f3f4f6",
            fg="#111827"
        ).pack(pady=(25, 4))

        tk.Label(
            main,
            text="Manage students, create relations and analyze their mathematical properties.",
            font=("Segoe UI", 10),
            bg="#f3f4f6",
            fg="#4b5563"
        ).pack()

        # Statistics
        cards = tk.Frame(
            main,
            bg="#f3f4f6"
        )

        cards.pack(pady=25)

        self.student_count = tk.StringVar(value="0")
        self.relation_count = tk.StringVar(value="0")

        self.create_card(
            cards,
            "TOTAL STUDENTS",
            self.student_count,
            0
        )

        self.create_card(
            cards,
            "TOTAL RELATIONS",
            self.relation_count,
            1
        )

        # Buttons
        buttons = tk.Frame(
            main,
            bg="#f3f4f6"
        )

        buttons.pack(pady=10)

        self.create_button(
            buttons,
            "Add Student",
            self.add_student,
            "#2563eb",
            0,
            0
        )

        self.create_button(
            buttons,
            "View Students",
            self.view_students,
            "#374151",
            0,
            1
        )

        self.create_button(
            buttons,
            "Add Relation",
            self.add_relation,
            "#059669",
            1,
            0
        )

        self.create_button(
            buttons,
            "View Relations",
            self.view_relations,
            "#0891b2",
            1,
            1
        )

        self.create_button(
            buttons,
            "Analyze Relation",
            self.analyze_relation,
            "#7c3aed",
            2,
            0
        )

        self.create_button(
            buttons,
            "Relation Matrix",
            self.show_matrix,
            "#dc2626",
            2,
            1
        )

        # Delete buttons
        self.create_button(
            buttons,
            "Delete Student",
            self.delete_student,
            "#b45309",
            3,
            0
        )

        self.create_button(
            buttons,
            "Delete Relation",
            self.delete_relation,
            "#be123c",
            3,
            1
        )

        tk.Label(
            main,
            text="Data is stored permanently using SQLite Database",
            font=("Segoe UI", 9),
            bg="#f3f4f6",
            fg="#6b7280"
        ).pack(
            side="bottom",
            pady=15
        )

    # =========================================================
    # CARD
    # =========================================================

    def create_card(self, parent, title, variable, column):

        card = tk.Frame(
            parent,
            bg="white",
            width=240,
            height=105,
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )

        card.grid(
            row=0,
            column=column,
            padx=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            bg="white",
            fg="#6b7280"
        ).pack(pady=(15, 3))

        tk.Label(
            card,
            textvariable=variable,
            font=("Segoe UI", 25, "bold"),
            bg="white",
            fg="#111827"
        ).pack()

    # =========================================================
    # BUTTON
    # =========================================================

    def create_button(
        self,
        parent,
        text,
        command,
        background,
        row,
        column
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=background,
            fg="white",
            width=20,
            height=2,
            relief="flat",
            cursor="hand2",
            activebackground=background,
            activeforeground="white"
        )

        button.grid(
            row=row,
            column=column,
            padx=10,
            pady=6
        )

    # =========================================================
    # ADD STUDENT
    # =========================================================

    def add_student(self):

        window = tk.Toplevel(self.root)

        window.title("Add Student")
        window.geometry("430x350")
        window.resizable(False, False)

        tk.Label(
            window,
            text="Add Student",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=20)

        tk.Label(
            window,
            text="Student Name",
            font=("Segoe UI", 10)
        ).pack()

        name_entry = tk.Entry(
            window,
            font=("Segoe UI", 11),
            width=32
        )

        name_entry.pack(pady=8)

        tk.Label(
            window,
            text="Roll Number",
            font=("Segoe UI", 10)
        ).pack()

        roll_entry = tk.Entry(
            window,
            font=("Segoe UI", 11),
            width=32
        )

        roll_entry.pack(pady=8)

        def save_student():

            name = name_entry.get().strip()
            roll = roll_entry.get().strip()

            if not name or not roll:

                messagebox.showwarning(
                    "Missing Information",
                    "Please enter both student name and roll number."
                )

                return

            student_id = self.db.add_student(
                name,
                roll
            )

            if student_id is None:

                messagebox.showerror(
                    "Duplicate Roll Number",
                    "This roll number already exists."
                )

                return

            self.update_counts()

            messagebox.showinfo(
                "Success",
                f"Student '{name}' added successfully."
            )

            window.destroy()

        tk.Button(
            window,
            text="Save Student",
            command=save_student,
            font=("Segoe UI", 10, "bold"),
            bg="#2563eb",
            fg="white",
            width=20,
            height=2,
            relief="flat"
        ).pack(pady=25)

        name_entry.focus()

    # =========================================================
    # VIEW STUDENTS
    # =========================================================

    def view_students(self):

        students = self.db.get_students()

        window = tk.Toplevel(self.root)

        window.title("Student List")
        window.geometry("650x500")

        tk.Label(
            window,
            text="Student List",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=15)

        if not students:

            tk.Label(
                window,
                text="No students added yet.",
                font=("Segoe UI", 11),
                fg="#6b7280"
            ).pack(pady=40)

            return

        frame = tk.Frame(window)

        frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        columns = (
            "number",
            "name",
            "roll"
        )

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        tree.heading(
            "number",
            text="#"
        )

        tree.heading(
            "name",
            text="Student Name"
        )

        tree.heading(
            "roll",
            text="Roll Number"
        )

        tree.column(
            "number",
            width=60,
            anchor="center"
        )

        tree.column(
            "name",
            width=350
        )

        tree.column(
            "roll",
            width=150,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        for index, student in enumerate(
            students,
            start=1
        ):

            tree.insert(
                "",
                "end",
                values=(
                    index,
                    student[1],
                    student[2]
                )
            )

    # =========================================================
    # ADD RELATION
    # =========================================================

    def add_relation(self):

        students = self.db.get_students()

        if len(students) < 2:

            messagebox.showwarning(
                "Not Enough Students",
                "Please add at least two students first."
            )

            return

        window = tk.Toplevel(self.root)

        window.title("Add Relation")
        window.geometry("480x420")
        window.resizable(False, False)

        tk.Label(
            window,
            text="Create Student Relation",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=20)

        student_map = {}

        for student in students:

            label = f"{student[1]} ({student[2]})"

            student_map[label] = student[0]

        names = list(student_map.keys())

        tk.Label(
            window,
            text="Student A",
            font=("Segoe UI", 10)
        ).pack()

        student_a = ttk.Combobox(
            window,
            values=names,
            state="readonly",
            width=35
        )

        student_a.pack(pady=10)

        tk.Label(
            window,
            text="Student B",
            font=("Segoe UI", 10)
        ).pack()

        student_b = ttk.Combobox(
            window,
            values=names,
            state="readonly",
            width=35
        )

        student_b.pack(pady=10)

        tk.Label(
            window,
            text="Relation: Student A  →  Student B",
            font=("Segoe UI", 9),
            fg="#6b7280"
        ).pack(pady=5)

        tk.Label(
            window,
            text="Self-relations are allowed for reflexive testing.",
            font=("Segoe UI", 9),
            fg="#2563eb"
        ).pack(pady=5)

        def save_relation():

            a = student_a.get()
            b = student_b.get()

            if not a or not b:

                messagebox.showwarning(
                    "Missing Information",
                    "Please select both students."
                )

                return

            relation_id = self.db.add_relation(
                student_map[a],
                student_map[b]
            )

            if relation_id is None:

                messagebox.showwarning(
                    "Relation Already Exists",
                    "This ordered pair already exists."
                )

                return

            self.update_counts()

            messagebox.showinfo(
                "Success",
                f"Relation created successfully:\n\n{a}  →  {b}"
            )

            window.destroy()

        tk.Button(
            window,
            text="Add Relation",
            command=save_relation,
            font=("Segoe UI", 10, "bold"),
            bg="#059669",
            fg="white",
            width=20,
            height=2,
            relief="flat"
        ).pack(pady=20)

    # =========================================================
    # GET RELATION DATA
    # =========================================================

    def get_relation_pairs(self):

        relations = self.db.get_relations()

        pairs = []

        for relation in relations:

            relation_id = relation[0]

            a_name = relation[1]
            a_roll = relation[2]

            b_name = relation[3]
            b_roll = relation[4]

            a_label = f"{a_name} ({a_roll})"
            b_label = f"{b_name} ({b_roll})"

            pairs.append(
                (
                    relation_id,
                    a_label,
                    b_label
                )
            )

        return pairs

    # =========================================================
    # VIEW RELATIONS
    # =========================================================

    def view_relations(self):

        relations = self.get_relation_pairs()

        if not relations:

            messagebox.showinfo(
                "No Relations",
                "No relations have been created yet."
            )

            return

        window = tk.Toplevel(self.root)

        window.title("Relation Pairs")
        window.geometry("750x500")

        tk.Label(
            window,
            text="Relation Pairs",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=15)

        frame = tk.Frame(window)

        frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        columns = (
            "number",
            "student_a",
            "arrow",
            "student_b"
        )

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        tree.heading(
            "number",
            text="#"
        )

        tree.heading(
            "student_a",
            text="Student A"
        )

        tree.heading(
            "arrow",
            text=""
        )

        tree.heading(
            "student_b",
            text="Student B"
        )

        tree.column(
            "number",
            width=50,
            anchor="center"
        )

        tree.column(
            "student_a",
            width=270
        )

        tree.column(
            "arrow",
            width=60,
            anchor="center"
        )

        tree.column(
            "student_b",
            width=270
        )

        tree.pack(
            fill="both",
            expand=True
        )

        for index, relation in enumerate(
            relations,
            start=1
        ):

            tree.insert(
                "",
                "end",
                values=(
                    index,
                    relation[1],
                    "→",
                    relation[2]
                )
            )

    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(self):

        students = self.db.get_students()

        if not students:

            messagebox.showinfo(
                "No Students",
                "There are no students to delete."
            )

            return

        window = tk.Toplevel(self.root)

        window.title("Delete Student")
        window.geometry("500x330")
        window.resizable(False, False)

        tk.Label(
            window,
            text="Delete Student",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=20)

        student_map = {}

        for student in students:

            label = f"{student[1]} ({student[2]})"

            student_map[label] = student[0]

        combo = ttk.Combobox(
            window,
            values=list(student_map.keys()),
            state="readonly",
            width=35
        )

        combo.pack(pady=20)

        tk.Label(
            window,
            text="Deleting a student also removes their relations.",
            font=("Segoe UI", 9),
            fg="#b91c1c"
        ).pack(pady=5)

        def confirm_delete():

            selected = combo.get()

            if not selected:

                messagebox.showwarning(
                    "Select Student",
                    "Please select a student."
                )

                return

            answer = messagebox.askyesno(
                "Confirm Delete",
                f"Are you sure you want to delete:\n\n{selected}?"
            )

            if not answer:
                return

            self.db.delete_student(
                student_map[selected]
            )

            self.update_counts()

            messagebox.showinfo(
                "Deleted",
                "Student deleted successfully."
            )

            window.destroy()

        tk.Button(
            window,
            text="Delete Student",
            command=confirm_delete,
            font=("Segoe UI", 10, "bold"),
            bg="#b45309",
            fg="white",
            width=20,
            height=2,
            relief="flat"
        ).pack(pady=25)

    # =========================================================
    # DELETE RELATION
    # =========================================================

    def delete_relation(self):

        relations = self.get_relation_pairs()

        if not relations:

            messagebox.showinfo(
                "No Relations",
                "There are no relations to delete."
            )

            return

        window = tk.Toplevel(self.root)

        window.title("Delete Relation")
        window.geometry("550x350")
        window.resizable(False, False)

        tk.Label(
            window,
            text="Delete Relation",
            font=("Segoe UI", 19, "bold")
        ).pack(pady=20)

        relation_map = {}

        display_values = []

        for relation in relations:

            relation_id = relation[0]

            text = f"{relation[1]}  →  {relation[2]}"

            relation_map[text] = relation_id

            display_values.append(text)

        combo = ttk.Combobox(
            window,
            values=display_values,
            state="readonly",
            width=42
        )

        combo.pack(pady=25)

        def confirm_delete():

            selected = combo.get()

            if not selected:

                messagebox.showwarning(
                    "Select Relation",
                    "Please select a relation."
                )

                return

            answer = messagebox.askyesno(
                "Confirm Delete",
                f"Delete this relation?\n\n{selected}"
            )

            if not answer:
                return

            self.db.delete_relation(
                relation_map[selected]
            )

            self.update_counts()

            messagebox.showinfo(
                "Deleted",
                "Relation deleted successfully."
            )

            window.destroy()

        tk.Button(
            window,
            text="Delete Relation",
            command=confirm_delete,
            font=("Segoe UI", 10, "bold"),
            bg="#be123c",
            fg="white",
            width=20,
            height=2,
            relief="flat"
        ).pack(pady=25)

    # =========================================================
    # GET STUDENT LABELS
    # =========================================================

    def get_student_labels(self):

        students = self.db.get_students()

        return [
            f"{student[1]} ({student[2]})"
            for student in students
        ]

    # =========================================================
    # REFLEXIVE
    # =========================================================

    def is_reflexive(self):

        students = self.get_student_labels()

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for student in students:

            if (student, student) not in relation_set:
                return False

        return True

    # =========================================================
    # SYMMETRIC
    # =========================================================

    def is_symmetric(self):

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in relation_set:

            if (b, a) not in relation_set:
                return False

        return True

    # =========================================================
    # ANTISYMMETRIC
    # =========================================================

    def is_antisymmetric(self):

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in relation_set:

            if a != b and (b, a) in relation_set:
                return False

        return True

    # =========================================================
    # TRANSITIVE
    # =========================================================

    def is_transitive(self):

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in relation_set:

            for c, d in relation_set:

                if b == c:

                    if (a, d) not in relation_set:
                        return False

        return True

    # =========================================================
    # EQUIVALENCE RELATION
    # =========================================================

    def is_equivalence_relation(
        self,
        reflexive,
        symmetric,
        transitive
    ):

        return (
            reflexive
            and symmetric
            and transitive
        )

    # =========================================================
    # PARTIAL ORDER
    # =========================================================

    def is_partial_order(
        self,
        reflexive,
        antisymmetric,
        transitive
    ):

        return (
            reflexive
            and antisymmetric
            and transitive
        )

    # =========================================================
    # MISSING REFLEXIVE PAIRS
    # =========================================================

    def get_missing_reflexive_pairs(self):

        missing = []

        students = self.get_student_labels()

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for student in students:

            if (student, student) not in relation_set:

                missing.append(
                    f"({student}, {student})"
                )

        return missing

    # =========================================================
    # MISSING SYMMETRIC PAIRS
    # =========================================================

    def get_missing_symmetric_pairs(self):

        missing = []

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in sorted(relation_set):

            if (b, a) not in relation_set:

                missing.append(
                    f"({b}, {a})"
                )

        return missing

    # =========================================================
    # ANTISYMMETRIC VIOLATIONS
    # =========================================================

    def get_antisymmetric_violations(self):

        violations = []

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in sorted(relation_set):

            if a != b and (b, a) in relation_set:

                pair = f"({a}, {b})"

                if pair not in violations:

                    violations.append(pair)

        return violations

    # =========================================================
    # TRANSITIVE VIOLATIONS
    # =========================================================

    def get_transitive_violations(self):

        violations = []

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        for a, b in relation_set:

            for c, d in relation_set:

                if b == c:

                    required = (a, d)

                    if required not in relation_set:

                        description = (
                            f"({a}, {b}) and "
                            f"({c}, {d}) require "
                            f"({a}, {d})"
                        )

                        if description not in violations:

                            violations.append(
                                description
                            )

        return violations

    # =========================================================
    # ANALYZE RELATION
    # =========================================================

    def analyze_relation(self):

        students = self.db.get_students()
        relations = self.get_relation_pairs()

        if len(students) == 0:

            messagebox.showwarning(
                "No Students",
                "Please add students first."
            )

            return

        if len(relations) == 0:

            messagebox.showwarning(
                "No Relations",
                "Please add at least one relation first."
            )

            return

        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        equivalence = self.is_equivalence_relation(
            reflexive,
            symmetric,
            transitive
        )

        partial_order = self.is_partial_order(
            reflexive,
            antisymmetric,
            transitive
        )

        window = tk.Toplevel(self.root)

        window.title("Relation Analysis")
        window.geometry("850x700")

        tk.Label(
            window,
            text="Relation Analysis",
            font=("Segoe UI", 21, "bold")
        ).pack(pady=(20, 5))

        tk.Label(
            window,
            text="Mathematical properties of the selected relation",
            font=("Segoe UI", 10),
            fg="#6b7280"
        ).pack()

        result_frame = tk.Frame(window)

        result_frame.pack(
            fill="x",
            padx=30,
            pady=20
        )

        self.add_result_row(
            result_frame,
            "Reflexive",
            reflexive
        )

        self.add_result_row(
            result_frame,
            "Symmetric",
            symmetric
        )

        self.add_result_row(
            result_frame,
            "Antisymmetric",
            antisymmetric
        )

        self.add_result_row(
            result_frame,
            "Transitive",
            transitive
        )

        self.add_result_row(
            result_frame,
            "Equivalence Relation",
            equivalence
        )

        self.add_result_row(
            result_frame,
            "Partial Order Relation",
            partial_order
        )

        details = tk.Text(
            window,
            font=("Consolas", 10),
            height=18,
            wrap="word"
        )

        details.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        details.insert(
            "end",
            "RELATION ANALYSIS DETAILS\n"
        )

        details.insert(
            "end",
            "=" * 70 + "\n\n"
        )

        details.insert(
            "end",
            "RELATION PAIRS:\n"
        )

        for relation in relations:

            details.insert(
                "end",
                f"  ({relation[1]}, {relation[2]})\n"
            )

        details.insert(
            "end",
            "\n"
        )

        # Reflexive
        details.insert(
            "end",
            "REFLEXIVE:\n"
        )

        if reflexive:

            details.insert(
                "end",
                "  ✓ Every student is related to itself.\n\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ Missing self-relations:\n"
            )

            for item in self.get_missing_reflexive_pairs():

                details.insert(
                    "end",
                    f"      {item}\n"
                )

            details.insert(
                "end",
                "\n"
            )

        # Symmetric
        details.insert(
            "end",
            "SYMMETRIC:\n"
        )

        if symmetric:

            details.insert(
                "end",
                "  ✓ For every (A,B), (B,A) also exists.\n\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ Missing reverse pairs:\n"
            )

            for item in self.get_missing_symmetric_pairs():

                details.insert(
                    "end",
                    f"      {item}\n"
                )

            details.insert(
                "end",
                "\n"
            )

        # Antisymmetric
        details.insert(
            "end",
            "ANTISYMMETRIC:\n"
        )

        if antisymmetric:

            details.insert(
                "end",
                "  ✓ No distinct students have relations in both directions.\n\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ Antisymmetry violations found:\n"
            )

            for item in self.get_antisymmetric_violations():

                details.insert(
                    "end",
                    f"      {item}\n"
                )

            details.insert(
                "end",
                "\n"
            )

        # Transitive
        details.insert(
            "end",
            "TRANSITIVE:\n"
        )

        if transitive:

            details.insert(
                "end",
                "  ✓ Relation satisfies transitivity.\n\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ Transitivity violations found:\n"
            )

            for item in self.get_transitive_violations():

                details.insert(
                    "end",
                    f"      {item}\n"
                )

            details.insert(
                "end",
                "\n"
            )

        # Final classification
        details.insert(
            "end",
            "FINAL CLASSIFICATION:\n"
        )

        if equivalence:

            details.insert(
                "end",
                "  ✓ This is an EQUIVALENCE RELATION.\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ This is NOT an equivalence relation.\n"
            )

        if partial_order:

            details.insert(
                "end",
                "  ✓ This is a PARTIAL ORDER RELATION.\n"
            )

        else:

            details.insert(
                "end",
                "  ✗ This is NOT a partial order relation.\n"
            )

        details.config(
            state="disabled"
        )

    # =========================================================
    # RESULT ROW
    # =========================================================

    def add_result_row(
        self,
        parent,
        name,
        result
    ):

        frame = tk.Frame(
            parent,
            bg="white",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )

        frame.pack(
            fill="x",
            pady=3
        )

        tk.Label(
            frame,
            text=name,
            font=("Segoe UI", 10, "bold"),
            bg="white",
            anchor="w",
            width=28
        ).pack(
            side="left",
            padx=15,
            pady=9
        )

        if result:

            text = "✓ YES"
            background = "#166534"

        else:

            text = "✗ NO"
            background = "#b91c1c"

        tk.Label(
            frame,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=background,
            fg="white",
            width=12
        ).pack(
            side="right",
            padx=10,
            pady=5
        )

    # =========================================================
    # RELATION MATRIX
    # =========================================================

    def show_matrix(self):

        students = self.db.get_students()

        if not students:

            messagebox.showwarning(
                "No Students",
                "Please add students first."
            )

            return

        student_labels = [
            f"{student[1]} ({student[2]})"
            for student in students
        ]

        relations = self.get_relation_pairs()

        relation_set = {
            (relation[1], relation[2])
            for relation in relations
        }

        window = tk.Toplevel(self.root)

        window.title("Relation Matrix")
        window.geometry("850x650")

        tk.Label(
            window,
            text="Relation Matrix",
            font=("Segoe UI", 21, "bold")
        ).pack(pady=(20, 5))

        tk.Label(
            window,
            text="1 = Relation exists     0 = Relation does not exist",
            font=("Segoe UI", 10),
            fg="#6b7280"
        ).pack(pady=(0, 20))

        frame = tk.Frame(window)

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columns = ["student"] + [
            f"c{i}"
            for i in range(len(student_labels))
        ]

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        tree.heading(
            "student",
            text="From \\ To"
        )

        tree.column(
            "student",
            width=180,
            anchor="center"
        )

        for i, student in enumerate(student_labels):

            column_name = f"c{i}"

            tree.heading(
                column_name,
                text=student
            )

            tree.column(
                column_name,
                width=100,
                anchor="center"
            )

        for student_a in student_labels:

            row = [student_a]

            for student_b in student_labels:

                if (student_a, student_b) in relation_set:

                    row.append("1")

                else:

                    row.append("0")

            tree.insert(
                "",
                "end",
                values=row
            )

        tree.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            window,
            text="Rows represent source students and columns represent destination students.",
            font=("Segoe UI", 9),
            fg="#6b7280"
        ).pack(pady=15)

    # =========================================================
    # UPDATE COUNTS
    # =========================================================

    def update_counts(self):

        students = self.db.get_students()
        relations = self.db.get_relations()

        self.student_count.set(
            str(len(students))
        )

        self.relation_count.set(
            str(len(relations))
        )


# =============================================================
# PROGRAM START
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = StudentRelationshipAnalyzer(root)

    root.mainloop()