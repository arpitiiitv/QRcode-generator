#pip install pypng
#pip install pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
#S="Arpit_iiitv"
S=input("Enter name(Shop,Org) to generate QRcode : ")
qrcode=pyqrcode.create(S)
qrcode.svg("myqr.svg",scale=8)
qrcode.png("myqrcode.png",scale=6)