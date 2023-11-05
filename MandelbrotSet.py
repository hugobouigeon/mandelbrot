"""
I'm gonna reimplement the mandelbrot set progrmm I made but with numpy

"""

## imports

import numpy as np
import matplotlib.pyplot as plt
import time as ti
import random as rd

## backEnd

def iterableFucntion(c,z):
    return c + z**2

def initializeMatrix(xCenter=0,yCenter=0,length=1,height=1,resolution=256):
    #initialize the matrix with complex plane

    h = int(height * resolution*2+1)
    l = int(length * resolution*2+1)

    matrix = np.zeros((l,h),dtype=complex)

    for y in range(h):
        for x in range(l):

            matrix[x,y] = complex((xCenter-length+x/resolution),(yCenter-height+y/resolution))

    return matrix



def step(M,M0,Mvis):
    h = len(M)
    l = len(M[0])
    Mbis = np.zeros((h,l),dtype=complex)
    for x in range(l):
        for y in range(l):
            if abs(Mvis[y,x])==-1:
                Mbis[y,x] = iterableFucntion(M0[y,x],M[y,x])
    return Mbis



def mandelbrotSet(xCenter=-0.5,yCenter=0,length=1.5,height=1.2,resolution=256,iterations=16):

    maxdim=max(length,height)

    h = int(height * resolution*2+1)
    l = int(length * resolution*2+1)

    M0 = initializeMatrix(xCenter,yCenter,length,height,resolution)

    M = initializeMatrix(xCenter,yCenter,length,height,resolution)

    visualMatrix = np.zeros((h,l), dtype = int) - 1

    for y in range(h):
        for x in range(l):
            if abs(M[x,y]) > 2:
                visualMatrix[y,x] = 0
                M[x,y]=complex(0,0)
                M0[x,y]=complex(0,0)

    for i in range(iterations):

        M = M**2+M0

        for y in range(h):
            for x in range(l):
                if visualMatrix[y,x] == -1:
                    if abs(M[x,y]) > 2:
                        visualMatrix[y,x] = i+1
                        M[x,y]=complex(0,0)
                        M0[x,y]=complex(0,0)

    for y in range(h):
        for x in range(l):
            if visualMatrix[y,x] == -1:
                visualMatrix[y,x] = 1.1*iterations

    return visualMatrix

##visual

def visual(M):
    plt.matshow(M,cmap=plt.cm.plasma)
    plt.show()

##find cool points

def electNextCenter(M,iterationlimit):
    L=[]
    Lnotborder=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i,j] == iterationlimit:
                L.append([i,j])
                if i>len(M)//6 and i<5*len(M)//6 and j>len(M[0])//6 and j<5*len(M[0])//6:
                    s = M[i+10,j] + M[i,j+10] +M [i-10,j] + M[i-10,j]
                    if s < 5 * iterationlimit:
                        Lnotborder.append([i,j])
    if len(L) == 0:
        return False
    elif len(Lnotborder) == 0:
        return L[rd.randint(0,len(L)-1)]
    else:
        return Lnotborder[rd.randint(0,len(Lnotborder)-1)]

def goDeep(xCenter=-0.5,yCenter=0,length=2,height=1.5,resolution=128,iterations=16,maxdepth=3):

    plt.clf()
    t0 = ti.time()

    iterationsincrement = 2* iterations

    for d in range(maxdepth):
        visM = mandelbrotSet(xCenter,yCenter,length,height,resolution,iterations)

        res = electNextCenter(visM,iterations)

        if not res:
            print("break")
            break
        y,x = res

        xCenter = xCenter-length+x/resolution
        yCenter = yCenter-height+y/resolution

        length /= 3
        height /= 3

        #iterations += iterationsincrement
        iterations = int(iterations*1.5)
        resolution *=3



        #dowload pix
        plt.matshow(visM,cmap=plt.cm.magma)
        plt.savefig('C:/Users/hugob/Desktop/studies/Polytechnique/Python&saucisson/visuals/fractal frames/fig'+str(d)+'.png')
        plt.close('all')

        print("center:")
        print(xCenter,yCenter)

        print("dimensions:")
        print(length,height)

        print("iterations:")
        print(iterations)

        print("time:")
        print(ti.time() - t0)
        print("")
        print("")

    return visM

## cleanZoom

def interpolateZoom(M0,x,y,d,nbOfSteps=10):
    l=len(M0[0])
    h=len(M0)
    for i in range(nbOfSteps):
        newl = l * (nbOfSteps-i)/nbOfSteps + l/3 * i/nbOfSteps
        newh = h * (nbOfSteps-i)/nbOfSteps + h/3 * i/nbOfSteps

        M = M0[int(max(y-newh//2,0)):int(y+newh//2),int(max(x-newl//2,0)):int(x+newl//2)]



        plt.matshow(M,cmap=plt.cm.magma)
        plt.savefig('C:/Users/hugob/Desktop/studies/Polytechnique/Python&saucisson/visuals/fractal frames/fig'+str(d)+'.'+str(i)+'.png')

    plt.clf()


def cleanZoom(xCenter=-0.5,yCenter=0,length=2,height=1.5,resolution=128,iterations=16,maxdepth=3):

    plt.clf()
    t0 = ti.time()

    iterationsincrement = 2* iterations

    for d in range(maxdepth):
        visM = mandelbrotSet(xCenter,yCenter,length,height,resolution,iterations)

        res = electNextCenter(visM,iterations)

        if not res:
            print("break")
            break
        y,x = res

        xCenter = xCenter-length+x/resolution
        yCenter = yCenter-height+y/resolution

        length /= 3
        height /= 3

        iterations += iterationsincrement
        iterations = int(iterations*1.2)
        resolution *=3



        #dowload pix
        interpolateZoom(visM,x,y,d,nbOfSteps=10)

        print("center:")
        print(xCenter,yCenter)

        print("dimensions:")
        print(length,height)

        print("iterations:")
        print(iterations)

        print("time:")
        print(ti.time() - t0)
        print("")
        print("")

    return visM


























