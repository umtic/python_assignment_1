#BBM-103 Assignment 2
#Umut Bayindir 2210356147
import os
current_dir_path = os.getcwd()
commands=[]
patientinfo=[]
output=[]
def fread():
    reading_file_name = "doctors_aid_inputs.txt"
    reading_file_path = os.path.join(current_dir_path, reading_file_name)
    with open(reading_file_path, "r") as i:
            count = 0
            while True:
                count += 1
                line = i.readline()
                if not line:
                    break
                commands.append(line)
            i.close()
def fwrite():
    writing_file_name = "doctors_aid_outputs.txt"
    writing_file_path = os.path.join(current_dir_path, writing_file_name)
    with open(writing_file_path,"w") as o:
        stroutput=""
        for x in output:
            stroutput += x
        o.write(stroutput)
        o.close()
def create():
    name=data[0]
    patientname=""
    if len(patientinfo)==0:
        patientinfo.append(data.copy())
        output.append("Patient {} is recorded.\n".format(name))
    else:
        for i in range(len(patientinfo)):
            patientname=patientinfo[i][0]
            if name in patientname:
                isFound=True
                break
            else:
                isFound=False
                continue
        if isFound is True:
            output.append("Patient {} cannot be recorded due to duplication.\n".format(name))
        else:
                patientinfo.append(data.copy())
                output.append("Patient {} is recorded.\n".format(name))
def remove():
    name=data[0]
    patientname=""
    if len(patientinfo)==0:
        output.append("Patient {} cannot be removed due to absence.\n".format(name))
    else:
        for i in range(len(patientinfo)):
            patientname=patientinfo[i][0]
            if name in patientname:
                isFound=True
                break
            else:
                isFound=False
                continue
        if isFound is True:
                patientinfo.pop(i)
                output.append("Patient {} is removed.\n".format(name))
        else:
                output.append("Patient {} cannot be removed due to absence.\n".format(name))
def flist():
    output.append("Patient Diagnosis\tDisease \t\tDisease \tTreatment\t\tTreatment\n")
    output.append("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n")
    output.append("-------------------------------------------------------------------------\n")
    for i in range(len(patientinfo)):
        patientname=patientinfo[i][0]
        accuracy=patientinfo[i][1]
        acc=float(accuracy)
        oacc=acc*100
        cancer=patientinfo[i][2]
        incidence=patientinfo[i][4]
        treatment=patientinfo[i][5]
        if treatment=="Targeted":
            risk=patientinfo[i][7]
            treatment="Targeted Therapy"
            frisk=float(risk)
            ofrisk=frisk*100
            output.append("{}\t{}%\t\t{} Cancer\t\t{}\t{}\t{}%\n".format(patientname,oacc,cancer,incidence,treatment,ofrisk))
        else:
            risk=patientinfo[i][6]
            frisk=float(risk)
            ofrisk=frisk*100
            output.append("{}\t{}%\t\t{} Cancer\t\t{}\t{} \t\t{}%\n".format(patientname,oacc,cancer,incidence,treatment,ofrisk))
def probability():
    name=data[0]
    patientname=""
    incidence=""
    cancer=""
    if len(patientinfo)==0:
        output.append("Probability for {} cannot be calculated due to absence.\n".format(name))
    else:
        for i in range(len(patientinfo)):
            patientname=patientinfo[i][0]
            if name in patientname:
                isFound=True
                break
            else:
                isFound=False
                continue
        if isFound is True:
            accuracy=patientinfo[i][1]
            acc=float(accuracy)
            cancer=patientinfo[i][2]
            cancerl=cancer.lower()
            incidence=patientinfo[i][4]
            inci=incidence.split("/")[0]
            inci1=int(inci)
            probab=(inci1/((1-acc)*100000+inci1))*100
            oprobab=round(probab,2)
            output.append("Patient {} has a probability of {}% of having {} cancer.\n".format(name,oprobab,cancerl))
        else:
            output.append("Probability for {} cannot be calculated due to absence.\n".format(name))
def recommendation():
    name=data[0]
    patientname=""
    if len(patientinfo)==0:
        output.append("Recommendation for {} cannot be calculated due to absence.\n".format(name))
    else:
        for i in range(len(patientinfo)):
            patientname=patientinfo[i][0]
            if name in patientname:
                isFound=True
                break
            else:
                isFound=False
                continue
        if isFound is True:
                accuracy=patientinfo[i][1]
                acc=float(accuracy)
                incidence=patientinfo[i][4]
                risk=patientinfo[i][6]
                r=float(risk)
                inci=incidence.split("/")[0]
                inci1=int(inci)
                probab=inci1/((1-acc)*100000+inci1)
                if r>=probab:
                    output.append("System suggests {} NOT to have the treatment.\n".format(name)) 
                else:
                    output.append("System suggests {} to have the treatment.\n".format(name))
        else:
            output.append("Recommendation for {} cannot be calculated due to absence.\n".format(name))
fread()
for i in range(len(commands)):
    strstep1=""
    strstep2=""
    strstep3=""
    step1=commands[i]
    for x in step1:
        strstep1+=x
    step2=strstep1.splitlines()
    for x in step2:
        strstep2+=x
    step3=strstep2.split(",")
    for x in step3:
        strstep3+=x
    data=strstep3.split(" ")
    funct=data[0]
    if funct == "create":
        funct=""
        data.pop(0)
        create()
    if funct == "remove":
        funct=""
        data.pop(0)
        remove()
    if funct == "list": 
        funct=""
        data.pop(0)    
        flist()
    if funct == "probability":  
        funct="" 
        data.pop(0)       
        probability()
    if funct == "recommendation":
        data.pop(0)
        funct=""
        recommendation()
    data.clear()
fwrite()