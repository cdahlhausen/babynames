
# coding: utf-8
#I recently created a programming exercise and I think you might appreciate working through it. 
#I have created my own solution, so we can compare.
#The United States Social Security Administration has made available data on the 
# frequency of baby names from 1880 through the present. 
# Download names.zip from ssa.gov (linked below) and unpack into your 
# working directory. 
# Create a Python callable which accepts 
# - the year, 
# - a number n
# - optionally whether to include only male or female names; 
# this callable should 
# - return a list of the top n names in that year 
# - (filtered down to only male or female, if requested by the optional argument). 
# You are welcome to add additional functionality to your program, and use of library modules is permitted.
#
#http://www.ssa.gov/oact/babynames/limits.html


import csv
import argparse


def print_results(results, n=10):
    iterator = 0
    print "{:<8} {:<15} {:<10}".format('#','Name','Births')        
    print "{:<8} {:<15} {:<10}".format('-','----','------')        
    for v in results[:n]:
        iterator += 1
        print "{:<8} {:<15} {:<10}".format( iterator, v['Name'], v['Births'])

def find_names(year, n, sex=None):
    with open('yob' + str(year) + '.txt', 'rb') as f:        
        reader =  csv.DictReader(f, fieldnames = ['Name', 'Gender', 'Births'])
        results = []
        males = []
        females = []

        # Read the complete csv into a dict
        for row in reader:
            results.append(row)
        
        # Iterate through dict and sort by gender
        for v in results:
            if v['Gender'] == 'F':
                females.append(v)
            if v['Gender'] == 'M':
                males.append(v)
                
        if sex == 'F':
            print "Female names:"
            print_results(females,n)
        if sex == 'M':
            print "Male names:"
            print_results(males,n)
        if sex == None:
            print "Male names:"
            print_results(males, n)
            print "\n"
            print "Female names:"
            print_results(females, n)

parser = argparse.ArgumentParser(description='Returns frequency of baby names.')
parser.add_argument('year', metavar='year', type=int, action='store',
                   help='year')
parser.add_argument('num', metavar='Number', action='store', default=10,
                   nargs='?', type=int, help='Number of results')
parser.add_argument('gender', metavar='Gender', action='store', default=None,
                   nargs='?', help='Results by gender')
args = parser.parse_args()
find_names(args.year,args.num,args.gender)
