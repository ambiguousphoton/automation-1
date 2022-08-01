import pywhatkit

hour = 21
mint = 51
wt = 1
message = "yo"
contact_list =['+919815464279','+918054207535', '+918054423980']

for i in contact_list:
    pywhatkit.sendwhatmsg(i, message , hour,mint)




print("narayan narayan narayan narayan")