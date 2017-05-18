import pyinsim

def multi_car_info(insim, mci):
    for info in mci.Info:
        print 'X: %d Y: %d Z: %d' % (info.X, info.Y, info.Z)

insim = pyinsim.insim('127.0.0.1', 29999, Flags=pyinsim.ISF_MCI, Admin='password')

insim.bind(pyinsim.ISP_MCI, multi_car_info)

pyinsim.run()
