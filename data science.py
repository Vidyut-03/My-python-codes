import matplotlib.pyplot as plt

students_names=["Arnav","Neel","Rohin","Avaneesh","Aaveg","Adam","Shreyas","Tuhin"]

students_marks=[45,100,87,75,98,56,89,99]

marks_perc = []
for x in students_marks:
  res = (x/50)*100
  marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
  plt.plot(students_names,students_marks)
  plt.title("Students Marks Graph")
  plt.xlabel("Students Names")
  plt.ylabel("Students Marks")
  plt.show()

marks_line_chart()

def percentage_bar_chart():
  plt.bar(students_names,marks_perc)
  plt.title("Students Percentage Graph")
  plt.xlabel("Students Names")
  plt.ylabel("Students Percentage")
  plt.show()

percentage_bar_chart()
