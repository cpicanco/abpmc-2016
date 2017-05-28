#!/usr/bin/python

import sys

configDir = \
    "/home/ft/research/areas/number/difference_ratio/code/circle"

sys.path.append(configDir)

from config import setting

from random import shuffle
from math import pi, cos, sin, trunc
from time import time, sleep

from Tkinter import Tk, Canvas, Button
from PIL.ImageTk import PhotoImage

import tkFileDialog

class trial:
    index = 0

    photoList = None
    tokenCount = 0

    choice = None
    time = 0.00

# each trial has a code determining current circle type
possibleSetting = ["1", "2", "3", "4", "5", "6", "7"]

ratioSmall = "RS-"
ratioLarge = "RL-"
differenceSmall = "DS-"
differenceLarge = "DL-"

def blockCodeList():
    codeList = \
        [ratioSmall + digit for digit in possibleSetting] + \
        [ratioLarge + digit for digit in possibleSetting] + \
        [differenceSmall + digit for digit in possibleSetting] + \
        [differenceLarge + digit for digit in possibleSetting]
    shuffle(codeList)
    return codeList

def setWindow():
    choicePrompt = "VERDE OU VERMELHO?"
    window.title(choicePrompt)
    screenWidth, screenHeight = \
        window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(str(screenWidth) + "x" + str(screenHeight))

def startTrial():
    setPhotos()
    drawTokens()
    startChoicePeriod()

# there are four types of token images
stimDir = \
    "/home/ft/research/areas/number/difference_ratio/code/stims"

greenWinFile = stimDir + "/green_win.png"
greenLossFile = stimDir + "/green_loss.png"

redWinFile = stimDir + "/red_win.png"
redLossFile = stimDir + "/red_loss.png"

def setPhotos():
    trialCode = trialCodeList[trial.index]
    (nG, nR, wG, wR) = setting[trialCode]
    imageFileList = []
    imageFileList += [greenWinFile] * wG
    imageFileList += [greenLossFile] * (nG - wG)
    imageFileList += [redWinFile] * wR
    imageFileList += [redLossFile] * (nR - wR)
    shuffle(imageFileList)
    trial.photoList = \
        map(lambda imageFile: PhotoImage(file = imageFile), imageFileList)
    trial.tokenCount = len(trial.photoList)

def drawTokens():
    unitAngle = (2 * pi)/(trial.tokenCount)
    radiusInPixels = canvasHeight/3
    for tokenIndex in range(trial.tokenCount):
        tokenAngle = tokenIndex * unitAngle
        x = (canvasWidth/2) + trunc(cos(tokenAngle) * radiusInPixels)
        y = (canvasHeight/2) + trunc(sin(tokenAngle) * radiusInPixels)
        canvas.create_image(x, y, image = trial.photoList[tokenIndex],
            tags = "token")

def startChoicePeriod():
    trial.choice = None
    trial.time = time()
    window.bind("<KeyPress>", onKeyPress)

def upperOrLower(keyRange):
    return keyRange + keyRange.upper()

# possible key choices
keyRangeLeft = upperOrLower("sdfg")
keyRangeRight = upperOrLower("hjkl")

greenChoice, redChoice = "g", "r"

def onKeyPress(event):
    pressedKey = event.char
    keyIsChar = pressedKey != ""
    keyIsValid = pressedKey in keyRangeLeft + keyRangeRight
    if keyIsChar and keyIsValid:
        if pressedKey in keyRangeLeft:
            trial.choice = greenChoice
        elif pressedKey in keyRangeRight:
            trial.choice = redChoice
        trial.time = time() - trial.time
        endChoicePeriod()

def endChoicePeriod():
    window.unbind("<KeyPress>")
    addChoiceData()
    confirmChoice()

fieldSep = ","
lineEnd = "\n"

def addChoiceData():
    dataLine = trialCodeList[trial.index] + fieldSep + trial.choice + \
        fieldSep + "%.2f" %(trial.time) + lineEnd
    choiceDataList.append(dataLine)

choiceMessage = {"g": "VERDE", "r": "VERMELHO"}

def confirmChoice():
    canvas.create_text(canvasWidth/2, canvasHeight/2,
        text = choiceMessage[trial.choice], font = "Arial 20",
        anchor = "center", tags = "confirmation")
    feedbackTime = 1000
    canvas.after(ms = feedbackTime, func = doInterTrial)

def doInterTrial():
    for tokenIndex in range(trial.tokenCount):
        canvas.delete("token")
    canvas.delete("confirmation")
    interTrialTime = 1000
    canvas.after(ms = interTrialTime, func = startNextTrial)

def startNextTrial():
    trial.index += 1
    if trial.index < len(trialCodeList):
        startTrial()
    else:
        endSession()

def endSession():
    bye = "SUA TAREFA ACABOU!"
    byeTop = 100
    canvas.create_text(canvasWidth/2, byeTop, text = bye,
        font = "Arial 20", anchor = "n", tags = "bye")
    messageTime = 5 * 1000
    canvas.after(ms = messageTime, func = saveSessionData)

def saveSessionData():
    dataFile = False
    while not dataFile:
        dataFile = tkFileDialog.asksaveasfile(defaultextension = ".dat",
            initialdir = "/home/ft/temp")
    dataFile.writelines(choiceDataList)
    dataFile.close()

# main program
trialCodeList = blockCodeList() + blockCodeList()
choiceDataList = []

window = Tk()
setWindow()

canvas = Canvas(bg = "white")
canvas.pack(expand = "yes", fill = "both")
canvasWidth, canvasHeight = window.wm_maxsize()

startTrial()

window.mainloop()