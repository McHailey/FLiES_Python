import common
from iparam import Parameters
import numpy as np
import ERRCODE
from G_Function import G_Function
from ipf import ipf
from idivspace import idivspace
from clai import CLAI
import datetime

# only in main
knmix = 10
knang = 2000
knzext = 200
fpv = [0.0] * 101
fpc = fpf = 0.0
i = ip = iwl = iz = num = 0

plai = [0.0] * 100
wkd = [0.0] * common.K_NKD
ang = [0.0] * knang
re = [0.0] * knmix
Qext_ref = [0.0] * knmix
Qext = [0.0] * knmix
G = [0.0] * knmix
Qabs = [0.0] * knmix
omg = [0.0] * knmix
phs = np.zeros(knmix * knang, dtype=float).reshape(knmix, knang)
ext = np.zeros(knmix * knzext, dtype=float).reshape(knmix, knzext)

# photon data
nscat = nscata = ichi = ikd = 0
x = y = z = ux = uy = uz = w = 0.0

# function parapeters
# real fsin, fcos, facos, r_acos,frnd

Nid = 0
Nprod = 1  # common.T_SIN[-1] = 5
# print(common.T_SIN)

def main():
    if (Nid == 0):
        print("*********************************************")
        print("3D canopy-atmosphere radiative transfer model")
        print("Forest Light Environmental Simulator (FLiES) ")
        print("                         by Hideki Kobayashi ")
        print("        Special thanks to Hironobu Iwabuchi  ")
        print("                      Since Ver2.00 2008/5/1  ")
        print("*********************************************")

    # ---- Preparation of the initial condition -------
    # set by iparam
    print("iparam")
    print("Parameters initialization...")
    para = Parameters()
    errCode = para.readParameters()

    if (errCode):
        return errCode

    # Initialize math function
    print("imath")

    # number the initial file read devide (5 for standard input)
    num = 5

    # Read required parameters

    # igtbl
    if (para.surfaceType == 2):
        print("G-function")     # G-function LUT
        gFunction = G_Function()
        errCode = gFunction.igtbl()

        if errCode:
            return errCode

        print("idivspace")      # Initialize space division
        errCode = idivspace()

        print("ipf")            # LUT for phase function
        ipf()

    # fish eye image at the forest floor
    # call local estimation for fish eye image
    if (para.nPhoton == -4):
        tgx = int(input("Input the x, y position of view\n"))
        tgy = int(input())

        # to be continue, not important

        return ERRCODE.SUCCESS

    #  LAI calculation
    if (para.nPhoton == -5):
        # spn = float(input("input sampling grid (m), suggested value is 0.1 (m)\n"))
        # debug
        spn = 0.1
        cLAI = CLAI()
        cLAI.calLAI(spn)

        print("LAI = ", cLAI.LAI)
        print("Crown cover = ", cLAI.crownCover)
        print("pLAI is")
        print(cLAI.pLAI)
        print("Finish print LAI.")
    return ERRCODE.SUCCESS



# ##################################################################
# # errCode = main()
# np.set_printoptions(threshold=1000)
# para = Parameters()
# gFunction = G_Function()
# errCode = gFunction.igtbl(para)
# para.nts = 2
# para.process202()
# errCode = idivspace.idivspace()
# print(common.Z_MAX)
# ERRCODE.printMessage(errCode)
# import math
# time.sleep(2)

# a = np.zeros((6 + 1) * (6 + 1), dtype=float).reshape((6 + 1), (6 + 1))
#
# print(a[1][1])
# print(a[1, 1])

START_TIME = datetime.datetime.now()

errCode = main()
ERRCODE.printMessage(errCode)

END_TIME = datetime.datetime.now()
print("TIME USED (HOURS, MINUTES, SECONDS): ", (END_TIME - START_TIME))
