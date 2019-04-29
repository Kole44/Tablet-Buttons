#!/usr/bin/env python3

#Created for the purpose of controlling stage elements in the Ai-Pollo play
#Author: Kole Seeber
#Date Created: Nov/14/2018

import sys
import tkinter
from socket import socket,AF_INET,SOCK_DGRAM

SERVER_IP = '192.168.1.3'
PORT_NUMBER = 5005
SIZE = 1024

mySocket = socket(AF_INET,SOCK_DGRAM) #open port and never close it

#mainloop
from tkinter import ttk
top=tkinter.Tk() #create top-level (or root) window
top.title("Stage Control")
top.geometry("800x480") #size of window
#top.resizable(0,0) #prevents from resizing window
top.config(cursor='none')
top.attributes('-fullscreen',True)
#messages to send through Ethernet port
mOpenGate="OGD"
mCloseGate="CGD"
mOpenShrine="OSD"
mCloseShrine="CSD"
mOpenGatePlat="OGP"
mCloseGatePlat="CGP"
mOpenShrinePlat="OSP"
mCloseShrinePlat="CSP"
mOpenEyes="OBE"
mCloseEyes="CBE"
mTurnOnLED="OBL"
mTurnOffLED="CBL"
mESTOP="STOP"
mReset="Reset"
#mOpengatedoorandplatform="OGDOGP"
#mClosegatedoorandplatform="CGDCGP"
#mOpenshrinedoorandplatform="OSDOSP"
#mCloseshrinedoorandplatform="CSDCSP"
#mOpenbabyeyesandturnonled="OBEOBL"
#mClosebabyeyesandturnonled="CBECBL"
    
#Callbacks for TAB 1: when button is pressed, send corresponding character & change button color
def callbackOpenGateDoor():
    #change color of buttons 
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenGate.encode('utf-8'),(SERVER_IP,PORT_NUMBER))#send character through port
    #change color of open button to green
    #print("Open gate button pressed")
    openGateDoorButton.configure(style='st.TButton')
    
def callbackCloseGateDoor():
    #change color of open gate door button back to blue4
    openGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseGate.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeGateDoorButton.configure(style='st.TButton')
    
def callbackOpenShrineDoor():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')    
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenShrine.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openShrineDoorButton.configure(style='st.TButton')
    
def callbackCloseShrineDoor():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton') 
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseShrine.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeShrineDoorButton.configure(style='st.TButton')
    
def callbackOpenGatePlatform():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')    
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenGatePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openGatePlatformButton.configure(style='st.TButton')
    
def callbackCloseGatePlatform():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseGatePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeGatePlatformButton.configure(style='st.TButton')
    
def callbackOpenShrinePlatform():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenShrinePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openShrinePlatformButton.configure(style='st.TButton')
    
def callbackCloseShrinePlatform():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseShrinePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeShrinePlatformButton.configure(style='st.TButton')
    
def callbackOpenEyes():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenEyes.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openEyesButton.configure(style='st.TButton')
    
def callbackCloseEyes():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseEyes.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeEyesButton.configure(style='st.TButton')
    
def callbackTurnOnLED():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mTurnOnLED.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    turnOnEyesButton.configure(style='st.TButton')
    
def callbackTurnOffLED():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mTurnOffLED.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    turnOffEyesButton.configure(style='st.TButton')

def callbackESTOP():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mESTOP.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    estop.configure(style='st.TButton')
    estop2.configure(style='st.TButton')

