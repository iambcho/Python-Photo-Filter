#!/usr/bin/env python

# import sys, os
import image_utils
from PIL import Image



def insta():
    # os.system('clear')

    print("___________________________________________________\n")
    print("\n")
    print("\n")
    print("----------------------INSTA.PY---------------------\n")
    print("A program to fulfill all your image filtering needs~")
    print("\n")
    print("\n")
    print("___________________________________________________\n")
    print("(f)ilter an image or (q)uit:")

    user = input(" >>  ")


    if user == 'q':
        exit
    elif user == 'f':

        imagepath = input("What's the full path to your image?\n")
        userimg = Image.open(imagepath)
        newimg = Image.new('RGB', (userimg.size[0], userimg.size[1]))

        filter = input("Write a series of filters to apply:"
                       "\n(p)ixelate\n(k)aleidoscope\n(g)ray-day\n(r)ighty\n(t)etris"
                       "\nExample: kpkr will run kaleidoscope, pixelate, kaleidoscope, and gray day in sequence.\n ")

        diff_filters = list(filter)
        count = 0

        for item in diff_filters:

            if item == 'p' or 'k' or 'g' or 'r' or 't':
                if item == 'g':
                    newimg = image_utils.grayscale(userimg)
                elif item == 'p':
                    newimg = image_utils.pixelate(userimg)
                elif item == 'k':
                    newimg = image_utils.kaleidoscope(userimg)
                elif item == 'r':
                    newimg = image_utils.flip(userimg)
                elif item == 't':
                    newimg = image_utils.tetris_filter(userimg)
                userimg = newimg
                count += 1
            else:
                if len(diff_filters) <= 1:
                    if count <= 1:
                        userimg = Image.open(imagepath)
                        userimg.open
                    else:
                        continue
                else:
                    continue
        userimg.show()
        insta()

    elif user == '':
        insta()
    else:
        insta()

insta()
