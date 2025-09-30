row1=['😘','😘','😘']
row2=['😘','😘','😘']
row3=['😘','😘','😘']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter your choice position to hide money:")
#32
row_number=int(position[0])
column_number=int(position[1])
row_selection=matrix[row_number-1]
row_selection[column_number-1]='💲'
print(f"{row1}\n{row2}\n{row3}")
