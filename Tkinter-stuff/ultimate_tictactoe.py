from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

# X starts so true
clicked = True
count = 0


# to allow playing on the area assigned by playing button 1 or 2 or 3 .... [ tic tac toe 1 ]
def disable_tic_one():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_two():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_3():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_4():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_5():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_6():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_7():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_8():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


def disable_tic_9():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 2 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_10():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_11():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_12():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_13():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_14():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_15():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_16():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_17():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_18():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 3 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_19():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_20():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_21():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_22():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_23():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_24():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_25():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_26():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_27():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 4 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_28():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_29():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_30():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_31():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_32():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_33():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_34():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_35():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_36():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 5 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_37():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_38():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_39():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_40():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_41():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_42():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_43():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_44():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_45():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 6 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_46():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_47():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_48():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_49():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_50():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_51():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_52():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_53():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_54():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 7 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_55():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_56():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_57():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_58():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_59():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_60():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_61():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_62():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_63():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


#  [ tic tac toe 8 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_64():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_65():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_66():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_67():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_68():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_69():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_70():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_71():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_72():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

#  [ tic tac toe 9 ]  SAME AS DISABLE_TIC_ONE
def disable_tic_73():
    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED) #


#   SAME AS DISABLE_TIC_TWO
def disable_tic_74():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_3
def disable_tic_75():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_4
def disable_tic_76():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_5
def disable_tic_77():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_6
def disable_tic_78():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_7
def disable_tic_79():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_8
def disable_tic_80():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


#   SAME AS DISABLE_TIC_9
def disable_tic_81():
    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)


# to enable all buttons again
def enable_all_buttons():
    # 1st tic tac toe
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)

    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)

    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)

    # 2nd tic tac toe
    b10.config(state=NORMAL)
    b11.config(state=NORMAL)
    b12.config(state=NORMAL)

    b13.config(state=NORMAL)
    b14.config(state=NORMAL)
    b15.config(state=NORMAL)

    b16.config(state=NORMAL)
    b17.config(state=NORMAL)
    b18.config(state=NORMAL)

    # 3rd tic tac toe
    b19.config(state=NORMAL)
    b20.config(state=NORMAL)
    b21.config(state=NORMAL)

    b22.config(state=NORMAL)
    b23.config(state=NORMAL)
    b24.config(state=NORMAL)

    b25.config(state=NORMAL)
    b26.config(state=NORMAL)
    b27.config(state=NORMAL)

    # 4th tic tac toe
    b28.config(state=NORMAL)
    b29.config(state=NORMAL)
    b30.config(state=NORMAL)

    b31.config(state=NORMAL)
    b32.config(state=NORMAL)
    b33.config(state=NORMAL)

    b34.config(state=NORMAL)
    b35.config(state=NORMAL)
    b36.config(state=NORMAL)

    # 5th tic tac toe
    b37.config(state=NORMAL)
    b38.config(state=NORMAL)
    b39.config(state=NORMAL)

    b40.config(state=NORMAL)
    b41.config(state=NORMAL)
    b42.config(state=NORMAL)

    b43.config(state=NORMAL)
    b44.config(state=NORMAL)
    b45.config(state=NORMAL)

    # 6th tic tac toe
    b46.config(state=NORMAL)
    b47.config(state=NORMAL)
    b48.config(state=NORMAL)

    b49.config(state=NORMAL)
    b50.config(state=NORMAL)
    b51.config(state=NORMAL)

    b52.config(state=NORMAL)
    b53.config(state=NORMAL)
    b54.config(state=NORMAL)

    # 7th tic tac toe
    b55.config(state=NORMAL)
    b56.config(state=NORMAL)
    b57.config(state=NORMAL)

    b58.config(state=NORMAL)
    b59.config(state=NORMAL)
    b60.config(state=NORMAL)

    b61.config(state=NORMAL)
    b62.config(state=NORMAL)
    b63.config(state=NORMAL)

    # 8th tic tac toe
    b64.config(state=NORMAL)
    b65.config(state=NORMAL)
    b66.config(state=NORMAL)

    b67.config(state=NORMAL)
    b68.config(state=NORMAL)
    b69.config(state=NORMAL)

    b70.config(state=NORMAL)
    b71.config(state=NORMAL)
    b72.config(state=NORMAL)

    # 9th tic tac toe
    b73.config(state=NORMAL)
    b74.config(state=NORMAL)
    b75.config(state=NORMAL)

    b76.config(state=NORMAL)
    b77.config(state=NORMAL)
    b78.config(state=NORMAL)

    b79.config(state=NORMAL)
    b80.config(state=NORMAL)
    b81.config(state=NORMAL)


