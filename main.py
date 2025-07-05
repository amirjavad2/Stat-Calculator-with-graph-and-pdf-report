import random as r
import pandas as p
import numpy  as n
import matplotlib.pyplot as mat
import math as m
from fpdf import FPDF
import os
import re
class Statistic_calculator : 
    def __init__(self, data=None):
        if data == None :
            self.data = self.inp()
        else :
            self.data = data
        self.data = self.sort_count(self.data)
        self.df =self.frequency_table(self.data)
        self.stats = self.Statistics(self.data)
        self.graphs(self.data)
        self.export(self.data, self.stats)
    def inp(self):        
        i = 0
        data = []
        while i < 80 :
            data.append(round(r.uniform(30.00,55.00),2))
            i += 1
        print(data)
        return data
    def sort_count(self, data):
        data = sorted(data)
        dpcounter = len(data)
        data.insert(0,dpcounter)
        print(data)
        return data
    def frequency_table(self, data):
        log = n.log10(data[0])
        k = m.ceil(1 + 3.322  * log )
        l = len(data)
        r = data[l-1] - data[1]
        width = r / k
        i = 1
        lowerinterval = [data[1] - 0.5]
        higherinterval = [data[1] - 0.5 + width - 0.001]
        xi = [0]
        fi = [0]
        pi = [0]
        si = [0]
        while i < (k) : 
            lcounter = lowerinterval[0] + i * width
            hcounter = higherinterval[0] + i * width
            lowerinterval.append(lcounter)
            higherinterval.append(hcounter)
            xi.append(0)
            fi.append(0)
            pi.append(0)
            si.append(0)
            i += 1
        i = 0 
        while i < k:
            higherinterval[i] = round(higherinterval[i], 2)
            lowerinterval[i] = round(lowerinterval[i], 2)
            i += 1
        higherinterval[k - 1] = float(m.ceil(higherinterval[k - 1]))
        i = 0
        while i < k   :#loop for inserting class intervals 
            xi[i] = round(((lowerinterval[i] + higherinterval[i]) / 2), 2)
            i += 1 
        i = 0   
        for x in data[1:] :#loop for inserting fi 
            if x > higherinterval[i]:
                if i == k - 1 :
                    break
                i += 1  
            if (i == k - 1 and x <= higherinterval[i]) or (lowerinterval[i] < x <= higherinterval[i]):
               fi[i] += 1
        i = 0 
        for x in fi : # loop for inserting pi 
            pi[i] = round((x / data[0]), 2)
            i += 1  
        i = 1
        si[0] = fi[0] 
        while i < len(fi) : # loop for inserting si 
            si[i] = si[i - 1] + fi[i]
            i += 1 
        ftdata = {#frequency table data 
            'lowerinterval' : lowerinterval ,
            'higherinterval' :  higherinterval ,
            'xi' : xi ,
            'fi' : fi , 
            'pi' : pi ,
            'si' : si , 
        }
        df = p.DataFrame(ftdata)
        df.to_csv(os.path.expanduser(r"C:\Users\iran\Documents\dataframe.csv"), index = False)        
        print(df)
        return df
    def Statistics(self, data):
        Variance = round(n.var(data),2)
        std = round(n.std(data),2)
        median = round(n.median(data),2)
        mean = round(n.mean(data),2)
        print(f"Variance : {Variance}\nStandard Deviation : {std}\nMedian : {median}\nMean : {mean}")
        return [Variance, std, median, mean]
    def graphs(self, data):
        x = list(range(len(data[1:])))  # for indexing
        mat.plot(x, data[1:])
        mat.savefig("Line plot.png", bbox_inches='tight')
        mat.show()
        mat.bar(x, data[1:])
        mat.savefig("Bar Chart.png", bbox_inches='tight')
        mat.show()
        mat.scatter(x, data[1:])
        mat.savefig("Scatter plot.png", bbox_inches='tight')
        mat.show()
        mat.hist(data[1:], bins=10)
        mat.savefig("Historgram.png", bbox_inches='tight')
        mat.show()
        # Pie Chart – Only works if you slice and preprocess data
        pie_data = data[1:6]  # top 5 elements
        labels = [f"Group {i+1}" for i in range(len(pie_data))]
        mat.figure(figsize=(6, 6))
        mat.pie(pie_data, labels=labels, autopct='%1.1f%%')
        mat.title("Pie Chart")
        mat.savefig("Pie chart.png", bbox_inches='tight')
        mat.show()
    def export(self, df, stats):
        export_path = os.path.expanduser(r"C:\Users\iran\Documents")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Sorted Data", ln=True)
        sorted_data = ", ".join([str(i) for i in self.data[1:]])
        chunk_size = 120
        for i in range(0, len(sorted_data), chunk_size):
            pdf.multi_cell(0, 10, sorted_data[i:i+chunk_size])
        pdf.set_font("Courier", size=9)
        pdf.cell(200, 10, txt="Frequency Distribution Table", ln=True)
        pdf.multi_cell(0, 8,"    Loweri            Higheri             xi                fi                pi               si")
        #table_text = self.df.to_string(index=False)
        for _, row in self.df.iterrows():
            row_text = " | ".join([f"{str(val):^15}" for val in row])
            pdf.cell(0, 8, txt=row_text, ln=True, align = "L")
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Statistics", ln=True)
        pdf.multi_cell(0, 10, f"Mean: {stats[3]}    Median: {stats[2]}    Std Dev: {stats[1]}    Variance: {stats[0]}")
        #pdf.add_page()
        pdf.image(r"C:\Users\iran\Documents\Line plot.png", x=55, y=None, w=100)
        pdf.add_page()
        pdf.image(r"C:\Users\iran\Documents\Bar Chart.png", x=55, y=None, w=100)
        #pdf.image(r"C:\Users\iran\Documents\Scatter plot.png", x=55, y=None, w=100)
        #pdf.add_page()
        pdf.image(r"C:\Users\iran\Documents\Historgram.png", x=55, y=None, w=100)
        #pdf.add_page()
        pdf.image(r"C:\Users\iran\Documents\Pie chart.png", x=55, y=None, w=100)
        pdf.output(f"{export_path}\Stat report.pdf")
with open(r"C:\Users\iran\Documents\data.txt") as d :
    data = d.read()
data = re.split("\s" , data)
#print(data)
l = len(data) - 1 
numdata = []
for x in data :
    y = float(x)
    numdata.append(y)
print(numdata)
rndata = Statistic_calculator(numdata)

