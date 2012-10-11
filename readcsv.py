import csv
import os
from django.db import transaction
from apps.disease.models import Disease, Category



class LoadRatesForDisease():
    def read_csv_file(self, filename):
            """for reading csv file"""
            csvcontentlist = list()
            reader = csv.reader(open(filename, 'rb'), delimiter = ',')
            for row in reader:
                csvcontentlist.append(row)
            return csvcontentlist
        
    def loadsubcategory(self):
        filename =  "/home/madhupavi/Downloads/subcategory1.csv"
        if os.path.exists(filename):
            categories = self.read_csv_file(filename)
            print categories
            
                
            for index in range(len(categories)):
            #    print categories[index][0], categories[index][1], categories[index][2], categories[index][3]
                
            
                
                with transaction.commit_on_success():
                    objCategory = Category()
                    if not (categories[index][0] == None and categories[index][4] == None):
#                            Category.objects.create(diseasename = Disease.objects.get(diseasename__iexact=item[4]),
#                                                    subcategory = item[0], 
#                                                    rate_for_NABH = float(item[1]), 
#                                                    rate_for_non_NABH = float(item[2]), 
#                                                    rate_for_superspecial = float(item[3]))
                        
                        if categories[index][1] == '':
                            categories[index][1] = '0'
                        
                        if categories[index][2] == '':
                            categories[index][2] = '0'
                        
                        if categories[index][3] == '':
                            categories[index][3] = '0'
                            
                        objCategory.subcategory =  unicode(categories[index][0])
                        objCategory.rate_for_NABH = float(categories[index][1])
                        objCategory.rate_for_non_NABH =  float(categories[index][2])
                        objCategory.rate_for_superspecial =  float(categories[index][3])
                        objCategory.diseasename = Disease.objects.get(diseasename__iexact=unicode(categories[index][4]))   
                        #objCategory.diseasename = categories[index][4] 
                        objCategory.save()
#            
        else:
            print "file doesn't exist"
            
    def loadcategory(self):
        filename =  "/home/madhupavi/Downloads/category1.csv"
        
        if os.path.exists(filename):
            diseases = self.read_csv_file(filename)
#            print diseases
            if diseases:
                objDisease = Disease()
                for diseasename in diseases:
                    with transaction.commit_on_success():
                        objDisease.diseasename = diseasename[0]
                        objDisease.save() 
        else:
            print "file doesn't exist"

objLoadRatesForDisease = LoadRatesForDisease()
print "cateory"
objLoadRatesForDisease.loadcategory()
print "subcategory"
objLoadRatesForDisease.loadsubcategory()
#
