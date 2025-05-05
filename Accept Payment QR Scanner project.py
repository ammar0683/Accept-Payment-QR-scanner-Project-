import qrcode

# Taking UPI ID As a input
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CUREENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QR Code to image file
phonepe_qr.save("phonepe.png", scale=8)
paytm_qr.save("paytm.png", scale=8)
google_pay_qr.save("google_pay.png", scale=8)

#Display the QR Codes (you need to install PIL/PILLOW Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

