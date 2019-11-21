#Working with missing values exercise (NumPy)

#create masked array with fill value -999

marr = MA.masked_array(range(10), fill_value=-999)

#mask the third value in the array

marr[2] = MA.masked

print(marr)

#print the mask associated with the array

print(marr.mask)

#make masked array "narr" which is "marr" but eveything >= 7 is masked

narr = MA.masked_where(marr > 6, marr)

#print an array that converts narr so that the missing values are represented by the filling values.

new_arr = MA.filled(narr)
print(new_arr)

