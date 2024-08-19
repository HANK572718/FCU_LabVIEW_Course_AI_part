# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# def read_image(filename, hotpixelremove=False):
#     '''
#     Reads an image file (supports multiple formats) using PIL and returns appropriate count values.
#     Optionally removes hot pixels.

#     :param filename: The image file path.
#     :param hotpixelremove: If True, apply hot pixel removal.
#     :return: Image data as a float64 numpy array.
#     '''
#     # 打開圖像
#     image = Image.open(filename)

#     # 將圖像轉換為 NumPy 陣列
#     ret = np.array(image)

#     # 根據圖像的類型處理位深度
#     if ret.dtype == np.uint16:
#         # 假設圖像是 16 位深度
#         significant_bits = 16
#     elif ret.dtype == np.uint8:
#         # 假設圖像是 8 位深度
#         significant_bits = 8
#     else:
#         significant_bits = 16  # 預設為 16 位

#     # 對於任何其他位深度的處理，你可以進行相應的調整
#     ret = ret >> (16 - significant_bits)

#     if hotpixelremove:
#         import scipy.ndimage
#         ret = scipy.ndimage.grey_opening(ret, size=(3, 3))
    
#     return np.float64(ret)

# if __name__ == "__main__":
#     image = read_image("MachineLearning/data/duck_dog.jpg")
#     plt.imshow(image)
#     plt.axis('off')  # 不顯示坐標軸
#     plt.show()
#     # print("ok")
# # def readpng(filename, hotpixelremove=False):
# #     '''
# #     Reads a png file and returns appropriate count vales, even if a bit depth
# #     other than 8 or 16 is used. An example this might be needed is having a
# #     12-bit png recorded from a 12-bit camera using LabViews IMAQ toolset.
# #     In this case the PIL (python image library) fails to retrieve the
# #     original count values. 
# #     '''
# #     import png  # pypng
# #     import scipy.misc as sm
# #     import numpy as np
# #     meta = png.Reader(filename)
# #     meta.preamble()
# #     significant_bits = ord(meta.sbit)
# #     ret = sm.imread(filename)
# #     ret >>= 16 - significant_bits
# #     if hotpixelremove:
# #         import scipy.ndimage
# #         ret = scipy.ndimage.morphology.grey_opening(ret, size=(3,3))
# #     return np.float64(ret)