def callbackReset():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    mySocket.sendto(mReset.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    reset.configure(style='st.TButton')
    reset2.configure(style='st.TButton')

def callbackOpenGDGP():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenGate.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    mySocket.sendto(mOpenGatePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openGDGPButton.configure(style='st.TButton')

def callbackCloseGDGP():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseGatePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    mySocket.sendto(mCloseGate.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeGDGPButton.configure(style='st.TButton')

#def callbackOpenSDSP():
#    openGateDoorButton.configure(style='s.TButton')
#    closeGateDoorButton.configure(style='s.TButton')
#    openShrineDoorButton.configure(style='s.TButton')
#    closeShrineDoorButton.configure(style='s.TButton')
#    openGatePlatformButton.configure(style='s.TButton')
#    closeGatePlatformButton.configure(style='s.TButton')
#    openShrinePlatformButton.configure(style='s.TButton')
#    closeShrinePlatformButton.configure(style='s.TButton')
#    openEyesButton.configure(style='s.TButton')
#    closeEyesButton.configure(style='s.TButton')
#    turnOnEyesButton.configure(style='s.TButton')
#    turnOffEyesButton.configure(style='s.TButton')
#    estop.configure(style='ste.TButton')
#    reset.configure(style='ste.TButton')
#    openGDGPButton.configure(style='s.TButton')
#    closeGDGPButton.configure(style='s.TButton')
#    closeSDSPButton.configure(style='s.TButton')
#    openBEBLButton.configure(style='s.TButton')
#    closeBEBLButton.configure(style='s.TButton')
#    estop2.configure(style='ste.TButton')
#    reset2.configure(style='ste.TButton')
#    mySocket.sendto(mOpenShrine.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
#    openSDSPButton.configure(style='st.TButton')
#    time.sleep(9)
#    mySocket.sendto(mOpenShrinePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        
#def callbackCloseSDSP():
#    openGateDoorButton.configure(style='s.TButton')
#    closeGateDoorButton.configure(style='s.TButton')
#    openShrineDoorButton.configure(style='s.TButton')
#    closeShrineDoorButton.configure(style='s.TButton')
#    openGatePlatformButton.configure(style='s.TButton')
#    closeGatePlatformButton.configure(style='s.TButton')
#    openShrinePlatformButton.configure(style='s.TButton')
#    closeShrinePlatformButton.configure(style='s.TButton')
#    openEyesButton.configure(style='s.TButton')
#    closeEyesButton.configure(style='s.TButton')
#    turnOnEyesButton.configure(style='s.TButton')
#    turnOffEyesButton.configure(style='s.TButton')
#    estop.configure(style='ste.TButton')
#    reset.configure(style='ste.TButton')
#    openGDGPButton.configure(style='s.TButton')
#    closeGDGPButton.configure(style='s.TButton')
#    openSDSPButton.configure(style='s.TButton')
#    openBEBLButton.configure(style='s.TButton')
#    closeBEBLButton.configure(style='s.TButton')
#    estop2.configure(style='ste.TButton')
#    reset2.configure(style='ste.TButton')
#    mySocket.sendto(mCloseShrinePlat.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
#    closeSDSPButton.configure(style='st.TButton')
#    time.sleep(9)
#    mySocket.sendto(mCloseShrine.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    
def callbackOpenBEBL():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    closeBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mOpenEyes.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    mySocket.sendto(mTurnOnLED.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    openBEBLButton.configure(style='st.TButton')
    
def callbackCloseBEBL():
    openGateDoorButton.configure(style='s.TButton')
    closeGateDoorButton.configure(style='s.TButton')
    openShrineDoorButton.configure(style='s.TButton')
    closeShrineDoorButton.configure(style='s.TButton')
    openGatePlatformButton.configure(style='s.TButton')
    closeGatePlatformButton.configure(style='s.TButton')
    openShrinePlatformButton.configure(style='s.TButton')
    closeShrinePlatformButton.configure(style='s.TButton')
    openEyesButton.configure(style='s.TButton')
    closeEyesButton.configure(style='s.TButton')
    turnOnEyesButton.configure(style='s.TButton')
    turnOffEyesButton.configure(style='s.TButton')
    estop.configure(style='ste.TButton')
    reset.configure(style='ste.TButton')
    openGDGPButton.configure(style='s.TButton')
    closeGDGPButton.configure(style='s.TButton')
    #openSDSPButton.configure(style='s.TButton')
    #closeSDSPButton.configure(style='s.TButton')
    openBEBLButton.configure(style='s.TButton')
    estop2.configure(style='ste.TButton')
    reset2.configure(style='ste.TButton')
    mySocket.sendto(mCloseEyes.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    mySocket.sendto(mTurnOffLED.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    closeBEBLButton.configure(style='st.TButton')


#***************************styles*******************************
tc=ttk.Style()
tc.configure('tc.TNotebook',background="white smoke")

t=ttk.Style()#style of tab frame'
t.configure('t.TFrame',background="white smoke")

f=ttk.Style() #use to configure style of frames buttons are in
f.configure('f.TLabelframe',font=('bold',70))

s=ttk.Style() #configure style of buttons before being pressed 
s.configure('s.TButton',state="normal",font=5,padding=6,background="blue4",foreground="white")
s.map('s.TButton',
      foreground=[('disabled','white'),
                  ('pressed','white'),
                  ('active','white')],
      background=[('disabled','blue4'),
                  ('pressed','blue4'),
                  ('active','blue4')])
st=ttk.Style()#configure style of buttons after being pressed
st.configure('st.TButton',state="normal",font=5,padding=6,background="green",foreground="white")
st.map('st.TButton',
      foreground=[('disabled','white'),
                  ('pressed','white'),
                  ('active','white')],
      background=[('disabled','green'),
                  ('pressed','green'),
                  ('active','green')])
ste=ttk.Style() #configure style of E-stop & Reset buttons before being pressed 
ste.configure('ste.TButton',state="normal",font=5,padding=6,background="red",foreground="white")
ste.map('ste.TButton',
      foreground=[('disabled','white'),
                  ('pressed','white'),
                  ('active','white')],
      background=[('disabled','red'),
                  ('pressed','red'),
                  ('active','red')])
#***************************************************************

#create two tabs
tabControl=ttk.Notebook(top,style='tc.TNotebook') #create tab control. Input argument in () is parent window
tab1=ttk.Frame(tabControl,style='t.TFrame') #first tab
tabControl.add(tab1,text='Single Function') #Add the tab
tabControl.pack(expand=1,fill="both") #Pack to make visible
tab2=ttk.Frame(tabControl,style='t.TFrame') #second tab
tabControl.add(tab2,text='Combined Functions')
tabControl.pack(expand=1,fill="both")
#end create two tabs

#creates equal padding between frames in tab 1 *************************
tab1.grid_columnconfigure(0,weight=1)
tab1.grid_columnconfigure(1,weight=5) 
tab1.grid_columnconfigure(2,weight=1)
tab1.grid_columnconfigure(3,weight=5)
tab1.grid_columnconfigure(4,weight=1)
tab1.grid_columnconfigure(5,weight=5)
tab1.grid_columnconfigure(6,weight=1)

tab1.grid_rowconfigure(0,weight=1)
tab1.grid_rowconfigure(1,weight=5)
tab1.grid_rowconfigure(2,weight=1)
tab1.grid_rowconfigure(3,weight=5)
tab1.grid_rowconfigure(4,weight=1)
tab1.grid_rowconfigure(5,weight=5)
tab1.grid_rowconfigure(6,weight=1)

#creates equal padding between frames in tab 2
tab2.grid_columnconfigure(0,weight=1)
tab2.grid_columnconfigure(1,weight=5) 
tab2.grid_columnconfigure(2,weight=1)
tab2.grid_columnconfigure(3,weight=5)
tab2.grid_columnconfigure(4,weight=1)
#tab2.grid_columnconfigure(5,weight=5)
#tab2.grid_columnconfigure(6,weight=1)

tab2.grid_rowconfigure(0,weight=1)
tab2.grid_rowconfigure(1,weight=5)
tab2.grid_rowconfigure(2,weight=1)
tab2.grid_rowconfigure(3,weight=5)
tab2.grid_rowconfigure(4,weight=1)

#create frames inside tab1 to hold two buttons each ******************************
frameGD=ttk.Labelframe(tab1,text='Gate Door',style="f.TLabelframe")
frameGD.grid(row=1,column=1,sticky='EWNS')
frameSD=ttk.Labelframe(tab1,text='Shrine Door')
frameSD.grid(row=1,column=3,sticky='EWNS')
frameGP=ttk.Labelframe(tab1,text='Gate Platform')
frameGP.grid(row=3,column=1,sticky='EWNS')
frameSP=ttk.Labelframe(tab1,text='Shrine Platform')
frameSP.grid(row=3,column=3,sticky='EWNS')
frameBE=ttk.Labelframe(tab1,text='Baby Eyes')
frameBE.grid(row=1,column=5,sticky='EWNS')
frameBL=ttk.Labelframe(tab1,text='Baby LEDs')
frameBL.grid(row=3,column=5,sticky='EWNS')
frameSTOP=ttk.Labelframe(tab1,text='E-STOP')
frameSTOP.grid(row=5,column=1,sticky='EWNS')
frameReset=ttk.Labelframe(tab1,text='Reset')
frameReset.grid(row=5,column=3,sticky='EWNS')

#create frames inside tab2 to hold two buttons each
frameGDGP=ttk.Labelframe(tab2,text='Gate Door & Platform',style="f.TLabelframe")
frameGDGP.grid(row=1,column=1,sticky='EWNS')
#frameSDSP=ttk.Labelframe(tab2,text='Shrine Door & Platform')
#frameSDSP.grid(row=1,column=3,sticky='EWNS')
frameBEBL=ttk.Labelframe(tab2,text='Baby Eyes & LEDs')
frameBEBL.grid(row=1,column=3,sticky='EWNS')
frameSTOP2=ttk.Labelframe(tab2,text='E-STOP')
frameSTOP2.grid(row=3,column=1,sticky='EWNS')
frameReset2=ttk.Labelframe(tab2,text='Reset')
frameReset2.grid(row=3,column=3,sticky='EWNS')

#Gridding for buttons in frames of tab 1 *********************************
#Gate door frame grid in tab 1
frameGD.grid_columnconfigure(0,weight=1)
frameGD.grid_columnconfigure(1,weight=1) 
frameGD.grid_columnconfigure(2,weight=1)
frameGD.grid_rowconfigure(0,weight=1)
frameGD.grid_rowconfigure(1,weight=1)
frameGD.grid_rowconfigure(2,weight=1)
frameGD.grid_rowconfigure(3,weight=1)
frameGD.grid_rowconfigure(4,weight=1)
frameGD.grid_rowconfigure(5,weight=1)

#Shrine door frame grid in tab 1
frameSD.grid_columnconfigure(0,weight=1)
frameSD.grid_columnconfigure(1,weight=1) 
frameSD.grid_columnconfigure(2,weight=1)
frameSD.grid_rowconfigure(0,weight=1)
frameSD.grid_rowconfigure(1,weight=1)
frameSD.grid_rowconfigure(2,weight=1)
frameSD.grid_rowconfigure(3,weight=1)
frameSD.grid_rowconfigure(4,weight=1)
frameSD.grid_rowconfigure(5,weight=1)

#Gate platform frame grid in tab 1
frameGP.grid_columnconfigure(0,weight=1)
frameGP.grid_columnconfigure(1,weight=1) 
frameGP.grid_columnconfigure(2,weight=1)
frameGP.grid_rowconfigure(0,weight=1)
frameGP.grid_rowconfigure(1,weight=1)
frameGP.grid_rowconfigure(2,weight=1)
frameGP.grid_rowconfigure(3,weight=1)
frameGP.grid_rowconfigure(4,weight=1)
frameGP.grid_rowconfigure(5,weight=1)

#Shrine platform frame grid in tab 1
frameSP.grid_columnconfigure(0,weight=1)
frameSP.grid_columnconfigure(1,weight=1) 
frameSP.grid_columnconfigure(2,weight=1)
frameSP.grid_rowconfigure(0,weight=1)
frameSP.grid_rowconfigure(1,weight=1)
frameSP.grid_rowconfigure(2,weight=1)
frameSP.grid_rowconfigure(3,weight=1)
frameSP.grid_rowconfigure(4,weight=1)
frameSP.grid_rowconfigure(5,weight=1)

#Baby Eyes (open/close) frame grid in tab 1
frameBE.grid_columnconfigure(0,weight=1)
frameBE.grid_columnconfigure(1,weight=1) 
frameBE.grid_columnconfigure(2,weight=1)
frameBE.grid_rowconfigure(0,weight=1)
frameBE.grid_rowconfigure(1,weight=1)
frameBE.grid_rowconfigure(2,weight=1)
frameBE.grid_rowconfigure(3,weight=1)
frameBE.grid_rowconfigure(4,weight=1)
frameBE.grid_rowconfigure(5,weight=1)

#Baby LEDs (on/off) frame grid in tab 1
frameBL.grid_columnconfigure(0,weight=1)
frameBL.grid_columnconfigure(1,weight=1) 
frameBL.grid_columnconfigure(2,weight=1)
frameBL.grid_rowconfigure(0,weight=1)
frameBL.grid_rowconfigure(1,weight=1)
frameBL.grid_rowconfigure(2,weight=1)
frameBL.grid_rowconfigure(3,weight=1)
frameBL.grid_rowconfigure(4,weight=1)
frameBL.grid_rowconfigure(5,weight=1)

#E-STOP frame grid in tab 1
frameSTOP.grid_columnconfigure(0,weight=1)
frameSTOP.grid_columnconfigure(1,weight=1) 
frameSTOP.grid_columnconfigure(2,weight=1)
frameSTOP.grid_rowconfigure(0,weight=1)
frameSTOP.grid_rowconfigure(1,weight=1)
frameSTOP.grid_rowconfigure(2,weight=1)

#Reset frame grid in tab 1
frameReset.grid_columnconfigure(0,weight=1)
frameReset.grid_columnconfigure(1,weight=1) 
frameReset.grid_columnconfigure(2,weight=1)
frameReset.grid_rowconfigure(0,weight=1)
frameReset.grid_rowconfigure(1,weight=1)
frameReset.grid_rowconfigure(2,weight=1)

#Gridding for buttons in frames of tab 2 **************************
#Gate door & gate platform frame grid in tab 2
frameGDGP.grid_columnconfigure(0,weight=1)
frameGDGP.grid_columnconfigure(1,weight=1) 
frameGDGP.grid_columnconfigure(2,weight=1)
frameGDGP.grid_rowconfigure(0,weight=1)
frameGDGP.grid_rowconfigure(1,weight=1)
frameGDGP.grid_rowconfigure(2,weight=1)
frameGDGP.grid_rowconfigure(3,weight=1)
frameGDGP.grid_rowconfigure(4,weight=1)
frameGDGP.grid_rowconfigure(5,weight=1)

#Shrine door & shrine platform frame grid in tab 2
#frameSDSP.grid_columnconfigure(0,weight=1)
#frameSDSP.grid_columnconfigure(1,weight=1) 
#frameSDSP.grid_columnconfigure(2,weight=1)
#frameSDSP.grid_rowconfigure(0,weight=1)
#frameSDSP.grid_rowconfigure(1,weight=1)
#frameSDSP.grid_rowconfigure(2,weight=1)
#frameSDSP.grid_rowconfigure(3,weight=1)
#frameSDSP.grid_rowconfigure(4,weight=1)
#frameSDSP.grid_rowconfigure(5,weight=1)

#Baby Eyes & LEDs frame grid in tab 2
frameBEBL.grid_columnconfigure(0,weight=1)
frameBEBL.grid_columnconfigure(1,weight=1) 
frameBEBL.grid_columnconfigure(2,weight=1)
frameBEBL.grid_rowconfigure(0,weight=1)
frameBEBL.grid_rowconfigure(1,weight=1)
frameBEBL.grid_rowconfigure(2,weight=1)
frameBEBL.grid_rowconfigure(3,weight=1)
frameBEBL.grid_rowconfigure(4,weight=1)
frameBEBL.grid_rowconfigure(5,weight=1)

#E-STOP frame grid in tab 2
frameSTOP2.grid_columnconfigure(0,weight=1)
frameSTOP2.grid_columnconfigure(1,weight=1) 
frameSTOP2.grid_columnconfigure(2,weight=1)
frameSTOP2.grid_rowconfigure(0,weight=1)
frameSTOP2.grid_rowconfigure(1,weight=1)
frameSTOP2.grid_rowconfigure(2,weight=1)

#Reset frame grid in tab 2
frameReset2.grid_columnconfigure(0,weight=1)
frameReset2.grid_columnconfigure(1,weight=1) 
frameReset2.grid_columnconfigure(2,weight=1)
frameReset2.grid_rowconfigure(0,weight=1)
frameReset2.grid_rowconfigure(1,weight=1)
frameReset2.grid_rowconfigure(2,weight=1)

#create buttons in frames of Tab 1 ******************************
openGateDoorButton=ttk.Button(frameGD,text="Open",style='s.TButton',command=callbackOpenGateDoor)
openGateDoorButton.grid(row=1,column=1,sticky='EWNS') 
closeGateDoorButton=ttk.Button(frameGD,text="Close",style='s.TButton',command=callbackCloseGateDoor)
closeGateDoorButton.grid(row=4,column=1,sticky='EWNS') 

openShrineDoorButton=ttk.Button(frameSD,text="Open",style='s.TButton',command=callbackOpenShrineDoor)
openShrineDoorButton.grid(row=1,column=1,sticky='EWNS')
closeShrineDoorButton=ttk.Button(frameSD,text="Close",style='s.TButton',command=callbackCloseShrineDoor)
closeShrineDoorButton.grid(row=4,column=1,sticky='EWNS')

openGatePlatformButton=ttk.Button(frameGP,text="Open",style='s.TButton',command=callbackOpenGatePlatform)
openGatePlatformButton.grid(row=1,column=1,sticky='EWNS')
closeGatePlatformButton=ttk.Button(frameGP,text="Close",style='s.TButton',command=callbackCloseGatePlatform)
closeGatePlatformButton.grid(row=4,column=1,sticky='EWNS')

openShrinePlatformButton=ttk.Button(frameSP,text="Open",style='s.TButton',command=callbackOpenShrinePlatform)
openShrinePlatformButton.grid(row=1,column=1,sticky='EWNS')
closeShrinePlatformButton=ttk.Button(frameSP,text="Close",style='s.TButton',command=callbackCloseShrinePlatform)
closeShrinePlatformButton.grid(row=4,column=1,sticky='EWNS')

openEyesButton=ttk.Button(frameBE,text="Open",style='s.TButton',command=callbackOpenEyes)
openEyesButton.grid(row=1,column=1,sticky='EWNS')
closeEyesButton=ttk.Button(frameBE,text="Close",style='s.TButton',command=callbackCloseEyes)
closeEyesButton.grid(row=4,column=1,sticky='EWNS')

turnOnEyesButton=ttk.Button(frameBL,text="On",style='s.TButton',command=callbackTurnOnLED)
turnOnEyesButton.grid(row=1,column=1,sticky='EWNS')
turnOffEyesButton=ttk.Button(frameBL,text="Off",style='s.TButton',command=callbackTurnOffLED)
turnOffEyesButton.grid(row=4,column=1,sticky='EWNS')

estop=ttk.Button(frameSTOP,text="STOP MOTORS",style='ste.TButton',command=callbackESTOP)
estop.grid(row=1,column=1,sticky='EWNS') 

reset=ttk.Button(frameReset,text="Reset MOTORS",style='ste.TButton',command=callbackReset)
reset.grid(row=1,column=1,sticky='EWNS')

#create buttons in frames of Tab 2 ******************************
openGDGPButton=ttk.Button(frameGDGP,text="Open",style='s.TButton',command=callbackOpenGDGP)
openGDGPButton.grid(row=1,column=1,sticky='EWNS') 
closeGDGPButton=ttk.Button(frameGDGP,text="Close",style='s.TButton',command=callbackCloseGDGP)
closeGDGPButton.grid(row=4,column=1,sticky='EWNS') 

#openSDSPButton=ttk.Button(frameSDSP,text="Open",style='s.TButton',command=callbackOpenSDSP)
#openSDSPButton.grid(row=1,column=1,sticky='EWNS') 
#closeSDSPButton=ttk.Button(frameSDSP,text="Close",style='s.TButton',command=callbackCloseSDSP)
#closeSDSPButton.grid(row=4,column=1,sticky='EWNS') 

openBEBLButton=ttk.Button(frameBEBL,text="Open",style='s.TButton',command=callbackOpenBEBL)
openBEBLButton.grid(row=1,column=1,sticky='EWNS') 
closeBEBLButton=ttk.Button(frameBEBL,text="Close",style='s.TButton',command=callbackCloseBEBL)
closeBEBLButton.grid(row=4,column=1,sticky='EWNS') 

estop2=ttk.Button(frameSTOP2,text="STOP MOTORS",style='ste.TButton',command=callbackESTOP)
estop2.grid(row=1,column=1,sticky='EWNS') 

reset2=ttk.Button(frameReset2,text="Reset MOTORS",style='ste.TButton',command=callbackReset)
reset2.grid(row=1,column=1,sticky='EWNS')


top.mainloop()
#end mainloop

sys.exit()