# disable all buttons [ for when game is over
def disable_all_buttons():

    # 1st tic tac toe
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # 2nd tic tac toe
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)

    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)

    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)

    # 3rd tic tac toe
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)

    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)

    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

    # 4th tic tac toe
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)

    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)

    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

    # 5th tic tac toe
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)

    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)

    # 6th tic tac toe
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)

    b49.config(state=DISABLED)
    b50.config(state=DISABLED)
    b51.config(state=DISABLED)

    b52.config(state=DISABLED)
    b53.config(state=DISABLED)
    b54.config(state=DISABLED)

    # 7th tic tac toe
    b55.config(state=DISABLED)
    b56.config(state=DISABLED)
    b57.config(state=DISABLED)

    b58.config(state=DISABLED)
    b59.config(state=DISABLED)
    b60.config(state=DISABLED)

    b61.config(state=DISABLED)
    b62.config(state=DISABLED)
    b63.config(state=DISABLED)

    # 8th tic tac toe
    b64.config(state=DISABLED)
    b65.config(state=DISABLED)
    b66.config(state=DISABLED)

    b67.config(state=DISABLED)
    b68.config(state=DISABLED)
    b69.config(state=DISABLED)

    b70.config(state=DISABLED)
    b71.config(state=DISABLED)
    b72.config(state=DISABLED)

    # 9th tic tac toe
    b73.config(state=DISABLED)
    b74.config(state=DISABLED)
    b75.config(state=DISABLED)

    b76.config(state=DISABLED)
    b77.config(state=DISABLED)
    b78.config(state=DISABLED)

    b79.config(state=DISABLED)
    b80.config(state=DISABLED)
    b81.config(state=DISABLED)


# check if someone won
def check_winner():
    global winner
    winner = False

    # CHECK IF X HAS WON
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner", "X is the winner...")
        disable_all_buttons()

    # CHECK IF O HAS WON

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Winner", "O is the winner...")
        disable_all_buttons()

    # check if tie
    if count == 81 and winner == False:
        messagebox.showinfo("Tie", "There is no winner\n     You suck!!")
        disable_all_buttons()


# build function for when button 1 is clicked [ note: it has to mark area for next move ]
# [ TIC TAC TOE 1 ]
def b1_clicked(b):
    global clicked, count
    enable_all_buttons()
    disable_tic_one()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b2_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_two()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# function when button 3 is clicked
def b3_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_3()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# function when button 4 is clicked
def b4_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_4()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# function when button 5 is clicked
def b5_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_5()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b6_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_6()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b7_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_7()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b8_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_8()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b9_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_9()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 2 ]
def b10_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_10()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b11_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_11()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b12_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_12()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b13_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_13()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b14_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_14()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b15_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_15()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b16_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_16()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b17_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_17()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b18_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_18()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 3 ]
def b19_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_19()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b20_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_20()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b21_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_21()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b22_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_22()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b23_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_23()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b24_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_24()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b25_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_25()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b26_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_26()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b27_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_27()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 4 ]
def b28_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_28()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b29_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_29()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b30_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_30()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b31_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_31()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b32_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_32()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b33_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_33()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b34_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_34()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b35_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_35()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b36_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_36()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 5 ]

def b37_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_37()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b38_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_38()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b39_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_39()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b40_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_40()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b41_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_41()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b42_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_42()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b43_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_43()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b44_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_44()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b45_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_45()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 6 ]

def b46_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_46()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b47_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_47()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b48_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_48()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b49_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_49()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b50_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_50()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b51_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_51()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b52_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_52()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b53_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_53()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b54_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_54()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 7 ]

