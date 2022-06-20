# formate --1 for making table's

from tabulate import tabulate
heading=[ "emp-id", "emp-name", "emp-dep", "emp-project" ]

date=[
    ["46073859", "Bharani ram kumar", "COX", "ACOE"],
    ["46090038", "JAYA LASKMI", "COX", "ACOE"],
    ["46090454", "A1", "COX", "ACOE"],
    ["45090566", "A2", "COX", "ACOE"]
]

print(tabulate(date, headers=heading, tablefmt="grid"))


# formate-2 for making table's

from prettytable import PrettyTable
table=PrettyTable(["Name", "Age", "Occupation", "City"])

table.add_row(["ram", "25", "software", "Guntur"])
table.add_row(["kumar", "25", "software", "Guntur"])
table.add_row(["bharani", "30", "Teacher", "Guntur"])
table.add_row(["ayesha", "25", "IT", "bangalore"])
table.add_row(["jaya", "25", "IT", ""])

print(table)
