#to add: open csv and convert format of decimal. Import into df 


for i in range(len(df)):
    area = ((df.xmax.iloc[i]-df.xmin.iloc[i])/2)*((df.ymax.iloc[i]-df.ymin.iloc[i])/2) 
    if df.class_.iloc[i] == 1:
        df.est_pop.iloc[i] = area * 0.065
    elif df.class_.iloc[i] == 2:
        df.est_pop.iloc[i] = area * 0.010
        
 final_df = pd.DataFrame(columns=['Image','NumObj_Class1','NumObj_Class2','EstimatedPopulation'])
 
 classes = ["1","2"]
final = []
for elem in set(imgs):
    tmpdf = df.loc[df['Image']==elem]
    #print(tmpdf)
    unodf = df.loc[df['class_']==1]
    #print(len(unodf))
    n_uno = len(unodf)
    duedf = df.loc[df['class_']==2]
    n_due = len(duedf)
    #print(elem, n_uno, n_due)
    l = [elem, n_uno, n_due]
    pop = df.groupby('Image').sum()
    print(pop)
    est = pop.loc[pop['Image']==elem]
    print(est)
    final.append(l)
    
  #to add: convert list of lists in csv and save it 
  #run on Output_2.csv 
