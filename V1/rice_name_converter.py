def namecheck(name):
      if 'LOC_Os' in name :
            return 0
      elif 'g' in name :
            return 1
      else :
            return 2

import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)



# open data and store as list 
# RM => RAP_MSU list
with open('RAP_MSU.txt','r') as file:
      RM = file.readlines()
for i in range(len(RM)):
      RM[i] = RM[i].strip()
      RM[i] = RM[i].split('\t')
      RM[i][1] = RM[i][1].split('.')
      RM[i][1] = RM[i][1][0]
# Rn => RAP_name list
with open('RAP_name.txt','r') as file:
      Rn = file.readlines()
for i in range(len(Rn)):
      Rn[i] = Rn[i].strip()
      Rn[i] = Rn[i].split('\t')
# RT => RAP_Transcript list
with open('RAP_Transcript.txt','r') as file:
      RT = file.readlines()
for i in range(len(RT)):
      RT[i] = RT[i].strip()
      RT[i] = RT[i].split('\t')



print('===============================')
print('Rice name converter V1')
print('1. You can input MSU id, RAP id and Accession number')
print('2. The program will convert your input.')

while True:
      print('===============================')
      name = input('Please input gene: ')
      check = namecheck(name)
      if check == 0: #LOC_(MSU)
            resRAP = []
            resMSU = []
            resTrans = []
            resName = []
            for i in range(len(RM)):
                  if RM[i][1] == name:
                        resRAP.append(RM[i][0])
            resMSU.append(name)
            name = resRAP[0]
            for i in range(len(RT)):
                  if RT[i][0] == name:
                        resTrans.append(RT[i][1])
            for i in range(len(Rn)):
                  if Rn[i][0] == name:
                        resName.append(Rn[i][1])
            addToClipBoard(','.join(resRAP))
            
      if check == 1 : #RAP
            resRAP = []
            resMSU = []
            resTrans = []
            resName = []
            resRAP.append(name)
            for i in range(len(RM)):
                  if RM[i][0] == name:
                        resMSU.append(RM[i][1])
            for i in range(len(RT)):
                  if RT[i][0] == name:
                        resTrans.append(RT[i][1])
            for i in range(len(Rn)):
                  if Rn[i][0] == name:
                        resName.append(Rn[i][1])
            addToClipBoard(','.join(resMSU))

      if check == 2 : #AK
            resRAP = []
            resMSU = []
            resTrans = []
            resName = []
            resTrans.append(name)
            for i in range(len(RT)):
                  if RT[i][1] == name:
                        name = RT[i][0]
                        resRAP.append(RT[i][0])
            for i in range(len(RM)):
                  if RM[i][0] == name:
                        resMSU.append(RM[i][1])
            for i in range(len(Rn)):
                  if Rn[i][0] == name:
                        resName.append(Rn[i][1])


      RAP = ','.join(resRAP)
      MSU = ','.join(resMSU)
      Trans = ','.join(resTrans)
      Name = ','.join(resName)
      print('============result==============')
      print('RAP_id: '+RAP)
      print('MSU_id: '+MSU)
      print('Accession number:'+Trans)
      print('Gene_name: '+Name)
      End = input('===============================\n')