def b55_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_55()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b56_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_56()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b57_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_57()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b58_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_58()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b59_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_59()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b60_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_60()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b61_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_61()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b62_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_62()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b63_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_63()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 8 ]

def b64_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_64()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b65_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_65()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b66_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_66()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b67_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_67()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b68_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_68()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b69_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_69()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b70_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_70()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b71_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_71()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b72_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_72()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# [ TIC TAC TOE 9 ]

def b73_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_73()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b74_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_74()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b75_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_75()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b76_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_76()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b77_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_77()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b78_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_78()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b79_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_79()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b80_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_80()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


def b81_clicked(b):
    global clicked, count
    # first I need to set the buttons to normal, otherwise it'd cause a bug
    enable_all_buttons()
    # secondly disable all areas except the one I need to play in
    disable_tic_81()

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")

# [ CONTINUE THE NEXT 60 BUTTONS! :( ]


# button click function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Error", "THAT SPOT IS TAKEN\nPICK ANOTHER SPOT\n         DUMMY!")


# start game over
def reset():

    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23
    global b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44
    global b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62, b63, b64, b65
    global b66, b67, b68, b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79, b80, b81

    global clicked, count
    clicked = True
    count = 0

    # building buttons for 1st tic tac toe
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b1_clicked(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b2_clicked(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b3_clicked(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b4_clicked(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b5_clicked(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b6_clicked(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b7_clicked(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b8_clicked(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: b9_clicked(b9))

    # building buttons for 2nd tic tac toe
    b10 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b10_clicked(b10))
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b11_clicked(b11))
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b12_clicked(b12))

    b13 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b13_clicked(b13))
    b14 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b14_clicked(b14))
    b15 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b15_clicked(b15))

    b16 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b16_clicked(b16))
    b17 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b17_clicked(b17))
    b18 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                command=lambda: b18_clicked(b18))

    # building buttons for 3rd tic tac toe
    b19 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b19_clicked(b19))
    b20 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b20_clicked(b20))
    b21 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b21_clicked(b21))

    b22 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b22_clicked(b22))
    b23 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b23_clicked(b23))
    b24 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b24_clicked(b24))

    b25 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b25_clicked(b25))
    b26 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b26_clicked(b26))
    b27 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b27_clicked(b27))

    # building buttons for 4th tic tac toe
    b28 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b28_clicked(b28))
    b29 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b29_clicked(b29))
    b30 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b30_clicked(b30))

    b31 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b31_clicked(b31))
    b32 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b32_clicked(b32))
    b33 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b33_clicked(b33))

    b34 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b34_clicked(b34))
    b35 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b35_clicked(b35))
    b36 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b36_clicked(b36))

    # building buttons for 5th tic tac toe
    b37 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b37_clicked(b37))
    b38 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b38_clicked(b38))
    b39 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b39_clicked(b39))

    b40 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b40_clicked(b40))
    b41 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b41_clicked(b41))
    b42 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b42_clicked(b42))

    b43 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b43_clicked(b43))
    b44 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b44_clicked(b44))
    b45 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b45_clicked(b45))

    # building buttons for 6th tic tac toe
    b46 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b46_clicked(b46))
    b47 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b47_clicked(b47))
    b48 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b48_clicked(b48))

    b49 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b49_clicked(b49))
    b50 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b50_clicked(b50))
    b51 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b51_clicked(b51))

    b52 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b52_clicked(b52))
    b53 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b53_clicked(b53))
    b54 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b54_clicked(b54))

    # [ CONTINUE NEXT 3 TIC TAC TOE]

    # building buttons for 7th tic tac toe
    b55 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b55_clicked(b55))
    b56 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b56_clicked(b56))
    b57 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b57_clicked(b57))

    b58 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b58_clicked(b58))
    b59 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b59_clicked(b59))
    b60 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b60_clicked(b60))

    b61 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b61_clicked(b61))
    b62 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b62_clicked(b62))
    b63 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b63_clicked(b63))

    # building buttons for 8th tic tac toe
    b64 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b64_clicked(b64))
    b65 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b65_clicked(b65))
    b66 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b66_clicked(b66))

    b67 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b67_clicked(b67))
    b68 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b68_clicked(b68))
    b69 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b69_clicked(b69))

    b70 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b70_clicked(b70))
    b71 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b71_clicked(b71))
    b72 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="#bdbdbd",
                 command=lambda: b72_clicked(b72))

    # building buttons for 9th tic tac toe
    b73 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b73_clicked(b73))
    b74 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b74_clicked(b74))
    b75 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b75_clicked(b75))

    b76 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b76_clicked(b76))
    b77 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b77_clicked(b77))
    b78 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b78_clicked(b78))

    b79 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b79_clicked(b79))
    b80 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b80_clicked(b80))
    b81 = Button(root, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace",
                 command=lambda: b81_clicked(b81))

    # grid/position buttons for 1st tic tac toe [ 1st row of ultimate tic tac toe ]
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    # grid/position buttons for 2nd tic tac toe
    b10.grid(row=0, column=3)
    b11.grid(row=0, column=4)
    b12.grid(row=0, column=5)

    b13.grid(row=1, column=3)
    b14.grid(row=1, column=4)
    b15.grid(row=1, column=5)

    b16.grid(row=2, column=3)
    b17.grid(row=2, column=4)
    b18.grid(row=2, column=5)

    # grid/position buttons for 3rd tic tac toe
    b19.grid(row=0, column=6)
    b20.grid(row=0, column=7)
    b21.grid(row=0, column=8)

    b22.grid(row=1, column=6)
    b23.grid(row=1, column=7)
    b24.grid(row=1, column=8)

    b25.grid(row=2, column=6)
    b26.grid(row=2, column=7)
    b27.grid(row=2, column=8)

    # grid/position buttons for 4th tic tac toe [ 2nd row of ultimate tic tac toe ]
    b28.grid(row=3, column=0)
    b29.grid(row=3, column=1)
    b30.grid(row=3, column=2)

    b31.grid(row=4, column=0)
    b32.grid(row=4, column=1)
    b33.grid(row=4, column=2)

    b34.grid(row=5, column=0)
    b35.grid(row=5, column=1)
    b36.grid(row=5, column=2)

    # grid/position buttons for 5th tic tac toe
    b37.grid(row=3, column=3)
    b38.grid(row=3, column=4)
    b39.grid(row=3, column=5)

    b40.grid(row=4, column=3)
    b41.grid(row=4, column=4)
    b42.grid(row=4, column=5)

    b43.grid(row=5, column=3)
    b44.grid(row=5, column=4)
    b45.grid(row=5, column=5)

    # grid/position buttons for 6th tic tac toe
    b46.grid(row=3, column=6)
    b47.grid(row=3, column=7)
    b48.grid(row=3, column=8)

    b49.grid(row=4, column=6)
    b50.grid(row=4, column=7)
    b51.grid(row=4, column=8)

    b52.grid(row=5, column=6)
    b53.grid(row=5, column=7)
    b54.grid(row=5, column=8)

    # grid/position buttons for 7th tic tac toe [ 3rd row of ultimate tic tac toe ]
    b55.grid(row=6, column=0)
    b56.grid(row=6, column=1)
    b57.grid(row=6, column=2)

    b58.grid(row=7, column=0)
    b59.grid(row=7, column=1)
    b60.grid(row=7, column=2)

    b61.grid(row=8, column=0)
    b62.grid(row=8, column=1)
    b63.grid(row=8, column=2)

    # grid/position buttons for 8th tic tac toe
    b64.grid(row=6, column=3)
    b65.grid(row=6, column=4)
    b66.grid(row=6, column=5)

    b67.grid(row=7, column=3)
    b68.grid(row=7, column=4)
    b69.grid(row=7, column=5)

    b70.grid(row=8, column=3)
    b71.grid(row=8, column=4)
    b72.grid(row=8, column=5)

    # grid/position buttons for 9th tic tac toe
    b73.grid(row=6, column=6)
    b74.grid(row=6, column=7)
    b75.grid(row=6, column=8)

    b76.grid(row=7, column=6)
    b77.grid(row=7, column=7)
    b78.grid(row=7, column=8)

    b79.grid(row=8, column=6)
    b80.grid(row=8, column=7)
    b81.grid(row=8, column=8)


# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# create options for menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()
