from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import os
import qrcode
os.system("title ID CARD Generator by Ojas")

title =(" \t\t\t\t\t\t ID CARD Generator\t\t\t\t\t")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (title)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your School Name: ')
company=message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (550, 175)
idno=input('Enter Admission Number: ')
message = str('Adm.no. '+str(idno))
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name=message
color = 'rgb(0, 0, 0)' 
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (250, 350)
message = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

(x, y) = (50, 750)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)




'''code is to save the data as a image
    this code save the qr code first then insert the qrcode into the final image(ID card)
'''
image.save(str(name)+'.png')



img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
img.save(str(idno)+'.bmp')


til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp')
til.paste(im,(600,350))
til.save(name+'.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))
eval(input('\n\nPress any key to Close program...'))
