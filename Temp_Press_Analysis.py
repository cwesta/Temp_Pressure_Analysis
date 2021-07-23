from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo
import pandas as pd 


root = Tk()
root.geometry("300x200")

label_1 = Label(root, text="Select the CSV File to run analysis", font="50")
label_1.pack()

def myClick():
	filename = askopenfilename()
	showinfo("SaveAs","Next Select the desired filepath for the outputed CSV File",parent=root)
	filepath = asksaveasfilename()
	return csvDataAnalysis(filename, filepath)

def csvDataAnalysis(filename, filepath):

	df = pd.read_csv(filename)
	df.dropna()

	df.reset_index(drop=True, inplace=True)

	time_stamp = []
	date_stamp = []

	avg_m_temp = []

	avg_temp_A = []
	avg_temp_B = []
	avg_temp_C = []

	pressure_delta_A =[]
	pressure_delta_B =[]
	pressure_delta_C =[]


	avg_temp_tank_A = []
	avg_temp_tank_B = []
	avg_temp_tank_C = []

	for i in range(1, len(df)):
	  
	    try:
	        
	        #check for the start of a condition changes from 0 to -1
	        if df['Condition'][i-1] == 0 and df['Condition'][i] == -1:
	            
	            date_stamp.append(df['Date'][i])
	            time_stamp.append(df['Time'][i])

	            mixer_temp = []
	            
	            temp_A = []
	            temp_B = []
	            temp_C = []
	            
	            idle_A = df['Press_A'][i-1]
	            idle_B = df['Press_B'][i-1]
	            idle_C = df['Press_C'][i-1]

	            dispense_A_arr=[]
	            dispense_B_arr=[]
	            dispense_C_arr=[]

	            avg_A = []
	            avg_B = []
	            avg_C = []
	            
	            temp_tank_A = []
	            temp_tank_B = []
	            temp_tank_C = []
	            
	            
	            
	            mixer_temp.append(df['M_Tp'][i])

	            temp_A.append(df['A_Tp'][i])
	            
	            temp_B.append(df['B_Tp'][i])
	            
	            temp_C.append(df['C_Tp'][i])
	            
	            
	            dispense_A_arr.append(df['A_Press'][i])
	            dispense_B_arr.append(df['B_Press'][i])
	            dispense_C_arr.append(df['C_Press'][i])
	            
	            temp_tank_A.append(df['Tank_A_Tp'][i])
	            temp_tank_B.append(df['Tank_B_Tp'][i])
	            temp_tank_C.append(df['Tank_C_Tp'][i])
	            
	            continue
	            
	        #check that condition is continuing     
	        elif df['Condition'][i] == -1 and df['Condition'][i+1] == -1:
	            
	            
	            mixer_temp.append(df['M_Tp'][i])

	            temp_A.append(df['A_Tp'][i])
	            
	            temp_B.append(df['B_Tp'][i])
	            
	            temp_C.append(df['C_Tp'][i])
	            
	            
	            dispense_A_arr.append(df['A_Press'][i])
	            dispense_B_arr.append(df['B_Press'][i])
	            dispense_C_arr.append(df['C_Press'][i])
	            
	            temp_tank_A.append(df['Tank_A_Tp'][i])
	            temp_tank_B.append(df['Tank_B_Tp'][i])
	            temp_tank_C.append(df['Tank_C_Tp'][i])
	        
	            continue
	            
	        elif df['Condition'][i] == -1 and df['Condition'][i+1] == 0:
	            
	            mixer_temp.append(df['M_Tp'][i])
	            
	            temp_A.append(df['A_Tp'][i])
	            
	            temp_B.append(df['B_Tp'][i])
	            
	            temp_C.append(df['C_Tp'][i])
	            
	            
	            dispense_A_arr.append(df['A_Press'][i])
	            dispense_B_arr.append(df['B_Press'][i])
	            dispense_C_arr.append(df['C_Press'][i])
	            
	            temp_tank_A.append(df['Tank_A_Tp'][i])
	            temp_tank_B.append(df['Tank_B_Tp'][i])
	            temp_tank_C.append(df['Tank_C_Tp'][i])
	            
	            continue 
	            
	        #check if condition is finished either loop ends or condition changes from -1 to 0    
	        elif df['Condition'][i] == 0 and df['Condition'][i-1] == -1:
	            #1
	            avg_mixer_temp.append((sum(mixer_temp)/len(mixer_temp)))
	            
	            avg_temp_A.append((sum(temp_A)/len(temp_A)))
	            
	            avg_temp_B.append((sum(temp_B)/len(temp_B)))
	            avg_temp_C.append((sum(temp_C)/len(temp_C)))
	            
	            avg_A = sum(dispense_A_arr)/len(dispense_A_arr)
	            avg_B = sum(dispense_B_arr)/len(dispense_B_arr)
	            avg_C = sum(dispense_C_arr)/len(dispense_C_arr)

	            delta_press_A = idle_A - avg_A
	            delta_press_B = idle_B - avg_B
	            delta_press_C = idle_C - avg_C
	            
	            pressure_delta_A.append(delta_press_A)
	            pressure_delta_B.append(delta_press_B)
	            pressure_delta_C.append(delta_press_C)
	        
	            avg_temp_tank_A.append((sum(temp_tank_A)/len(temp_tank_A)))
	            avg_temp_tank_B.append((sum(temp_tank_B)/len(temp_tank_B)))
	            avg_temp_tank_C.append((sum(temp_tank_C)/len(temp_tank_C)))
	        
	            continue
	            
	    except:
	        
	        avg_mixer_temp.append((sum(mixer_temp)/len(mixer_temp)))
	        
	        avg_temp_A.append((sum(temp_A)/len(temp_A)))
	        
	        avg_temp_B.append((sum(temp_B)/len(temp_B)))
	        avg_temp_C.append((sum(temp_C)/len(temp_C)))
	        
	        
	        avg_A = sum(dispense_A_arr)/len(dispense_A_arr)
	        avg_B = sum(dispense_B_arr)/len(dispense_B_arr)
	        avg_C = sum(dispense_C_arr)/len(dispense_C_arr)

	        delta_press_A = idle_A - avg_A
	        delta_press_B = idle_B - avg_B
	        delta_press_C = idle_C - avg_C
	        
	            
	        pressure_delta_A.append(delta_press_A)
	        pressure_delta_B.append(delta_press_B)
	        pressure_delta_C.append(delta_press_C)

	        
	        avg_temp_tank_A.append((sum(temp_tank_A)/len(temp_tank_A)))
	        avg_temp_tank_B.append((sum(temp_tank_B)/len(temp_tank_B)))
	        avg_temp_tank_C.append((sum(temp_tank_C)/len(temp_tank_C)))

	output_DF = pd.DataFrame(columns=['Date','TimeStamp','MixerTp', 'A_Tp', 'A_Press','Tank_A_Tp', 'B_Tp', 'B_Press','Tank_B_Tp', 'C_Tp', 'C_Press','Tank_C_Tp']).set_index("TimeStamp")

	output_DF['Date'] = pd.to_datetime(date_stamp)
	output_DF['TimeStamp'] = pd.to_datetime(time_stamp).time

	output_DF['MixerTp'] = avg_mixer_temp

	output_DF['A_Tp'] = avg_temp_A
	output_DF['A_Press'] = pressure_delta_A
	output_DF['Tank_A_Tp'] = avg_temp_tank_A


	output_DF['B_Tp'] = avg_temp_B
	output_DF['B_Press'] = pressure_delta_B
	output_DF['Tank_B_Tp'] = avg_temp_tank_B


	output_DF['C_Tp'] = avg_temp_C
	output_DF['C_Press'] = pressure_delta_C
	output_DF['Tank_C_Tp'] = avg_temp_tank_C


	output_DF.to_csv(filepath, index = False)














myButton = Button(root, text="Run Analysis!", command=myClick)
myButton.pack()



root.mainloop()