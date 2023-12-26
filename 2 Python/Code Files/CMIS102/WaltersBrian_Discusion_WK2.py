# Python code
# This program will perform mathematical computation with the three numbers, and displays the result.
# Developer: Brian Walters CMIS102/7384
# Date: March 22, 2023

print('Developer:\t Brian Walters')
print('Class:\t CMIS 102/7384\nDate:\t  3/23/2023')
print('Week 2 Discusion:\t Perform mathematical computation for Area in Square Feet for tile.')

def main():

#Initialize variable (tilesize = .5)
    tilesize = .5

#Prompt the user for (length)
    length = int(input('\nEnter length of area in feet.\t'))

#Prompt the user for the (width)
    width = int(input('\nEnter the width of the area in feet.\t'))

#Calculate the total (area)
    area = length * width

#Calculate total tiles needed (totTile)
    totTile = area // tilesize

#Display total tiles needed (totTile)
    print('\nTotal tiles needed is',(totTile))

# Execute -----------------------------
main()

    
