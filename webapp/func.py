from flask import request

#fungsi buat ngeliat apakah semua args yg dibutuhin ada
def checkArgs(arg):
    temp = True
    for ar in arg:
        temp = temp and (ar in request.args)
    return temp
