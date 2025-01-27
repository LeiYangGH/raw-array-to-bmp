import os

WIDTH = 1052
HEIGHT = 780


def read_file(file):
    with open(file, 'r', encoding='utf8', errors='ignore') as f:
        return f.read()


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def read_img_array(file_name):
    data = read_file(file_name).replace('[', '').replace(']', '')
    arr = []
    for x in data.split(','):
        if represents_int(x):
            arr.append(int(x))
    return arr

    # 这个头是我用画图工具创建了个1052, 780的bmp文件，
    # 然后复制出来的头信息


header_array = [0x42, 0x4D, 0x26, 0x90, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x36, 0x00, 0x00, 0x00, 0x28, 0x00,
                0x00,
                0x00, 0x1C, 0x04, 0x00, 0x00, 0x0C, 0x03, 0x00, 0x00, 0x01, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00,
                0x00,
                0xF0, 0x8F, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00,
                0x00, 0x00, 0x00]


def raw_array_to_bmp_1(img_array, file_name):
    print(len(img_array))
    with  open(file_name, "wb") as fw:
        global header_array
        for h in header_array:
            fw.write(bytes([h]))
        for b in img_array:
            fw.write(bytes([b]))
    print(f'wrote to {file_name}')


def raw_array_to_bmp_2(img_array, file_name):
    from PIL import Image
    img_bytes = bytes(img_array)
    # 如果直接用file.read()
    # 读出来的就是bytes，
    # 但由于你给我的是list of int
    # 就要转换一下
    red, green, blue = Image.frombytes('RGB', (WIDTH, HEIGHT), img_bytes).split()
    image = Image.merge('RGB', (blue, green, red))
    image.save(file_name)
    print(f'wrote to {file_name}')


def show_img_array_tk(img_array):
    import tkinter as tk
    from PIL import Image, ImageTk
    root = tk.Tk()
    img_bytes = bytes(img_array)
    red, green, blue = Image.frombytes('RGB', (WIDTH, HEIGHT), img_bytes).split()
    image = Image.merge('RGB', (blue, green, red))
    img = ImageTk.PhotoImage(image=image)
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=img)
    root.mainloop()


if __name__ == '__main__':
    # basepath = r'C:\Users\LeiYang\Downloads'
    basepath = r'C:\Users\YANG.LEI\Downloads'
    datapath = os.path.join(basepath, 'data.txt')
    img_array = read_img_array(datapath)
    # raw_array_to_bmp_1(img_array, r'C:\Users\LeiYang\Downloads\addheader.bmp')
    # raw_array_to_bmp_2(img_array, r'C:\Users\LeiYang\Downloads\pilsave.bmp')
    show_img_array_tk(img_array)
